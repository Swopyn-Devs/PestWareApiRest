from fastapi.testclient import TestClient

from main import app
from decouple import config

client = TestClient(app)

fake_country = {
    "name": "México",
    "code_country": "52",
    "coin_country": "mxn",
    "symbol_country": "$"
}

good_authorization = {
    'Authorization': f"Bearer {config('TESTS_TOKEN')}"
}


def test_read_countries():
    response = client.get('/catalogs/countries')
    assert response.status_code == 200


def test_read_item():
    response = client.get('/catalogs/countries/442aa873-00a3-495c-93eb-5ae3558ecaf1', headers=good_authorization)
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'name' in response.json()
    assert 'code_country' in response.json()
    assert 'coin_country' in response.json()
    assert 'symbol_country' in response.json()


def test_create_country():
    response = client.post('/catalogs/countries', json=fake_country, headers=good_authorization)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert 'name' in response.json()
    assert 'code_country' in response.json()
    assert 'coin_country' in response.json()
    assert 'symbol_country' in response.json()
