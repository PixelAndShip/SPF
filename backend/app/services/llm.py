from openai import OpenAI

from app.config import OPENAI_API_KEY
from app.models.llm import LLMEvaluation
from app.models.paper import Paper


def evaluate_paper(
    paper: Paper,
    keywords: list[str],
) -> LLMEvaluation:
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
Evaluate how relevant this scientific paper is to the user's search.

User keywords:
{", ".join(keywords)}

Paper ID:
{paper.paper_id}

Paper title:
{paper.title}

Paper abstract:
{paper.abstract or "No abstract available."}

Give the paper a relevance score from 0 to 10.
10 means extremely relevant to the user's search.
0 means completely irrelevant.

Explain briefly why you gave this score.
"""

    response = client.responses.parse(
        model="gpt-5-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a scientific literature relevance evaluator. "
                    "Evaluate only the paper provided to you. "
                    "Do not invent information about the paper."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        text_format=LLMEvaluation,
    )

    return response.output_parsed


def mock_evaluate_paper(
    paper: Paper,
    keywords: list[str],
) -> LLMEvaluation:
    return LLMEvaluation(
        paper_id=paper.paper_id,
        relevance_score=8.0,
        explanation=(
            "Mock evaluation. The paper appears relevant to the provided keywords."
        ),
    )
