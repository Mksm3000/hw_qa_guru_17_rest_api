import requests


def test_put_update(base_url):
    endpoint = '/api/users/'
    user_id = '2'
    url = base_url + endpoint + user_id

    params = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.request(method='PUT', url=url, json=params)
    body = response.json()

    assert response.status_code == 200
    assert 'name' in body
    assert body['name'] == params['name']
    assert 'job' in body
    assert body['job'] == params['job']
    assert 'updatedAt' in body


def test_patch_update(base_url):
    endpoint = '/api/users/'
    user_id = '2'
    url = base_url + endpoint + user_id

    params = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.request(method='PATCH', url=url, json=params)
    body = response.json()

    assert response.status_code == 200
    assert 'name' in body
    assert body['name'] == params['name']
    assert 'job' in body
    assert body['job'] == params['job']
    assert 'updatedAt' in body


def test_delete(base_url):
    endpoint = '/api/users/'
    user_id = '2'
    url = base_url + endpoint + user_id

    response = requests.request(method='DELETE', url=url)

    assert response.status_code == 204
