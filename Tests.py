import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(BASE_URL, json=new_post)
    assert response.status_code == 201
    assert 'id' in response.json()

def test_change_post():
    change_post = {
        "id":1,
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/1", json=change_post)
    assert response.status_code in [200, 204]
    assert response.json().get('id') == 1

def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code in [200, 204]