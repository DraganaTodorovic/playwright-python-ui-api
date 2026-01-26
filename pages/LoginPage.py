
from playwright.sync_api import Page
from config import locators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = locators.LOGIN_USERNAME
        self.password = locators.LOGIN_PASSWORD
        self.login_button = locators.LOGIN_BUTTON
        self.error_msg = locators.ERROR_MESSAGE
        self.app_logo = locators.APP_LOGO_TITLE

    def navigate(self, url):
        self.page.goto(url)

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_button)

    def is_logged_in(self, endpoint_name):
        return endpoint_name in self.page.url

    def get_error_text(self):
        return self.page.locator(self.error_msg).inner_text()

    def get_app_logo_name(self):
        return self.page.locator(self.app_logo).inner_text()
