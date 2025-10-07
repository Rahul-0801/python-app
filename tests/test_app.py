import pytest
from app import app  # Import your Flask app instance


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.status_code == 200
    # You might want to add more specific assertions about the content
    # For example, check if a specific string is present in the response data:
    # assert b"Hello, World!" in response.data


def test_about_page(client):
    """Test the about page route."""
    response = client.get('/about')
    assert response.status_code == 200
    # Add more specific assertions about the content if needed


if __name__ == '__main__':
    pytest.main()