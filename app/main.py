from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI("Recipe API")

@app.get("/")
def read_root():
    return {"status":"ok"}

"""
example from FASTAPI documentation

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q":q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

"""