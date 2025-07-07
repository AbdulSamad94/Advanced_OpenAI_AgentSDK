from agents import (
    Agent,
    Runner,
    RunConfig,
    RunContextWrapper,
    input_guardrail,
    TResponseInputItem,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OpenAIChatCompletionsModel,
)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from pydantic import BaseModel
from agent_instructions import (
    input_guardial_instruction,
    analysis_agent_instruction,
    friendly_agent_instruction,
    main_agent_instruction,
)
from Tools_and_Agent import (
    SummarizerAgent,
    RiskDetectorAgent,
    ClauseCheckerAgent,
    fallback_response,
)


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


class SensitiveCheckOutput(BaseModel):
    contains_sensitive_info: bool
    reasoning: str


class SummaryOutput(BaseModel):
    summary: str


class RiskOutput(BaseModel):
    risks: list[str]


class FinalOutput(BaseModel):
    summary: str
    risks: list[str]
    verdict: str
    disclaimer: str = (
        "This summary is for informational purposes only and does not constitute legal advice."
    )


class FriendlyMessage(BaseModel):
    message: str


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.0-flash")
config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

sensitive_check_agent = Agent(
    name="Sensitive Info Checker",
    instructions=input_guardial_instruction,
    model=model,
    output_type=SensitiveCheckOutput,
)


@input_guardrail
async def sensitive_input_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    if isinstance(input, list):

        user_inputs = [item["content"] for item in input if item["role"] == "user"]
        last_user_input = user_inputs[-1] if user_inputs else ""
    else:
        last_user_input = input

    result = await Runner.run(
        sensitive_check_agent, last_user_input, context=ctx.context
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_sensitive_info,
    )


analysis_agent = Agent(
    name="LegalAnalysisAgent",
    instructions=analysis_agent_instruction,
    input_guardrails=[sensitive_input_guardrail],
    output_type=FinalOutput,
    model=model,
    tools=[
        SummarizerAgent.as_tool(
            tool_name="summarize_document",
            tool_description="Summarize the legal document in clear and concise English.",
        ),
        RiskDetectorAgent.as_tool(
            tool_name="detect_risks",
            tool_description="Identify any risky or problematic clauses in the legal document.",
        ),
        ClauseCheckerAgent.as_tool(
            tool_name="check_clause",
            tool_description="Check if a given clause is legally acceptable or risky.",
        ),
    ],
)

friendly_agent = Agent(
    name="FriendlyResponseAgent",
    instructions=friendly_agent_instruction,
    model=model,
    output_type=FriendlyMessage,
)

main_agent = Agent(
    name="MainLegalAgent",
    instructions=main_agent_instruction,
    model=model,
    input_guardrails=[sensitive_input_guardrail],
    tools=[
        analysis_agent.as_tool(
            tool_name="analyze_document",
            tool_description="Run full legal analysis; returns JSON FinalOutput.",
        ),
        friendly_agent.as_tool(
            tool_name="make_friendly",
            tool_description="Takes JSON analysis; returns a friendly message.",
        ),
        # fallback_response,
    ],
    output_type=FriendlyMessage,
)


async def main():
    history = []
    while True:
        ui = input("User: ")
        try:
            resp = await Runner.run(main_agent, ui, run_config=config)
            print("\nAI says:")
            print(resp.final_output.message, "\n")
            history.append({"role": "user", "content": ui})
            history.append({"role": "assistant", "content": resp.final_output.message})
        except InputGuardrailTripwireTriggered as e:
            print(
                "\n❌ Blocked:", e.guardrail_result.output.output_info.reasoning, "\n"
            )


if __name__ == "__main__":
    asyncio.run(main())
