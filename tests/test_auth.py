from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

good_credentials = {
    'email': 'admin@swopyn.com',
    'password': '1234567890'
}


def test_user_can_obtain_auth_token():
    response = client.post('/authentication/login', json=good_credentials)
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert 'refresh_token' in response.json()
    assert 'type' in response.json()
