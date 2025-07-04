from agents import Agent, Runner, RunConfig, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


async def main():
    client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    async with MCPServerStdio(
        params={
            "command": "python",
            "args": ["calculator_server.py"],
        }
    ) as calc_server:

        agent = Agent(
            model=model,
            instructions="You are a calculator assistant. Use tools to compute math operations.",
            mcp_servers=[calc_server],
        )
        res = await Runner.run(
            agent,
            "What's 12 * 7 and then subtract 5 from the result?",
            run_config=config,
        )
        print("Agent:", res.final_output)


if __name__ == "__main__":
    asyncio.run(main())
