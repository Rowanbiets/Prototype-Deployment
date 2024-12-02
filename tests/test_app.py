import pytest
import requests
import subprocess
import time

@pytest.fixture(scope="module", autouse=True)
def flask_server():
    # Start de Flask-server
    server = subprocess.Popen(["flask", "run", "--port=5000"], env={"FLASK_APP": "app.py"})
    time.sleep(3)  # Wacht tot de server actief is
    yield
    server.terminate()  # Stop de server na de tests

def test_health_check():
    response = requests.get("http://127.0.0.1:5000/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_add_route():
    response = requests.get("http://127.0.0.1:5000/add/3/4")
    assert response.status_code == 200
    assert response.json() == {"result": 7}
