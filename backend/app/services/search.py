from app.models.paper import Paper
from app.services.llm import mock_evaluate_paper, evaluate_paper
from app.services.openalex import search_papers
from app.services.ranking import rank_papers, select_candidates


def search(keywords: list[str]) -> list[Paper]:
    query = " ".join(keywords)

    papers = search_papers(query)

    ranked_papers = rank_papers(papers, keywords)

    candidates = select_candidates(ranked_papers)

    for paper in candidates:
        evaluation = mock_evaluate_paper(paper, keywords)

        paper.llm_score = evaluation.relevance_score
        paper.llm_explanation = evaluation.explanation

    return candidates
