from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, SQLiteSession
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio
import os
from rich import print

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.5-flash")
config = RunConfig(model=model, model_provider=client, tracing_disabled=True)


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=model,
    )

    session = SQLiteSession("conversation_123", "conversation.db")

    # First turn
    result = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session,
        run_config=config,
    )
    print(result.final_output)  # "San Francisco"

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(
        agent, "What state is it in?", session=session, run_config=config
    )
    print(result.final_output)  # "California"

    # Also works with synchronous runner
    result = await Runner.run(
        agent, "What's the population?", session=session, run_config=config
    )
    print(result.final_output)

    result = await Runner.run(
        agent,
        "What was the last message of yours and mine?",
        session=session,
        run_config=config,
    )
    print(result.final_output)

    items = await session.get_items()
    print(items)


if __name__ == "__main__":
    asyncio.run(main())
