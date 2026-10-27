import os
import uuid
import pytest
from project_api import ProjectApi

token = # Подставить свой токен
BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN", token)

@pytest.fixture
def api():
    return ProjectApi(BASE_URL, TOKEN)

@pytest.fixture
def project_id(api):
    resp = api.create({"title": f"autotest {uuid.uuid4()}"})
    assert resp.status_code == 201
    proj_id = resp.json()["id"]
    yield proj_id
    api.update(proj_id, {"deleted": True})

def test_post_positive(api):
    title = f"autotest {uuid.uuid4()}"
    resp = api.create({"title": title})
    assert resp.status_code == 201
    proj_id = resp.json()["id"]
    assert api.get(proj_id).json()["title"] == title
    api.update(proj_id, {"deleted": True})

def test_post_negative(api):
    resp = api.create({"title": ""})
    assert resp. status_code == 400

def test_update_positive(api, project_id):
    resp = api.update(project_id, {"title": "new name"})
    assert resp.status_code == 200
    assert api.get(project_id).json()["title"] == "new name"

def test_update_negative(api):
    resp = api.update(str(uuid.uuid4()), {"title": "new name"})
    assert resp.status_code == 404

def test_get_positive(api, project_id):
    resp = api.get(project_id)
    assert resp.status_code == 200
    assert resp.json()["id"] == project_id

def test_get_negative(api):
    resp = api.get(str(uuid.uuid4()))
    assert resp.status_code == 404
