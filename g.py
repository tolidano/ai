import asyncio
import base64
import json
import os
import pyaudio
from websockets.asyncio.client import connect


class SimpleGeminiVoice:
    def __init__(self):
        self.audio_queue = asyncio.Queue()
        self.api_key = self.get_key()
        self.model = "gemini-2.0-flash-exp"
        self.uri = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key={self.api_key}"
        # Audio settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.CHUNK = 512
        self.RATE = 16000
        self.gemini_talking = False

    def get_key(self):
        key_file = "gemini-key.txt"
        if not os.path.exists(key_file):
            raise ValueError("File missing gemini-key.txt")
        with open(key_file) as f:
            key = f.read().strip()
        if len(key) > 100:
            raise ValueError("Invalid format. Get key here: https://aistudio.google.com/app/apikey")
        return key

    async def start(self):
        self.ws = await connect(
            self.uri, additional_headers={"Content-Type": "application/json"}
        )
        config = {
            "setup": {
                "model": f"models/{self.model}",
                "generation_config": {
                    "speech_config": {
                        "voice_config": {
                            "prebuilt_voice_config": {
                                "voice_name": "Charon", # Puck Charon Kore Fenrir Aoede
                            }
                        }
                    }
                },
                # "system_instruction": "",
                # "tools":[],
            }
        }
        await self.ws.send(json.dumps(config))
        await self.ws.recv(decode=False)
        print("Gemini Online")
        # Start audio streaming
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.capture_audio())
            tg.create_task(self.stream_audio())
            tg.create_task(self.play_response())

    async def capture_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK,
        )

        while True:
            data = await asyncio.to_thread(stream.read, self.CHUNK)
            if self.gemini_talking:
                continue
            await self.ws.send(
                json.dumps({
                    "realtime_input": {
                        "media_chunks": [{
                            "data": base64.b64encode(data).decode(),
                            "mime_type": "audio/pcm",
                        }]
                    }
                })
            )

    async def stream_audio(self):
        async for msg in self.ws:
            response = json.loads(msg)
            try:
                audio_data = response["serverContent"]["modelTurn"]["parts"][0][
                    "inlineData"
                ]["data"]
                self.audio_queue.put_nowait(base64.b64decode(audio_data))
            except KeyError:
                pass
            try:
                turn_complete = response["serverContent"]["turnComplete"]
            except KeyError:
                pass
            else:
                if turn_complete:
                    # If you interrupt the model, it sends an end_of_turn. For interruptions to work, we need to empty out the audio queue
                    print("\nGemini Done")
                    while not self.audio_queue.empty():
                        self.audio_queue.get_nowait()

    async def play_response(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.FORMAT, channels=self.CHANNELS, rate=32000, output=True
        )
        while True:
            data = await self.audio_queue.get()
            if data:
                self.gemini_talking = True
            await asyncio.to_thread(stream.write, data)
            if data:
                self.gemini_talking = False


if __name__ == "__main__":
    client = SimpleGeminiVoice()
    asyncio.run(client.start())
