from app import app

def test_index():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_status():
    tester = app.test_client()
    response = tester.get("/status")
    assert response.status_code == 200
    assert b'"status": "ok"' in response.data
