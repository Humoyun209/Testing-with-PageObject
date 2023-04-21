import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators, BasketPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        self.browser.implicitly_wait(5)
        bask_btn = self.browser.find_element(*(MainPageLocators.BASKET_BTN))
        bask_btn.click()
        text = self.browser.find_elements(*(BasketPageLocators.EMPTY_TEXT))
        assert bool(text), 'Корзина не пусто'
