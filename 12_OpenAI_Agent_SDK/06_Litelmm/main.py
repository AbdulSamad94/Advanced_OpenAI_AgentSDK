import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

# Disable tracing
set_tracing_disabled(disabled=True)

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")

# Define the model name
MODEL = "gemini/gemini-1.5-flash"


@function_tool
def get_weather(city: str) -> str:
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


# Main asynchronous function
async def main(model: str, api_key: str):
    try:
        agent = Agent(
            name="Assistant",
            instructions="You only respond in English.",
            model=LitellmModel(model=model, api_key=api_key),
            tools=[get_weather],
        )

        # Run the agent with a sample input
        result = await Runner.run(agent, "How are you?")
        print(result.final_output)

    except Exception as e:
        print(f"An error occurred: {e}")


# Execute the main function
if __name__ == "__main__":
    asyncio.run(main(model=MODEL, api_key=GEMINI_API_KEY))
