from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_get_items():
    response = client.get("/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item():
    response = client.get("/list-item?item_id=1")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] == 1


def test_create_item():
    response = client.post(
        "/add-item",
        json={"name": "Test Item", "description": "Description for Test Item"},
    )
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["name"] == "Test Item"


def test_update_item():
    response = client.patch(
        "/update-item/1",
        json={"name": "Updated Item", "description": "Updated Description"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"
    assert response.json()["description"] == "Updated Description"


def test_delete_item():
    response = client.delete("/delete-item/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted successfully"}
