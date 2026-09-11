import re
from datetime import datetime

from app.models.paper import Paper


def contains_keyword(text: str, keyword: str) -> bool:
    pattern = rf"\b{re.escape(keyword.lower())}\b"

    return re.search(pattern, text.lower()) is not None


def calculate_relevance(paper: Paper, keywords: list[str]) -> float:
    score = 0.0

    title = paper.title
    abstract = paper.abstract or ""

    for keyword in keywords:
        if contains_keyword(title, keyword):
            score += 3.0

        if contains_keyword(abstract, keyword):
            score += 1.0

    return score


def calculate_citation_score(paper: Paper) -> float:
    return min(paper.citation_count / 1000, 1.0)


def calculate_recency_score(paper: Paper) -> float:
    if paper.year is None:
        return 0.0

    current_year = datetime.now().year
    age = current_year - paper.year

    return max(0.0, 1.0 - age / 50)


def calculate_score(paper: Paper, keywords: list[str]) -> float:
    relevance = calculate_relevance(paper, keywords)
    citations = calculate_citation_score(paper)
    recency = calculate_recency_score(paper)

    return relevance * 0.70 + citations * 2.0 + recency * 1.0


def rank_papers(papers: list[Paper], keywords: list[str]) -> list[Paper]:
    for paper in papers:
        paper.ranking_score = calculate_score(paper, keywords)

    return sorted(
        papers,
        key=lambda paper: paper.ranking_score,
        reverse=True,
    )


def select_candidates(
    papers: list[Paper],
    count: int = 3,
) -> list[Paper]:
    return papers[:count]
