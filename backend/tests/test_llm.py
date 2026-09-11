from unittest.mock import MagicMock, patch

from app.models.llm import LLMEvaluation
from app.models.paper import Paper
from app.services.llm import evaluate_paper


def test_llm_evaluation():
    evaluation = LLMEvaluation(
        paper_id="paper1",
        relevance_score=8.5,
        explanation="Highly relevant to the search.",
    )

    assert evaluation.paper_id == "paper1"
    assert evaluation.relevance_score == 8.5
    assert evaluation.explanation == "Highly relevant to the search."


@patch("app.services.llm.OpenAI")
def test_evaluate_paper(mock_openai):
    paper = Paper(
        paper_id="paper1",
        title="Evolution of Species",
        abstract="This paper studies biological evolution.",
    )

    mock_client = MagicMock()
    mock_openai.return_value = mock_client

    fake_response = MagicMock()

    fake_response.output_parsed = LLMEvaluation(
        paper_id="paper1",
        relevance_score=9.0,
        explanation="The paper directly discusses evolution.",
    )

    mock_client.responses.parse.return_value = fake_response

    result = evaluate_paper(
        paper,
        ["evolution"],
    )

    assert result.paper_id == "paper1"
    assert result.relevance_score == 9.0
    assert "evolution" in result.explanation
