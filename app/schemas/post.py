from pydantic import BaseModel
from typing import List


class PostAnalyzeRequest(BaseModel):
    text: str


class PostAnalyzeResponse(BaseModel):
    viral_score: int
    hook_score: int
    readability_score: int
    suggested_hashtags: List[str]
    improvement_tips: List[str]