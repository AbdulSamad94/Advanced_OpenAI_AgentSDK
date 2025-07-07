from agents import Agent, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agent_instructions import (
    summarizer_agent_instruction,
    risk_detector_agent_instruction,
    clause_checker_agent_instruction,
)
from pydantic import BaseModel


class SummaryOutput(BaseModel):
    summary: str


class RiskOutput(BaseModel):
    risks: list[str]


class FriendlyMessage(BaseModel):
    message: str


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.0-flash")

SummarizerAgent = Agent(
    name="SummarizerAgent",
    instructions=summarizer_agent_instruction,
    output_type=SummaryOutput,
    model=model,
)

RiskDetectorAgent = Agent(
    name="RiskDetectorAgent",
    instructions=risk_detector_agent_instruction,
    output_type=RiskOutput,
    model=model,
)

ClauseCheckerAgent = Agent(
    name="Clause Checker Agent",
    instructions=clause_checker_agent_instruction,
    output_type=str,
    model=model,
)


@function_tool
def fallback_response(user_input: str) -> FriendlyMessage:
    """Respond when the input is not a legal document."""
    return FriendlyMessage(
        message="Hi there! I specialize in reviewing legal clauses. Please paste your contract or clause."
    )
