from pydantic import BaseModel


class LLMEvaluation(BaseModel):
    paper_id: str
    relevance_score: float
    explanation: str
