export interface Paper {
    paper_id: string;
    title: string;
    abstract: string | null;
    authors: string[];
    year: number | null;
    citation_count: number;
    url: string | null;
    pdf_url: string | null;
    ranking_score: number;
    llm_score: number | null;
    llm_explanation: string | null;
}