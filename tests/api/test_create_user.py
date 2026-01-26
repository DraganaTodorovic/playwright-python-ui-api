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
# ids = []

@pytest.mark.parametrize("data", payload_data)
def test_create_user(data):
    payload = {"name": data["name"], "job": data["job"]}
    end_point_api = API_BASE_URL + "/users"
    r = requests.post(end_point_api, json=payload, headers=headers)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data
    # ids.append(data["id"])
    # end_point_api = API_BASE_URL + "/users/" + id
    end_point_api = API_BASE_URL + "/users/" + data["id"]
    r = requests.delete(end_point_api, headers=headers)

    assert r.status_code == 204


# @pytest.mark.parametrize("id", ['917', '714', '291', '398'])
# def test_delete_user(id):
#     print(id)
#     # ids.append(id)
#     # print(ids)
#     end_point_api = API_BASE_URL + "/users/" + id
#     r = requests.delete(end_point_api, headers=headers)
#
#     assert r.status_code == 204


