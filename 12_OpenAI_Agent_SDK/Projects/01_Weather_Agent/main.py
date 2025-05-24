import os
import chainlit as cl
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
)
from agents.run import RunConfig
from agents.tool import function_tool
from dotenv import load_dotenv
import requests
from typing import Dict, Any

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is not set. Please set it in the .env file.")


@function_tool
@cl.step(type="weather tool")
def get_weather(city: str) -> str:
    """
    Fetches the current weather for a given city.


    Args:
        city: The name of the city.

    Returns:
        A string describing the current weather, or an error message.
    """
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data: Dict[str, Any] = response.json()
        if "current" in data and "temperature" in data["current"]:
            return f"The weather in {city} is {data['current']['temperature']} degrees Celsius. Last updated at {data['current']['observation_time']}."
        else:
            return f"Could not find weather information for {city}."
    else:
        return f"Failed to fetch weather data. Status code: {response.status_code}"


@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash", openai_client=external_client
    )

    config = RunConfig(
        model=model, model_provider=external_client, tracing_disabled=True
    )

    cl.user_session.set("chat_history", [])

    cl.user_session.set("config", config)
    agent: Agent = Agent(
        name="Best Agent",
        instructions="You are a helpful assistant.",
        model=model,
    )
    agent.tools.append(get_weather)
    cl.user_session.set("agent", agent)

    await cl.Message(
        content="Welcome to the AI Weather Assistant! How can I help you today?"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cl.user_session.get("agent")
    config: RunConfig = cl.user_session.get("config")

    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        result = Runner.run_streamed(agent, history, run_config=config)

        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, "delta"):
                token = event.data.delta
                await msg.stream_token(token)

        response_content = result.final_output

        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})

        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
