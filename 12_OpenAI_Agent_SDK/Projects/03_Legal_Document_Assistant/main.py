from agents import (
    Agent,
    Runner,
    RunConfig,
    RunContextWrapper,
    input_guardrail,
    output_guardrail,
    function_tool,
    TResponseInputItem,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
    OpenAIChatCompletionsModel,
)
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from datetime import datetime
import logging
from pydantic_models import (
    RiskOutput,
    SummaryOutput,
    FinalOutput,
    FriendlyMessage,
    SharedContext,
    SensitiveCheckOutput,
    DocumentCheckOutput,
)
from agent_instructions import (
    analysis_agent_instruction,
    summarizer_agent_instructions,
    risk_agent_instructions,
    clause_agent_instructions,
    document_detector_agent_instructions,
    guardrail_instructions,
    friendly_agent_instruction,
    casual_chat_agent_instruction,
    main_agent_instruction,
)


class SimpleLogger:
    @staticmethod
    def log(step: str, details: str = ""):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {step} {details}")


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

logging.basicConfig(level=logging.DEBUG)

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.0-flash")

summarizer_agent = Agent(
    name="SummarizerAgent",
    instructions=summarizer_agent_instructions,
    output_type=SummaryOutput,
    model=model,
)

risk_detector_agent = Agent(
    name="RiskDetectorAgent",
    instructions=risk_agent_instructions,
    output_type=RiskOutput,
    model=model,
)

clause_checker_agent = Agent(
    name="ClauseCheckerAgent",
    instructions=clause_agent_instructions,
    output_type=str,
    model=model,
)

document_detector_agent = Agent(
    name="DocumentDetector",
    instructions=document_detector_agent_instructions,
    output_type=DocumentCheckOutput,
    model=model,
)

sensitive_check_agent = Agent(
    name="SensitiveInfoChecker",
    instructions=guardrail_instructions,
    output_type=SensitiveCheckOutput,
    model=model,
)


@input_guardrail
async def sensitive_input_guardrail(
    ctx: RunContextWrapper[SharedContext],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    SimpleLogger.log("🛡️ GUARDRAIL", "Checking for sensitive info...")

    if isinstance(input, list):
        user_inputs = [item["content"] for item in input if item["role"] == "user"]
        last_input = user_inputs[-1] if user_inputs else ""
    else:
        last_input = input

    if not ctx.context:
        ctx.context = SharedContext(document_text=last_input)
    else:
        ctx.context.document_text = last_input

    result = await Runner.run(sensitive_check_agent, last_input)

    SimpleLogger.log(
        "🛡️ GUARDRAIL",
        f"Result: {'BLOCKED' if result.final_output.contains_sensitive_info else 'PASSED'}",
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_sensitive_info,
    )


@output_guardrail
async def final_output_validation_guardrail(
    ctx: RunContextWrapper[SharedContext],
    agent: Agent,
    output: FinalOutput,
) -> GuardrailFunctionOutput:
    SimpleLogger.log("🛡️ FINAL_OUTPUT_GUARDRAIL", "Validating final analysis output...")

    has_summary = bool(output.summary and len(output.summary.strip()) > 10)
    has_risks = output.risks is not None and isinstance(output.risks, list)
    has_verdict = bool(output.verdict and len(output.verdict.strip()) > 5)
    has_disclaimer = bool(output.disclaimer and len(output.disclaimer.strip()) > 10)

    is_valid = has_summary and has_risks and has_verdict and has_disclaimer

    SimpleLogger.log(
        "🛡️ FINAL_OUTPUT_GUARDRAIL",
        f"Summary: {'✓' if has_summary else '✗'} | "
        f"Risks: {'✓' if has_risks else '✗'} | "
        f"Verdict: {'✓' if has_verdict else '✗'} | "
        f"Disclaimer: {'✓' if has_disclaimer else '✗'} | "
        f"Result: {'VALID' if is_valid else 'INVALID'}",
    )

    return GuardrailFunctionOutput(
        output_info={
            "validation_passed": is_valid,
            "summary_valid": has_summary,
            "risks_valid": has_risks,
            "verdict_valid": has_verdict,
            "disclaimer_valid": has_disclaimer,
        },
        tripwire_triggered=not is_valid,
    )


# Output Guardrail for FriendlyMessage type
@output_guardrail
async def friendly_message_validation_guardrail(
    ctx: RunContextWrapper[SharedContext],
    agent: Agent,
    output: FriendlyMessage,
) -> GuardrailFunctionOutput:
    SimpleLogger.log(
        "🛡️ FRIENDLY_OUTPUT_GUARDRAIL", "Validating friendly message output..."
    )

    has_message = bool(output.message and len(output.message.strip()) > 5)
    is_not_too_long = len(output.message) < 2000

    contains_inappropriate = any(
        word in output.message.lower()
        for word in ["i cannot", "i can't", "sorry, i cannot", "i'm unable to"]
    )

    is_valid = has_message and is_not_too_long and not contains_inappropriate

    SimpleLogger.log(
        "🛡️ FRIENDLY_OUTPUT_GUARDRAIL",
        f"Has message: {'✓' if has_message else '✗'} | "
        f"Length OK: {'✓' if is_not_too_long else '✗'} | "
        f"Appropriate: {'✓' if not contains_inappropriate else '✗'} | "
        f"Result: {'VALID' if is_valid else 'INVALID'}",
    )

    return GuardrailFunctionOutput(
        output_info={
            "validation_passed": is_valid,
            "has_message": has_message,
            "length_ok": is_not_too_long,
            "appropriate_content": not contains_inappropriate,
        },
        tripwire_triggered=not is_valid,
    )


# @function_tool
# async def analyze_document_full(document: str) -> dict:
#     """
#     Analyze a legal document in 3 steps and return a structured JSON response.

#     Steps to follow:
#     1. Summarize the document using legal summarizer.
#     2. Detect risky or unclear clauses.
#     3. Judge if clauses are fair/risky and return a short verdict.

#     Combine all 3 results into the following JSON format:

#     {
#       "summary": string,
#       "risks": list of strings,
#       "verdict": string,
#       "disclaimer": "This summary is for informational purposes only and does not constitute legal advice."
#     }

#     All steps are required. Do not skip any.
#     """

#     config = RunConfig(model=model, model_provider=client)

#     summary_res = await Runner.run(summarizer_agent, document, run_config=config)
#     summary = summary_res.final_output.summary

#     risks_res = await Runner.run(risk_detector_agent, document, run_config=config)
#     risks = risks_res.final_output.risks

#     clause_res = await Runner.run(clause_checker_agent, document, run_config=config)
#     verdict = (
#         clause_res.final_output
#         if isinstance(clause_res.final_output, str)
#         else str(clause_res.final_output)
#     )

#     final = FinalOutput(summary=summary, risks=risks, verdict=verdict)
#     return final.model_dump()


analysis_agent = Agent(
    name="LegalAnalysisAgent",
    instructions=analysis_agent_instruction,
    input_guardrails=[sensitive_input_guardrail],
    output_guardrails=[final_output_validation_guardrail],
    output_type=FinalOutput,
    model=model,
    tools=[
        summarizer_agent.as_tool(
            tool_name="summarize_document",
            tool_description="Summarize the legal document in clear English.",
        ),
        risk_detector_agent.as_tool(
            tool_name="detect_risks",
            tool_description="Identify risky or problematic clauses.",
        ),
        clause_checker_agent.as_tool(
            tool_name="check_clause",
            tool_description="Check if clauses are legally acceptable.",
        ),
    ],
)

friendly_agent = Agent(
    name="FriendlyResponseAgent",
    instructions=friendly_agent_instruction,
    output_type=FriendlyMessage,
    output_guardrails=[friendly_message_validation_guardrail],
    model=model,
)

casual_chat_agent = Agent(
    name="CasualChatAgent",
    instructions=casual_chat_agent_instruction,
    output_type=FriendlyMessage,
    output_guardrails=[friendly_message_validation_guardrail],
    model=model,
)

main_agent = Agent(
    name="MainLegalAgent",
    instructions=main_agent_instruction,
    model=model,
    input_guardrails=[sensitive_input_guardrail],
    tools=[
        document_detector_agent.as_tool(
            tool_name="detect_document_type",
            tool_description="Check if input is a legal document or casual conversation.",
        ),
        analysis_agent.as_tool(
            tool_name="analyze_document_agent",
            tool_description="Analyze legal document with full validation.",
        ),
        friendly_agent.as_tool(
            tool_name="make_friendly",
            tool_description="Convert JSON analysis to friendly message.",
        ),
        casual_chat_agent.as_tool(
            tool_name="casual_chat",
            tool_description="Handle casual conversation and general questions.",
        ),
    ],
    output_type=FriendlyMessage,
    output_guardrails=[friendly_message_validation_guardrail],
)


async def main():
    print("🚀 Legal Agent System Starting...")
    print("=" * 50)

    config = RunConfig(tracing_disabled=True, model=model, model_provider=client)

    while True:
        user_input = input("\n👤 User: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        SimpleLogger.log("📥 INPUT", f"Received ({len(user_input)} chars)")

        try:
            context = SharedContext(document_text=user_input, analysis_stage="starting")

            print("\n🤖 Processing with Main Agent...")
            result = await Runner.run(
                main_agent, user_input, run_config=config, context=context
            )

            print(f"\n💬 Response: {result.final_output.message}")
        except InputGuardrailTripwireTriggered as e:
            SimpleLogger.log("🛑 INPUT GUARDRAIL TRIGGERED", str(e))
            print(f"Input blocked: {e.message}")
        except OutputGuardrailTripwireTriggered as e:
            SimpleLogger.log("🛑 OUTPUT GUARDRAIL TRIGGERED", str(e))
            print(f"Output validation failed: {e.message}")
        except Exception as e:
            SimpleLogger.log("❌ ERROR", str(e))
            print(f"Sorry, there was an error: {e}")

        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
