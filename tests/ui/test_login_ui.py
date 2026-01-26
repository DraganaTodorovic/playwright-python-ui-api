
from utils import config_reader
from playwright.sync_api import sync_playwright
from config import locators

BASE_URL = config_reader.readConfig("URLs","base_url")
expected_endpoint = locators.ENDPOINT_AFTER_LOGIN
USERNAME = config_reader.readConfig("credentials","standard_user")
PASSWORD = config_reader.readConfig("credentials","password")

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill(locators.LOGIN_USERNAME, USERNAME)
        page.fill(locators.LOGIN_PASSWORD, PASSWORD)
        page.click(locators.LOGIN_BUTTON)
        assert expected_endpoint in page.url, f"Login failed for {USERNAME}"
        browser.close()
