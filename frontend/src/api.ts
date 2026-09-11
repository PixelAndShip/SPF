import type { Paper } from "./types";

const API_URL = "http://localhost:8000";

export async function searchPapers(keywords: string[]): Promise<Paper[]> {
    const response = await fetch(`${API_URL}/search`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            keywords,
        }),
    });

    if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
    }

    return response.json();
}