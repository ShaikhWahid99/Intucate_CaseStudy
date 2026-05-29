from fastapi import FastAPI

from app.routes.chat import router

from app.db.database import db

app = FastAPI()

@app.get("/")
async def home():

    return {
        "message": "Database connected"
    }

app.include_router(router)
