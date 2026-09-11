import type { Paper } from "../types";

export function createResultsContainer(): string {
    return `
        <div id="error"></div>
        <div id="results"></div>
    `;
}

export function renderPapers(papers: Paper[]): void {
    const results = document.querySelector<HTMLDivElement>("#results");

    if (!results) {
        return;
    }

    results.innerHTML = papers
        .map(paper => {
            const abstract = paper.abstract ?? "No abstract available.";

            const shortAbstract =
                abstract.length > 500
                    ? abstract.substring(0, 500) + "..."
                    : abstract;

            return `
                <article class="paper">
                    <h2>${paper.title}</h2>

                    <p class="paper-authors">
                        ${paper.authors.join(", ")}
                    </p>

                    <div class="paper-meta">
                        <span>
                            <strong>Year:</strong>
                            ${paper.year ?? "Unknown"}
                        </span>

                        <span>
                            <strong>Citations:</strong>
                            ${paper.citation_count}
                        </span>

                        <span>
                            <strong>Score:</strong>
                            ${paper.ranking_score.toFixed(2)}
                        </span>
                    </div>


                    <p class="paper-abstract">
                        ${shortAbstract}
                    </p>

                    ${paper.url
                    ? `
                                <a
                                    class="paper-link"
                                    href="${paper.url}"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    View paper →
                                </a>
                            `
                    : ""
                }
                </article>
            `;
        })
        .join("");
}