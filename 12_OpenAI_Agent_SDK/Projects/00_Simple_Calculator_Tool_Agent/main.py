from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
    function_tool,
)
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("GEMINI_API_KEY is not set. Please set it in the .env file.")


@function_tool
def add(a: float, b: float) -> float:
    """Adds two numbers, but you become a little bit happy and crack a joke about it."""
    return a + b


@function_tool
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers but you become a little bit mad and crack a joke about it."""
    return a - b


@function_tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and say the result in haikiyo."""
    return a * b


@function_tool
def divide(a: float, b: float) -> float:
    """Divides two numbers but normally you would crack a joke with it after dividing, and divide only 30% of the time."""
    return a / b


provider = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)


async def main():
    user_input = input("Enter a mathematical expression (e.g, 'add 2 3'): ")
    if not user_input:
        print("No input provided. Exiting.")
        return
    agent = Agent(
        name="Simple Calculator Agent",
        instructions="You are a simple calculator agent. You can perform basic arithmetic operations like addition, subtraction, multiplication, and division. when someone asks you to add, subtract, multiply or divide two numbers, you will use the tools provided to perform the operation. You will also crack a joke about it.",
        model=model,
        tools=[add, subtract, multiply, divide],
    )

    result = await Runner.run(agent, user_input)
    print(result.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
