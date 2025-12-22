from fastapi import FastAPI
from app.routers.user_router import router as user_router

app = FastAPI(
    title="User API",
    description="API REST básica con FasAPI",
    version="1.0.0"
)

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {"status": "ok"}