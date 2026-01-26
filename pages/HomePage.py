
from playwright.sync_api import Page
from config import locators


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = locators.MENU_BUTTON
        self.logout_link = locators.LOGOUT_LINK
        self.cart_badge = locators.CART_BADGE
        self.card_link = locators.CART_LINK
        self.add_to_card_button = locators.ADD_TO_CART_BUTTON
        self.remove_button = locators.REMOVE_BUTTON

    def click_menu_button(self):
        self.page.click(self.menu_button)

    def click_LogoutLink(self):
        self.page.click(self.logout_link)

    def click_shopping_cart(self):
        self.page.click(self.card_link)

    def is_cart_page(self, endpoint_name):
        return endpoint_name in self.page.url

    def click_add_to_cart(self):
        self.page.click(self.add_to_card_button)

    def click_remove_button(self):
        self.page.click(self.remove_button)

    def get_cart_badge_number(self):
        return self.page.locator(self.cart_badge).inner_text()

    def get_cart_badge_count(self):
        return self.page.locator(self.cart_badge).count()

    def is_visible_on_home_page(self, element_name):
        return self.page.locator(element_name).is_visible()

    def select_option_in_dropdown(self, element_name, option):
        self.page.select_option(element_name, option)

    def get_item_name(self, item_name):
        return self.page.locator(item_name).first.inner_text()

