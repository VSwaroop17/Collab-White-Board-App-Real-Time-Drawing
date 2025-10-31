from fastapi import FastAPI
from .auth import router as auth_router
from .signaling import router as signaling_router
from .db import connect_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Collaborative Whiteboard API")

origins = ["*"]  # For development. Restrict in production.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(signaling_router, prefix="/signaling")

@app.on_event("startup")
async def startup_db():
    connect_db()