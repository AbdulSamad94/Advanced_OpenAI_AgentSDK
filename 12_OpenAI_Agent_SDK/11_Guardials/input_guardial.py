from agents import (
    OpenAIChatCompletionsModel,
    Agent,
    Runner,
    RunConfig,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    input_guardrail,
    TResponseInputItem,
)
from pydantic import BaseModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str


async def main():
    client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.0-flash")
    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    guardrail_agent = Agent(
        name="Guardrail check",
        instructions="Check if the user is asking you to do their math homework.",
        output_type=MathHomeworkOutput,
        model=model,
    )

    @input_guardrail
    async def math_guardrail(
        ctx: RunContextWrapper[None],
        agent: Agent,
        input: str | list[TResponseInputItem],
    ) -> GuardrailFunctionOutput:
        result = await Runner.run(guardrail_agent, input, context=ctx.context)

        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=result.final_output.is_math_homework,
        )

    agent = Agent(
        name="Customer support agent",
        instructions="You are a customer support agent. You help customers with their questions.",
        input_guardrails=[math_guardrail],
        model=model,
    )
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        history.append({"role": "user", "content": user_input})
        try:
            result = await Runner.run(agent, history, run_config=config)
            history.append({"role": "assistant", "content": result.final_output})
            print(f"Assistant: {result.final_output}")
            print("Guardrail didn't trip - this is unexpected")
        except InputGuardrailTripwireTriggered as e:
            print("Math homework guardrail tripped")
            print("Math homework guardrail tripped")


if __name__ == "__main__":
    asyncio.run(main())
