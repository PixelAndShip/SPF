import requests

from app.models.paper import Paper


BASE_URL = "https://api.openalex.org/works"


def reconstruct_abstract(inverted_index: dict) -> str:
    words = []

    for word, positions in inverted_index.items():
        for position in positions:
            words.append((position, word))

    words.sort()

    return " ".join(word for _, word in words)


def search_papers(query: str, limit: int = 10) -> list[Paper]:
    params = {
        "search": query,
        "per-page": limit,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    papers = []

    for item in data.get("results", []):
        authors = [
            author["author"]["display_name"]
            for author in item.get("authorships", [])
            if author.get("author", {}).get("display_name")
        ]

        pdf_url = None

        open_access = item.get("open_access") or {}
        best_oa_location = item.get("best_oa_location") or {}

        if best_oa_location.get("pdf_url"):
            pdf_url = best_oa_location["pdf_url"]

        paper = Paper(
            paper_id=item.get("id", ""),
            title=item.get("title", ""),
            abstract=reconstruct_abstract(
                item.get("abstract_inverted_index", {}) or {}
            ),
            authors=authors,
            year=item.get("publication_year"),
            citation_count=item.get("cited_by_count", 0),
            url=item.get("doi") or item.get("id"),
            pdf_url=pdf_url,
        )

        papers.append(paper)

    return papers
