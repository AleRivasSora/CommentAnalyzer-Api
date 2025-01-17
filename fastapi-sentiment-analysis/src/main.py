from fastapi import FastAPI
from routers.sentiment import router as sentiment_router

app = FastAPI()

app.include_router(sentiment_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)