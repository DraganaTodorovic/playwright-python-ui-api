from playwright.sync_api import Page
from config import locators

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.remove_button = locators.REMOVE_BUTTON
        self.checkout_button = locators.CHECKOUT_BUTTON
        self.continue_shopping_button = locators.CONTINUE_SHOPPING_BUTTON
        self.cart_items = locators.CART_ITEMS

    # def get_cart_items(self):
    #     return self.cart_items

    def click_checkout_button(self):
        self.page.click(self.checkout_button)

    def click_remove_button(self):
        self.page.click(self.remove_button)

    def click_continue_shopping_button(self):
        self.page.click(self.continue_shopping_button)

    def get_page_inner_text(self, element_name):
        return self.page.inner_text(element_name)
