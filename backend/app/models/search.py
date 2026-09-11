from pydantic import BaseModel


class SearchRequest(BaseModel):
    keywords: list[str]
