from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_id():
    response = client.get("/pet_id")
    assert response.status_code == 200
    assert response.json() == {"name": "waldi", "version": 0.1}


def test_read_mood():
    response = client.get("/mood")
    assert response.status_code == 200
    assert response.json() == {"angry"}


def test_managa_mood():

    # send appropriate pet care action for initial mood "angry"
    response = client.post("/manage_mood", json={"action": "CALM"})
    assert response.status_code == 200
    assert response.json() == 0

    # assert that the pet endpoint has changed mood according to mood model
    response = client.get("/mood")
    assert response.status_code == 200
    assert response.json() == {"lonley"}

    # assert error code for pet care action that does not comply with the mood model
    response = client.post("/manage_mood", json={"action": "FEED"})
    assert response.status_code == 200
    assert response.json() == 1

    # assert that the pet endpoint has not changed mood
    response = client.get("/mood")
    assert response.status_code == 200
    assert response.json() == {"lonley"}