from fastapi.testclient import TestClient
from starter.main import app

client = TestClient(app)

def test_create_get_delete_cycle():
    # create
    r = client.post("/items", json={"name": "A", "price": 9.99})
    assert r.status_code == 201
    created = r.json()
    item_id = created["id"]

    # get
    r = client.get(f"/items/{item_id}")
    assert r.status_code == 200
    assert r.json()["name"] == "A"

    # delete
    r = client.delete(f"/items/{item_id}")
    assert r.status_code == 204

    # get after delete
    r = client.get(f"/items/{item_id}")
    assert r.status_code == 404

def test_list_and_pagination():
    # ensure listing works and limit/skip query params accepted
    client.post("/items", json={"name": "Item1", "price": 1.0})
    client.post("/items", json={"name": "Item2", "price": 2.0})
    r = client.get("/items?limit=1")
    assert r.status_code == 200
    assert len(r.json()) <= 1
