from pages.login_page import LoginPage

import pytest


def test_login_link_and_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.has_login_form_in_page_login()
    page.has_register_form_in_page_login()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link, 5)
        page.open()
        page.go_to_login_page()
        page.has_login_form_in_page_login()
        page.has_register_form_in_page_login()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link, 5)
        page.open()
        page.should_be_login_link()