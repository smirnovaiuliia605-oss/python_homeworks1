import os

import requests
from dotenv import load_dotenv

base_url = "https://ru.yougile.com"

load_dotenv()
key = os.getenv('KEY')

my_headers = {
   "Authorization": f"Bearer {key}",
   "Content-Type": "application/json"
}


def test_create_project_positive():
    """создание проекта"""
    body = {"title": "Моя семья"}
    response = requests.post(f'{base_url}/api-v2/projects',
                             headers=my_headers, json=body)
    assert response.status_code == 201


def test_create_project_negative():
    """создание проекта"""
    body = {"title": ""}
    response = requests.post(f'{base_url}/api-v2/projects',
                             headers=my_headers, json=body)
    assert response.status_code == 400


def test_get_one_project_positive():
    """Получение проекта по ID"""
    body = {"title": "Доктор +"}
    response = requests.post(f'{base_url}/api-v2/projects',
                             headers=my_headers, json=body)

    project_id = response.json().get('id')
    assert project_id
    assert response.status_code == 201


def test_get_project_id_negative():
    """Получение проекта по ID"""
    Project_ID = "  "
    headers = {'Content-Type': 'application/json',
               'Authorization': "Bearer " + key}
    url = f"{base_url}/api-v2/projects/{Project_ID}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 404


def test_update_project_positive():
    """Изменение проекта"""
    data = {"title": "Автотест"}
    response = requests.post(f'{base_url}/api-v2/projects',
                             headers=my_headers, json=data)
    project_id = response.json()["id"]
    update_data = {"title": "Новое имя"}
    response_2 = requests.put(f'{base_url}/api-v2/projects/id',
                              headers=my_headers, json=data)
    assert response.status_code == 201
    assert response.json()["id"]

    """Удаление проекта"""
    update_data = {"deleted": True}
    response_2 = requests.put(f'{base_url}/api-v2/projects/id',
                              headers=my_headers, json=data)


def test_update_project_negative():
    """Изменение проекта"""
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    id = "999"
    update_data = {"title": "Новое имя"}
    response = requests.put(f'{base_url}/api-v2/projects/id',
                            headers=my_headers, json=update_data)
    assert response.status_code == 404
