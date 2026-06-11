from typing import Dict
from .models import Item

# Simple in-memory store (safe for single-process dev)
class DataStore:
    def __init__(self):
        self._items: Dict[int, Item] = {}
        self._next_id = 1

    def list(self, skip: int = 0, limit: int = 100):
        items = list(self._items.values())
        return items[skip : skip + limit]

    def get(self, item_id: int):
        return self._items.get(item_id)

    def create(self, item_create):
        item = Item(id=self._next_id, **item_create.dict())
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def update(self, item_id: int, item_update):
        existing = self._items.get(item_id)
        if not existing:
            return None
        updated = existing.copy(update=item_update.dict(exclude_unset=True))
        self._items[item_id] = updated
        return updated

    def delete(self, item_id: int):
        return self._items.pop(item_id, None)

store = DataStore()
