import asyncio
from sys import argv
import time

from ollama import AsyncClient as ola

"""
Async client to interact with local Ollama and GCP gemini models

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
GEMINI_HOST: str = "http://localhost:22434"
LOCAL_HOST: str = "http://localhost:11434"
MAX_SIZE: int = 50000000000
MAX_PARAMETER_SIZE: int = 75
DEBUG: bool = True

async def get_model_list(embed: bool = False, max_size: int = MAX_SIZE, max_parameters: int = MAX_PARAMETER_SIZE) -> list[str]:
    response: dict[str, any] = await ola(host=LOCAL_HOST).list()
    models: list[str] = ["gemini-1.5-flash-001"]
    for i in response["models"]:
        m: str = i["model"]
        if not embed and "embed" in m:
            continue
        if "size" in i and i["size"] > max_size:
            continue
        param_size: int = 0
        if "details" in i and "parameter_size" in i["details"] and "M" not in i["details"]["parameter_size"] and i["details"]["parameter_size"]:
            param_size = float(i["details"]["parameter_size"].lower().replace("b", ""))
        if param_size > max_parameters:
            continue
        models.append(m)
    return models

async def valid_model(model: str) -> bool:
    models = await get_model_list()
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
        models = await get_model_list()
    print(f"Using prompt: {prompt}")
    for run in range(runs):
        for i in models:
            stream: bool = True
            host: str = LOCAL_HOST
            if "gemini" in i:
                stream = False
                host = GEMINI_HOST
            start = time.time()
            if DEBUG:
                print("*" * 10 + i + "*" * 10)
            response = await ola(host=host).chat(model=i, messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'content': prompt,
                },
            ], stream=stream)
            diff = 0
            if stream:
                async for chunk in response:
                    print(chunk["message"]["content"], end="", flush=True)
                    if diff == 0:
                        diff = round(time.time() - start, 3)
            else:
                print(response["message"]["content"])
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
