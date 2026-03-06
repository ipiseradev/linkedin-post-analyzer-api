from fastapi import FastAPI
from app.routers.posts import router as posts_router

app = FastAPI(title="PostPilot API")

app.include_router(posts_router)


@app.get("/")
def root():
    return {"message": "PostPilot API running"}