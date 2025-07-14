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
OPEN_ROUTER_KEY = os.getenv("OPEN_ROUTER_KEY")

if not OPEN_ROUTER_KEY:
    raise ValueError("OPEN_ROUTER_KEY is not set. Please set it in the .env file.")

# Define the model name
MODEL = "perplexity/pplx-7b-online"


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
        )

        # Run the agent with a sample input
        result = await Runner.run(
            agent,
            "Can you search about openai agents sdk and tell me what it actually is?",
        )
        print(result.final_output)

    except Exception as e:
        print(f"An error occurred: {e}")


# Execute the main function
if __name__ == "__main__":
    asyncio.run(main(model=MODEL, api_key=OPEN_ROUTER_KEY))
