import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()


OPEN_ROUTER_KEY = os.getenv("OPEN_ROUTER_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-chat-v3-0324:free"

client = AsyncOpenAI(api_key=OPEN_ROUTER_KEY, base_url=BASE_URL)

set_tracing_disabled(disabled=True)


async def main():
    # This agent will use the custom LLM provider

    agent = Agent(
        name="Assistant",
        instructions="You are a good assistant sweet assistant.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
