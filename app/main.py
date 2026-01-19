from fastapi import FastAPI
from pydantic import BaseModel
from app.routes import recipes

app = FastAPI(title="Recipe API")
app.include_router(recipes.router)


@app.get("/")
def read_root():
    return {"status":"ok"}

