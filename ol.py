import asyncio
from sys import argv

from ollama import AsyncClient

"""
Async client to interact with local Ollama models

Needs:
    python3 -m pip install ollama

Default:
    Download phi3:mini first (`ollama run phi3:mini`)
    python3 ol.py

Use:
    python3 ol.py "<prompt>"
    Will ask phi3:mini your prompt

    python3 ol.py phi3:mini "<prompt>"
    Will ask phi3:mini your prompt
"""

async def chat(model: str = "phi3:mini", prompt: str = "Why is the sky blue?"):
    response = await AsyncClient().list()
    models = [i["name"] for i in response["models"]]
    if model not in models:
        print("You must pick one of these models:")
        print("\n".join(models))
        return
    message = {"role": "user", "content": prompt}
    async for part in await AsyncClient().chat(
        model=model, messages=[message], stream=True
    ):
        print(part["message"]["content"], end="", flush=True)


async def run():
    model: str = "phi3:mini"
    prompt: str = "Why is the sky blue?"
    if len(argv) == 2:
        content = argv[1]
    elif len(argv) > 2:
        model = argv[1]
        prompt = argv[2]
    await chat(model=model, prompt=prompt)


asyncio.run(run())
