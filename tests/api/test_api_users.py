
import requests
import pytest
from utils import config_reader, data_reader

API_BASE_URL = config_reader.readConfig("URLs","api_base_url")
API_Key = config_reader.readConfig("Headers","api_key")
CONTENT_Type = config_reader.readConfig("Headers","content_type")

headers = {}
headers["x-api-key"] = API_Key
headers["Content-Type"] = CONTENT_Type

payload_data = data_reader.read_json("testdata/api_create_user_data.json")

def test_get_user_by_id():
    end_point_api = API_BASE_URL + "/users/2"
    r = requests.get(end_point_api, headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["data"]["id"] == 2

@pytest.mark.parametrize("data", payload_data)
def test_create_user(data):
    payload = {"name": data["name"], "job": data["job"]}
    end_point_api = API_BASE_URL + "/users"
    r = requests.post(end_point_api, json=payload, headers=headers)
    assert r.status_code == 201
    response_data = r.json()
    assert response_data["name"] == payload["name"]
