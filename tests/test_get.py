import requests
from jsonschema import validate

from schemas import get_user, get_list_users, get_color, get_list_colors


def test_get_list_users(base_url):
    endpoint = '/api/users'
    url = base_url + endpoint

    params = {'page': 2,
              'per_page': 3}

    response = requests.request(method='GET', url=url, params=params)
    body = response.json()

    assert response.status_code == 200
    assert 'data' in body
    assert len(body['data']) == params['per_page']
    assert 'support' in body
    assert body['support']['url'] == 'https://reqres.in/#support-heading'
    validate(body, schema=get_list_users)


def test_get_single_user(base_url):
    endpoint = '/api/users/'
    user_id = '5'
    url = base_url + endpoint + user_id

    response = requests.request(method='GET', url=url)
    body = response.json()

    assert response.status_code == 200
    assert 'data' in body
    assert body['data']['id'] == int(user_id)
    assert 'support' in body
    validate(body, schema=get_user)


def test_get_single_user_not_found(base_url):
    endpoint = '/api/users/'
    user_id = '25'
    url = base_url + endpoint + user_id

    response = requests.request(method='GET', url=url)

    assert response.status_code == 404


def test_get_list_colors(base_url):
    endpoint = '/api/unknown'
    url = base_url + endpoint

    params = {'page': 2,
              'per_page': 3}

    response = requests.request(method='GET', url=url, params=params)
    body = response.json()

    assert response.status_code == 200
    assert 'data' in body
    assert len(body['data']) == params['per_page']
    assert 'support' in body
    assert body['support']['text'] == (
        'To keep ReqRes free, contributions towards server costs are appreciated!')
    validate(body, schema=get_list_colors)


def test_get_single_color(base_url):
    endpoint = '/api/unknown/'
    user_id = '4'
    url = base_url + endpoint + user_id

    response = requests.request(method='GET', url=url)
    body = response.json()

    assert response.status_code == 200
    assert 'data' in body
    assert body['data']['id'] == int(user_id)
    assert 'support' in body
    assert body['support']['text'] == (
        'To keep ReqRes free, contributions towards server costs are appreciated!')
    validate(body, schema=get_color)

