from playwright.sync_api import sync_playwright
from utils import config_reader
from config import locators

BASE_URL = config_reader.readConfig("URLs","base_url")
USERNAME = config_reader.readConfig("credentials","standard_user")
PASSWORD = config_reader.readConfig("credentials","password")

def test_inventory_filters():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        page.fill(locators.LOGIN_USERNAME, USERNAME)
        page.fill(locators.LOGIN_PASSWORD, PASSWORD)
        page.click(locators.LOGIN_BUTTON)
        page.select_option(locators.SORT_DROPDOWN, locators.SORT_DROPDOWN_OPTION_2)
        first_item = page.locator(locators.FIRST_ITEM_NAME).first.inner_text()
        assert first_item is not None
        browser.close()
