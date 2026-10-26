import requests

base_url = "https://ru.yougile.com/api-v2"
token = ""
company_id = "cad634d1-004f-4554-a3ea-c39cd3c41cee"
user_id = "9dc05539-9655-49c2-b1a6-edfb0d3325d0"

# Позитивная проверка метода post
def test_post_1():
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    project_data = {
        'title': 'positive test',
        'users': {"9dc05539-9655-49c2-b1a6-edfb0d3325d0": "worker"},
        'idempotencyKey': '7183557e-3d71-417b-9e33-fd7622299cb9'
    }

    response = requests.post(base_url+'/projects', headers=headers, json=project_data)
    
    assert response.status_code == 201
    

# Неагивная проверка метода post
def test_post_2():
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    project_data = {
        'title': '',
        'users': {"9dc05539-9655-49c2-b1a6-edfb0d3325d0": "worker"},
        'idempotencyKey': '7183557e-3d71-417b-9e33-fd7622299cb9'
    }

    response = requests.post(base_url+'/projects', headers=headers, json=project_data)
    assert response.status_code == 400

# Позитивная проверка метода put
def test_put_1():
    payload = {
        'deletaed': True,
        'title': 'change name',
        'users': {"9dc05539-9655-49c2-b1a6-edfb0d3325d0": "worker"}
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.put(base_url+'/projects'+company_id, headers=headers, json=payload)
    assert response.status_code == 201
