import "./styles/style.css"
import { createSearchBar } from "./components/SearchBar";
import {
    createResultsContainer,
    renderPapers
} from "./components/Results";
import { searchPapers } from "./api";

const app = document.querySelector<HTMLDivElement>("#app");

if (app) {
    app.innerHTML = `
        <h1>Science Paper Filter</h1>

        ${createSearchBar()}

        ${createResultsContainer()}
    `;

    const searchInput =
        document.querySelector<HTMLInputElement>("#searchInput");

    const searchButton =
        document.querySelector<HTMLButtonElement>("#searchButton");

    if (searchInput && searchButton) {
        searchButton.addEventListener("click", async () => {
            const keywords = searchInput.value
                .split(",")
                .map(keyword => keyword.trim())
                .filter(keyword => keyword.length > 0);

            if (keywords.length === 0) {
                return;
            }

            try {
                const papers = await searchPapers(keywords);

                renderPapers(papers);
            } catch (error) {
                console.error("Search failed:", error);

                const errorContainer =
                    document.querySelector<HTMLDivElement>("#error");

                if (errorContainer) {
                    errorContainer.textContent =
                        "The paper database is temporarily unavailable. Please try again later.";
                }
            }
        });
    }
}