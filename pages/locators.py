from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-group .btn-default:nth-child(1)')
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, '#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, '#register_form')

    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, ' #messages > div:nth-child(1) > div strong')
    PRICE_BASKET_IN_ALERT = (By.CSS_SELECTOR, ' #messages > div:nth-child(3) > div strong')

    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_SHOPPING = (By.CSS_SELECTOR, '#messages strong')

    MINI_BASKET = (By.CSS_SELECTOR, '.basket-mini')


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')