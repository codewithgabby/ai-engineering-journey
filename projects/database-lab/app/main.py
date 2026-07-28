from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.models import Base

# Build every table defined in our models
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    with engine.connect() as connection:
        version = connection.execute(
            text("SELECT version();")
        ).scalar()

    return {
        "message": "Connected successfully!",
        "postgres_version": version,
    }