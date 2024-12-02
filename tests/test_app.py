import sys
import os
import pytest

# Voeg de root van je project toe aan sys.path zodat pytest de app kan vinden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # Gebruik create_app in plaats van rechtstreeks app importeren

@pytest.fixture(scope="module")
def client():
    # Zorg ervoor dat de Flask-app wordt geïnitialiseerd
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_add_route(client):
    response = client.get('/add/3/4')
    assert response.status_code == 200
    assert response.json == {"result": 7}
