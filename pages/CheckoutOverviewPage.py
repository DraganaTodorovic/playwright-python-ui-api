from playwright.sync_api import Page
from config import locators

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = locators.FINISH_BUTTON
        self.cancel_button = locators.CANCEL_BUTTON
        self.back_home_button = locators.BACK_HOME_BUTTON

    def click_finish_button(self):
        self.page.click(self.finish_button)

    def click_cancel_button(self):
        self.page.click(self.cancel_button)

    def click_back_home_button(self):
        self.page.click(self.back_home_button)

    def get_page_inner_text(self, element_name):
        return self.page.inner_text(element_name)
