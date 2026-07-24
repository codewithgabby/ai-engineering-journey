from fastapi import FastAPI
from app.database import engine

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Database Lab",
        "engine": str(engine)
    }