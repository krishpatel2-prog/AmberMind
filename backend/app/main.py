from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from backend.app.api.chat import router as chat_router
from backend.app.api.upload import router as upload_router

os.makedirs("uploads", exist_ok=True)
os.makedirs("chroma_db", exist_ok=True)
app = FastAPI()

# Allow CORS so the static frontend can call the API during local development.
# Adjust `allow_origins` to your deployment origins as needed.
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