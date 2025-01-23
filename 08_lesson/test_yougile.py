import pytest
import requests

url = "https://ru.yougile.com/api-v2/projects"
headers = {
        "Content-Type": "application/json",
        "Authorization":
        "Bearer rbveLxvMmzT9C1oCcBZq74+Cg9a9neHH1ont6of6ksiQdChkPBBXVpFmc6RMQP7n"
        }
# получение списка проектов


def test_get_list_aut():
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200

# получение списка проектов без авторизации


def test_get_list():
    response = requests.request("GET", url)
    assert response.status_code == 401

# создание проекта


def test_create_a_project():
    payload = {
        "title": "My_company"
        }

    response = requests.request("POST", url, json=payload, headers=headers)
    assert response.status_code == 201


@pytest.fixture(scope="module")
def project_id():
    payload = {
        "title": "My_company"
        }
    response = requests.request("POST", url, json=payload, headers=headers)
    assert response.status_code == 201
    return response.json().get('id')


# создание проекта без названия


def test_create_a_project_1():
    payload = {
        "title": ""
        }

    response = requests.request("POST", url, json=payload, headers=headers)
    assert response.status_code == 400

# получение проекта по id


def test_get_project(project_id):
    response = requests.request("GET", f"{url}/{project_id}", headers=headers)
    assert response.status_code == 200

# внесение изменений в проект


def test_put_project(project_id):
    payload = {
        "deleted": False,
        "title": "My_comany_2"
        }

    response = requests.request("PUT", f"{url}/{project_id}", json=payload,
                                headers=headers)
    assert response.status_code == 200
