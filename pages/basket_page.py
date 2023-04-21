from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        empty = self.browser.find_element(*BasketPageLocators.EMPTY_TEXT)
        assert bool(empty.text), 'Корзина не пусто'