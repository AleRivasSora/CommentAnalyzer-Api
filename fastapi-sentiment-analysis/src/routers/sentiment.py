from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.services.sentiment_analysis import analyze_sentiment

router = APIRouter()

class CommentRequest(BaseModel):
    comments: List[str]

class SentimentResponse(BaseModel):
    comment: str
    sentiment: str

@router.post("/analyze", response_model=List[SentimentResponse])
async def analyze_comments(request: CommentRequest):
    if not request.comments:
        raise HTTPException(status_code=400, detail="No comments provided")
    
    results = analyze_sentiment(request.comments)
    return results