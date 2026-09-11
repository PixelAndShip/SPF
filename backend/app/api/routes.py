from fastapi import APIRouter, HTTPException

from app.models.search import SearchRequest
from app.services.search import search

router = APIRouter()


@router.post("/search")
def server_search_papers(request: SearchRequest):
    try:
        return search(request.keywords)
    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error),
        )
