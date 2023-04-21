from pages.base_page import BasePage
from pages.locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def open(self):
        self.browser.get(self.url)

    def has_login_form_in_page_login(self):
        login_form = self.browser.find_elements(*LoginPageLocators.FORM_LOGIN)
        assert bool(login_form), 'Форма логина на странице нету'

    def has_register_form_in_page_login(self):
        register_form = self.browser.find_elements(*LoginPageLocators.FORM_REGISTER)
        assert bool(register_form), 'Форма регистрация на странице нету'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()