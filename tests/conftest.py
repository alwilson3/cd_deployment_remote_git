import pytest
from app import app

@pytest.fixture
def web_client():
    app.config['TESTING'] = False
    with app.test_client() as client:
        yield client
