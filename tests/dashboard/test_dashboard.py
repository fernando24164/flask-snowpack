from unittest import TestCase

def test_dashboard(client):
    response = client.get('/')
    assert response.status_code == 200
