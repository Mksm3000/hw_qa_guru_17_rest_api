import requests
from jsonschema import validate
from datetime import datetime, timezone
from schemas import post_login_user, post_create_user


def test_post_login_successful(base_url):
    endpoint = '/api/login'
    url = base_url + endpoint

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.request(method='POST', url=url, data=payload)
    body = response.json()

    assert response.status_code == 200
    assert 'token' in body
    assert body['token'] == 'QpwL5tke4Pnpja7X4'
    validate(body, schema=post_login_user)


def test_post_login_unsuccessful(base_url):
    endpoint = '/api/login'
    url = base_url + endpoint

    payload = {
        "email": "peter@klaven"
    }

    response = requests.request(method='POST', url=url, data=payload)
    body = response.json()

    assert response.status_code == 400
    assert 'error' in body
    assert body['error'] == 'Missing password'


def test_post_create(base_url):
    current_time = datetime.now(timezone.utc)
    endpoint = '/api/users'
    url = base_url + endpoint

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.request(method='POST', url=url, data=payload)
    body = response.json()

    assert response.status_code == 201
    assert 'name' in body
    assert body['name'] == 'morpheus'
    assert 'job' in body
    assert body['job'] == 'leader'
    validate(body, schema=post_create_user)
