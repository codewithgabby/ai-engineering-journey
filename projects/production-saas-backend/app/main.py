from fastapi import FastAPI

app = FastAPI(
    title="Production SaaS Backend",
)

@app.get("/")
def health_check():
    return {"status": "ok"}