from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link, 3)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.basket_is_empty()