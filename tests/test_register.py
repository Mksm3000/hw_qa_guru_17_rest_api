import requests
from jsonschema import validate

from schemas import post_register_user


def test_post_register_successful(base_url):
    endpoint = '/api/register'
    url = base_url + endpoint

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.request(method='POST', url=url, data=payload)
    body = response.json()

    assert response.status_code == 200
    assert 'token' in body
    assert body['token'] == 'QpwL5tke4Pnpja7X4'
    assert body['id'] == 4
    validate(body, schema=post_register_user)


def test_post_register_unsuccessful(base_url):
    endpoint = '/api/register'
    url = base_url + endpoint

    payload = {
        "email": "sydney@fife"
    }

    response = requests.request(method='POST', url=url, data=payload)
    body = response.json()

    assert response.status_code == 400
    assert 'error' in body
    assert body['error'] == 'Missing password'
