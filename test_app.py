from app import app


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Information System" in response.data


def test_courses():
    client = app.test_client()
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.get_json()
    assert "courses" in data
    assert len(data["courses"]) == 3


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
