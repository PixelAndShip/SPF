export function createSearchBar(): string {
    return `
        <input
            id="searchInput"
            type="text"
            placeholder="Enter keywords..."
        />

        <button id="searchButton">
            Search
        </button>
    `;
}