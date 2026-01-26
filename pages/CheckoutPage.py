from playwright.sync_api import Page
from config import locators

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = locators.FIRST_NAME_INPUT
        self.last_name = locators.LAST_NAME_INPUT
        self.postal_code = locators.POSTAL_CODE_INPUT
        self.continue_button = locators.CONTINUE_BUTTON
        self.finish_button = locators.FINISH_BUTTON
        self.cancel_button = locators.CANCEL_BUTTON
        self.checkout_button = locators.CHECKOUT_BUTTON

        def click_checkout_button(self):
            self.page.click(self.checkout_button)

    def fill_checkout_information(self, firstName, lastName, postalCode):
        self.page.fill(self.first_name, firstName)
        self.page.fill(self.last_name, lastName)
        self.page.fill(self.postal_code, postalCode)
        self.page.click(self.continue_button)

    def get_page_inner_text(self, element_name):
        return self.page.inner_text(element_name)