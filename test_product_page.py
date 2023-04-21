import time

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('num', [i for i in range(10)])
def test_add_product_to_basket_with_promo(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.comparison_price_and_name()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_skip_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.has_login_form_in_page_login()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    browser.implicitly_wait(5)
    product_page_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, product_page_link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_has_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209'
    page = ProductPage(browser, link)
    page.open()

    page.go_to_basket_page()
    bask_page = BasketPage(browser, browser.current_url)
    bask_page.should_be_basket_is_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(f'{time.time()}@gmail.com', time.time())
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209')
        page.open()
        page.add_to_basket()
        browser.implicitly_wait(5)
        page.should_be_has_message()

    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209')
        page.open()
        page.should_be_has_message()