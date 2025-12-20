from fastapi import FastAPI

app = FastAPI(
    title="User API",
    description="API REST básica con FasAPI",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "ok"}