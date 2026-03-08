from fastapi import FastAPI
from app.routers.posts import router as posts_router

app = FastAPI(
    title="PostPilot API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(posts_router)


@app.get("/")
def root():
    return {"message": "PostPilot API running"}


@app.get("/routes")
def list_routes():
    return [route.path for route in app.routes]