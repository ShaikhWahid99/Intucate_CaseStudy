from fastapi import FastAPI
from app.routes.chat import router
from app.db.database import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB test endpoint
@app.get("/")
async def home():

    return {"message": "Database connected"}


app.include_router(router)
