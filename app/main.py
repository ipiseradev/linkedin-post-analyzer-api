from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.posts import router as posts_router

app = FastAPI(
    title="PostPilot API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts_router)


@app.get("/")
def root():
    return {"message": "PostPilot API running"}