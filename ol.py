import asyncio
from sys import argv
import time

from ollama import AsyncClient as ola

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

SYSTEM_PROMPT: str = "You are a concise artificial intelligence chat bot. You provide clear answers that are easy to read and digest generally under 50 words."
HOST: str = "http://localhost:11434"
DEBUG: bool = True

async def valid_model(model: str) -> bool:
    response = await ola(host=HOST).list()
    models = [i["model"] for i in response["models"]]
    if model not in models:
        print("You must pick one of these models:")
        print("\n".join(models))
        return False
    return True

async def chat(model: str = "phi3:mini", prompt: str = "Why is the sky blue?", runs: int = 1):
    if model != "ALL" and not await valid_model(model):
        return
    models = [model]
    if model == "ALL":
        out = await ola(host=HOST).list()
        models = [i["model"] for i in out["models"]]
    print(f"Using prompt: {prompt}")
    for run in range(runs):
        for i in models:
            start = time.time()
            if DEBUG:
                print("*" * 10 + i + "*" * 10)
            response = await ola(host=HOST).chat(model=i, messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'content': prompt,
                },
            ], stream=True)
            diff = 0
            async for chunk in response:
                print(chunk['message']['content'], end='', flush=True)
                if diff == 0:
                    diff = round(time.time() - start, 3)
            total = round(time.time() - start, 3)
            difftot = round(total - diff, 3)
            if DEBUG:
                print(f"\nFirst token: {diff} sec\tFull response: {total} sec\tOutput time: {difftot}")

async def run():
    model: str = "phi3:latest"
    prompt: str = "Why is the sky blue?"
    runs = 1
    if len(argv) == 2:
        prompt = argv[1]
    elif len(argv) == 3:
        model = argv[1]
        prompt = argv[2]
    elif len(argv) == 4:
        runs = int(argv[1])
        model = argv[2]
        prompt = argv[3]
    print(model)
    await chat(model=model, prompt=prompt, runs=runs)

asyncio.run(run())
