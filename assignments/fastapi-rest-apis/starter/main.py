from fastapi import FastAPI, HTTPException, status, Query, Path
from typing import List
from .models import Item, ItemCreate
from .data_store import store

app = FastAPI(title="Items API", version="0.1.0")

@app.get("/items", response_model=List[Item])
def list_items(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=1000)):
    return store.list(skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int = Path(..., ge=1)):
    item = store.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    item = store.create(payload)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int = Path(..., ge=1), payload: ItemCreate = None):
    updated = store.update(item_id, payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return updated

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int = Path(..., ge=1)):
    deleted = store.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return None
