from fastapi import FastAPI, HTTPException, 
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.limiter import limiter 
from slowapi.errors import RateLimiteExceeded
from slowapi.errors import _rate_limit_exceeded_handler
import uvicorn

app = FastAPI()

app.middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="", port=8000)