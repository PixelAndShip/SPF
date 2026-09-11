from app.models.paper import Paper
from app.services.ranking import (
    calculate_relevance,
    calculate_score,
    contains_keyword,
    rank_papers,
    select_candidates,
)


def test_select_candidates():
    papers = [
        Paper(paper_id="1", title="Paper 1"),
        Paper(paper_id="2", title="Paper 2"),
        Paper(paper_id="3", title="Paper 3"),
        Paper(paper_id="4", title="Paper 4"),
        Paper(paper_id="5", title="Paper 5"),
    ]

    candidates = select_candidates(papers, 3)

    assert len(candidates) == 3
    assert candidates[0].paper_id == "1"
    assert candidates[1].paper_id == "2"
    assert candidates[2].paper_id == "3"


def test_contains_keyword():
    assert contains_keyword("IT is important", "IT")
    assert not contains_keyword("This is important", "IT")


def test_title_keyword_is_more_relevant():
    paper = Paper(
        paper_id="1",
        title="Evolution of Species",
        abstract="A study about biology.",
    )

    score = calculate_relevance(paper, ["evolution"])

    assert score == 3.0


def test_abstract_keyword_is_relevant():
    paper = Paper(
        paper_id="1",
        title="A Biology Study",
        abstract="This paper studies evolution.",
    )

    score = calculate_relevance(paper, ["evolution"])

    assert score == 1.0


def test_title_and_abstract_both_count():
    paper = Paper(
        paper_id="1",
        title="Evolution of Species",
        abstract="This paper studies evolution.",
    )

    score = calculate_relevance(paper, ["evolution"])

    assert score == 4.0


def test_citations_affect_score():
    low_citation = Paper(
        paper_id="1",
        title="Evolution",
        citation_count=0,
    )

    high_citation = Paper(
        paper_id="2",
        title="Evolution",
        citation_count=1000,
    )

    low_score = calculate_score(low_citation, ["evolution"])
    high_score = calculate_score(high_citation, ["evolution"])

    assert high_score > low_score


def test_rank_papers():
    paper1 = Paper(
        paper_id="1",
        title="Evolution",
        citation_count=10,
    )

    paper2 = Paper(
        paper_id="2",
        title="Completely Different Topic",
        citation_count=1000,
    )

    ranked = rank_papers(
        [paper2, paper1],
        ["evolution"],
    )

    assert ranked[0].paper_id == "1"
    assert ranked[1].paper_id == "2"
