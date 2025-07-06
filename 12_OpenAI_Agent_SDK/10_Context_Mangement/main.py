from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig,
    function_tool,
    RunContextWrapper,
)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio
import os
from dataclasses import dataclass

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


async def main():
    client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    @dataclass
    class Userinfo:
        name: str
        uid: int

    @function_tool
    async def fetch_user_age(wrapper: RunContextWrapper[Userinfo]) -> str:
        """Fetch the age of the user. Call this function to get user's age information and uid information."""
        return f"The user {wrapper.context.name} is 47 years old and his uid is {wrapper.context.uid}."

    userinfo = Userinfo(name="John Doe", uid=12345)

    agent = Agent[Userinfo](name="Assistant", tools=[fetch_user_age], model=model)

    result = await Runner.run(
        starting_agent=agent,
        run_config=config,
        input="Give me the user's information?",
        context=userinfo,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
