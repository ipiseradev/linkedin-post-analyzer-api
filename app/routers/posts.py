from fastapi import APIRouter
from app.schemas.post import PostAnalyzeRequest, PostAnalyzeResponse
from app.services.analyzer import analyze_post_text

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/analyze", response_model=PostAnalyzeResponse)
def analyze_post(payload: PostAnalyzeRequest):
    return analyze_post_text(payload.text)