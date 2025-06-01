from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    function_tool,
    Runner,
    AsyncOpenAI,
    RunConfig,
    set_tracing_disabled,
)
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")

external_client = AsyncOpenAI(
    api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=model,
    )
    history = []  # Initialize history outside the loop to persist across interactions
    while True:
        user_input = input("Enter your question: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the assistant. Goodbye!")
            break

        # Append the user's message to the history
        history.append({"role": "user", "content": user_input})

        # Run the agent with the current history
        result = await Runner.run(agent, history)

        # Append the assistant's response to the history
        history.append({"role": "assistant", "content": result.final_output})

        print(result.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
