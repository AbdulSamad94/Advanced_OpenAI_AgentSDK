from pydantic import BaseModel


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


class SharedContext(BaseModel):
    document_text: str
    analysis_stage: str = "starting"
    previous_outputs: dict = {}


class DocumentCheckOutput(BaseModel):
    is_legal_document: bool
    document_type: str
    reasoning: str
