import requests
from utils import config_reader

API_BASE_URL = config_reader.readConfig("URLs","api_base_url")
API_Key = config_reader.readConfig("Headers","api_key")
CONTENT_Type = config_reader.readConfig("Headers","content_type")

headers = {}
headers["x-api-key"] = API_Key
headers["Content-Type"] = CONTENT_Type

def test_update_user():
    payload = {"name": "Jane Doe", "job": "Dev"}
    # payload = {"name": data["name"], "job": data["job"]}
    end_point_api = API_BASE_URL + "/users/2"
    r = requests.put(end_point_api, json=payload, headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == payload["name"]
