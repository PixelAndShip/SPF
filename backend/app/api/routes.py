from app.models.search import SearchRequest
from app.services.search import search
from fastapi import APIRouter

router = APIRouter()


@router.post("/search")
def server_search_papers(request: SearchRequest):
    return search(request.keywords)
