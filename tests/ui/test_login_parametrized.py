
import pytest
from playwright.sync_api import sync_playwright
from utils import data_reader, config_reader
from config import locators

BASE_URL = config_reader.readConfig("URLs","base_url")
expected_endpoint = locators.ENDPOINT_AFTER_LOGIN
json_data = data_reader.read_json("testdata/login_data.json")
csv_data = data_reader.read_csv("testdata/login_data.csv")

@pytest.mark.parametrize("data", json_data)
def test_login_parametrized_json(data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        username = data["username"]
        password = data["password"]
        page.fill(locators.LOGIN_USERNAME, username)
        page.fill(locators.LOGIN_PASSWORD, password)
        page.click(locators.LOGIN_BUTTON)
        if data["expected"] == "pass":
            assert expected_endpoint in page.url, f"Login failed for {username}"
        else:
            assert page.locator(locators.ERROR_MESSAGE).is_visible()
            error_inner_text = page.locator(locators.ERROR_MESSAGE).inner_text()
            assert locators.LOGIN_ERROR_MESSAGE_1 not in error_inner_text or locators.LOGIN_ERROR_MESSAGE_2 not in error_inner_text, f"Unexpected login success for {username}"
        browser.close()


# @pytest.mark.parametrize("username,password,expected", csv_data)
@pytest.mark.parametrize("data", csv_data)
def test_login_parametrized_csv(data):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        username = data["username"]
        password = data["password"]
        page.fill(locators.LOGIN_USERNAME, username)
        page.fill(locators.LOGIN_PASSWORD, password)
        page.click(locators.LOGIN_BUTTON)
        if data["expected"] == "pass":
            assert expected_endpoint in page.url, f"Login failed for {username}"
        else:
            assert page.locator(locators.ERROR_MESSAGE).is_visible()
            error_inner_text = page.locator(locators.ERROR_MESSAGE).inner_text()
            assert locators.LOGIN_ERROR_MESSAGE_1 not in error_inner_text or locators.LOGIN_ERROR_MESSAGE_2 not in error_inner_text, f"Unexpected login success for {username}"
        browser.close()
