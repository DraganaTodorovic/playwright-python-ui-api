from playwright.sync_api import sync_playwright
from utils import config_reader
from config import locators

BASE_URL = config_reader.readConfig("URLs","base_url")
USERNAME = config_reader.readConfig("credentials","standard_user")
PASSWORD = config_reader.readConfig("credentials","password")

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill(locators.LOGIN_USERNAME, USERNAME)
        page.fill(locators.LOGIN_PASSWORD, PASSWORD)
        page.click(locators.LOGIN_BUTTON)
        page.click(locators.ADD_TO_CART_BUTTON)
        assert "1" in page.locator(locators.CART_BADGE).inner_text()
        browser.close()
