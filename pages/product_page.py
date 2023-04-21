import math

from selenium.common.exceptions import NoAlertPresentException

from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.implicitly_wait(5)
        add_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_btn.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        res = str(math.log(abs(12 * math.sin(int(x)))))
        alert.send_keys(res)
        alert.accept()
        try:
            alert_for_stepik = self.browser.switch_to.alert
            print(alert_for_stepik.text)
            alert_for_stepik.accept()
        except NoAlertPresentException:
            print("Alert didn't find")

    def comparison_price_and_name(self):
        self.browser.implicitly_wait(5)
        pr_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        pr_name_in_alert = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT).text

        pr_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_IN_ALERT).text
        assert pr_name == pr_name_in_alert, 'Имени не совпали'
        assert pr_price == price_basket, 'Цены не совпали'

    def should_not_be_success_message(self):
        assert self.is_element_not_present(*ProductPageLocators.MESSAGE_SHOPPING)

    def should_be_skip_success_message(self):
        assert self.is_element_not_present(*ProductPageLocators.MESSAGE_SHOPPING)

    def should_be_has_message(self):
        msg = self.browser.find_elements(*ProductPageLocators.MESSAGE_SHOPPING)
        assert bool(msg), 'Сообщение не найдено'

    def should_not_be_mini_basket(self):
        m_bask = self.browser.find_elements(*ProductPageLocators.MINI_BASKET)
        assert not bool(m_bask), 'Мини корзина нету'