# FastAPI Sentiment Analysis

This project is a FastAPI application that utilizes the NLTK sentiment analysis library and Pandas to analyze the sentiment of a list of comments or texts. The application classifies the sentiments as positive, negative, or neutral and returns the results in JSON format.

## Project Structure

```
fastapi-sentiment-analysis
├── src
│   ├── main.py               # Entry point of the FastAPI application
│   ├── models
│   │   └── sentiment.py      # Data model for sentiment analysis results
│   ├── routers
│   │   └── sentiment.py      # API router for handling sentiment analysis requests
│   └── services
│       └── sentiment_analysis.py # Logic for analyzing sentiment using NLTK and Pandas
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-sentiment-analysis
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

## Usage

To analyze the sentiment of comments, send a POST request to the `/analyze` endpoint with a JSON body containing a list of texts. For example:

```json
{
  "comments": [
    "I love this product!",
    "This is the worst experience I've ever had.",
    "It's okay, not great but not bad."
  ]
}
```

The response will include the sentiment classification for each comment:

```json
{
  "results": [
    {"text": "I love this product!", "sentiment": "positive"},
    {"text": "This is the worst experience I've ever had.", "sentiment": "negative"},
    {"text": "It's okay, not great but not bad.", "sentiment": "neutral"}
  ]
}
```

## License

This project is licensed under the MIT License.