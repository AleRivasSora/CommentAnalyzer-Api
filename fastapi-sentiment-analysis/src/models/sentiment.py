from pydantic import BaseModel
from typing import List, Dict

class SentimentResult(BaseModel):
    text: str
    sentiment: str
    score: float

class SentimentResponse(BaseModel):
    results: List[SentimentResult]