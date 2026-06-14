from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import os

from backend.app.api.chat import router as chat_router
from backend.app.api.upload import router as upload_router
from backend.app.services.preload_service import PreloadService


os.makedirs("uploads", exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):

    preload_service = PreloadService()
    preload_service.preload_documents()

    yield


app = FastAPI(
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(upload_router)


@app.get("/")
def home():

    return FileResponse(
        "frontend/index.html"
    )