"""
Somewhat borrowed from: https://github.com/namuan/llm-playground/blob/main/local-llm-tools-simple.py
"""

import asyncio
import inspect
import json
from sys import argv
from typing import get_type_hints

from ollama import AsyncClient

# GPT_MODEL: str = "mixtral:8x7b-instruct-v0.1-q6_K"
GPT_MODEL: str = "mixtral:8x22b-instruct"

async def valid_model(model: str) -> bool:
    response = await AsyncClient().list()
    models = [i["name"] for i in response["models"]]
    return (model in models)

async def chat(
    model: str = "phi3:mini", prompt: str = "Why is the sky blue?", **kwargs
) -> dict[str, str]:
    if not await valid_model(model):
        return {}
    response = await AsyncClient().generate(model=model, prompt=prompt, stream=False)
    print(prompt)
    print(response)
    return json.loads(response["response"])


class Article:
    pass


class Weather:
    pass


class Directions:
    pass


def calculate_mortgage_payment(
    loan_amount: int, interest_rate: float, loan_term: int
) -> float:
    """Get the monthly mortgage payment given an interest rate percentage."""
    pass


def get_article_details(
    title: str,
    authors: list[str],
    short_summary: str,
    date_published: str,
    tags: list[str],
) -> Article:
    """
    Get article details from unstructured article text.
    date_published: formatted as "MM/DD/YYYY"
    """
    pass


def get_weather(city: str) -> Weather:
    """Get the current weather given a city."""
    pass

def get_directions(start: str, destination: str) -> Directions:
    """
    Get directions from Google Directions API.
    start: start address as a string including zipcode (if any)
    destination: end address as a string including zipcode (if any)
    """
    pass


def get_type_name(t):
    name = str(t)
    if "list" in name or "dict" in name:
        return name
    else:
        return t.__name__


def function_to_json(func):
    signature = inspect.signature(func)
    type_hints = get_type_hints(func)

    function_info = {
        "name": func.__name__,
        "description": func.__doc__,
        "parameters": {"type": "object", "properties": {}},
        "returns": type_hints.get("return", "void").__name__,
    }

    for name, _ in signature.parameters.items():
        param_type = get_type_name(type_hints.get(name, type(None)))
        function_info["parameters"]["properties"][name] = {"type": param_type}

    return json.dumps(function_info, indent=2)


async def main():
    functions_prompt = f"""
You have access to the following tools:
{function_to_json(get_weather)}
{function_to_json(calculate_mortgage_payment)}
{function_to_json(get_directions)}
{function_to_json(get_article_details)}

You must follow these instructions:
Always select one or more of the above tools based on the user query
If a tool is found, you must respond in the JSON format matching the following schema:
{{
   "tools": {{
        "tool": "<name of the selected tool>",
        "tool_input": <parameters for the selected tool, matching the tool's JSON schema
   }}
}}
If there are multiple tools required, make sure a list of tools are returned in a JSON array.
If there is no tool that match the user request, you will respond with empty json.
Do not add any additional Notes or Explanations

User Query:
    """

    prompts = [
        "What's the weather in New York, NY",
        "Determine the monthly mortgage payment for a loan amount of $200,000, an interest rate of 4%, and a loan term of 30 years.",
        "What's the current exchange rate for GBP to EUR?",
        "I'm planning a trip to Killington, Vermont (05751) from Hoboken, NJ (07030). Can you get me weather for both locations and directions?",
    ]

    for prompt in prompts:
        print(f"❓{prompt}")
        question = functions_prompt + prompt
        response = await chat(GPT_MODEL, question)
        try:
            print(response)
        except Exception as e:
            print(e)
            print(f"❌ Unable to decode JSON. {response}")


asyncio.run(main())
