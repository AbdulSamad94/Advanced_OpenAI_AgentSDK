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
from agent_instructions import input_guardial_instruction, main_agent_instruction

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


async def main():
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

    SummarizerAgent = Agent(
        name="SummarizerAgent",
        instructions="""
        You are an expert legal document summarizer. Given a long legal document or contract, summarize it in clear and concise English that a layman can understand. 
        Avoid jargon and be objective.
        """,
        output_type=SummaryOutput,
        model=model,
    )

    RiskDetectorAgent = Agent(
        name="RiskDetectorAgent",
        instructions="""
        You are a legal risk analysis expert. Analyze the given legal text and identify any risky, vague, or potentially problematic clauses.
        Be specific and return a list of clearly stated risks or concerns.
        """,
        output_type=RiskOutput,
        model=model,
    )

    ClauseCheckerAgent = Agent(
        name="Clause Checker Agent",
        instructions="""
        You are a clause checking agent. When given a legal clause, analyze it and determine if it's risky, unfair, or acceptable. Be short and precise in your answer.
        """,
        output_type=str,
        model=model,
    )

    agent = Agent(
        name="Customer support agent",
        instructions=main_agent_instruction,
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

    history = []
    while True:
        user_input = input("User: ")

        history.append({"role": "user", "content": user_input})
        try:
            result = await Runner.run(agent, history, run_config=config)
            history.append(
                {"role": "assistant", "content": result.final_output.summary}
            )

            print("\n--- Legal Document Analysis ---")
            print(f"📄 Summary:\n{result.final_output.summary}\n")
            print("⚠️ Risks:")
            for risk in result.final_output.risks:
                print(f"- {risk}")
            print(f"\n✅ Verdict:\n{result.final_output.verdict}")
            print(f"\n📢 Disclaimer:\n{result.final_output.disclaimer}\n")

        except InputGuardrailTripwireTriggered as e:
            print(
                f"\n❌ Input blocked:\n{e.guardrail_result.output.output_info.reasoning}"
            )


if __name__ == "__main__":
    asyncio.run(main())
