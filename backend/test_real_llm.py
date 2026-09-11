from app.models.llm import LLMEvaluation
from app.models.paper import Paper
from app.services.llm import evaluate_paper


paper = Paper(
    paper_id="test-paper",
    title="The Evolution of Complex Life",
    abstract=(
        "This study examines how evolutionary processes contributed "
        "to the development of complex organisms."
    ),
)

result = evaluate_paper(
    paper,
    ["evolution", "biology"],
)

print("Paper ID:", result.paper_id)
print("Relevance:", result.relevance_score)
print("Explanation:", result.explanation)
