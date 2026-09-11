from pydantic import BaseModel


class Paper(BaseModel):
    paper_id: str
    title: str
    abstract: str | None = None
    authors: list[str] = []
    year: int | None = None
    citation_count: int = 0
    url: str | None = None
    pdf_url: str | None = None
    ranking_score: float = 0.0
    llm_score: float | None = None
    llm_explanation: str | None = None
