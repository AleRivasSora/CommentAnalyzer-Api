from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from typing import List, Dict

def analyze_sentiment(comments: List[str]) -> List[Dict[str, str]]:
    sid = SentimentIntensityAnalyzer()
    results = []

    for comment in comments:
        score = sid.polarity_scores(comment)
        sentiment = 'neutral'
        
        if score['compound'] >= 0.05:
            sentiment = 'positive'
        elif score['compound'] <= -0.05:
            sentiment = 'negative'
        
        results.append({
            'comment': comment,
            'sentiment': sentiment,
            'scores': score
        })
    
    return results