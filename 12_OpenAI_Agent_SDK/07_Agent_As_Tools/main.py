from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client,
)


async def main():
    spanish_agent = Agent(
        name="Spanish agent",
        instructions="You translate the user's message to Spanish",
        model=model,
    )

    french_agent = Agent(
        name="French agent",
        instructions="You translate the user's message to French",
        model=model,
    )


    main_agent = Agent(
        name="main_agent",
        instructions=(
            "You are a translation agent. You use the tools given to you to translate."
            "If asked for multiple translations, you call the relevant tools."
        ),
        model=model,
        tools=[
            spanish_agent.as_tool(
                tool_name="translate_to_spanish",
                tool_description="Translate the user's message to Spanish",
            ),
            french_agent.as_tool(
                tool_name="translate_to_french",
                tool_description="Translate the user's message to French",
            ),
        ],
    )

    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    run = await Runner.run(
        main_agent,
        "Say 'Hello, how are you?' in Spanish and French.",
        run_config=config,
    )
    print(run.final_output)


if __name__ == "__main__":
    asyncio.run(main())
