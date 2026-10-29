
from fastapi import FastAPI

from app.routers.products import router as products_router
from app.routers.users import router as users_router

app = FastAPI(title="Production SaaS Backend")

app.include_router(products_router)
app.include_router(users_router)


@app.get("/")
def health_check():
    return {"status": "ok"}
