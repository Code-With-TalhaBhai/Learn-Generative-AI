from fastapi.testclient import TestClient
from main import app,get_db_session
import httpx



testing_db = ["DB for testing"]
def get_testing_db():
    return testing_db

app.dependency_overrides[get_db_session] = get_testing_db

client = TestClient(app)


def test_db_item():
    response = client.get(
        "/add-item?item=machine_learning"
    )

    assert response.status_code == 200
    assert response.json() == {"message": "added item machine_learning"}
