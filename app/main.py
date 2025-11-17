from fastapi import FastAPI

from app.router import get_router, post_router, put_router, patch_router, delete_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, This is a FastAPI Core project!"}

app.include_router(get_router.router, prefix="/api", tags=["Get Router"])

app.include_router(post_router.router, prefix="/api", tags=["Post Router"])

app.include_router(put_router.router, prefix="/api", tags=["Put Router"])

app.include_router(patch_router.router, prefix="/api", tags=["Patch Router"])

app.include_router(delete_router.router, prefix="/api", tags=["Delete Router"])
