from fastapi import FastAPI

from app.router import get_router, post_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, This is a FastAPI Core project!"}

app.include_router(get_router.router, prefix="/api", tags=["Get Router"])
app.include_router(post_router.router, prefix="/api", tags=["Post Router"])
