from selenium import webdriver
import pytest

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language, })

    print('\n start browser....')
    browser = webdriver.Chrome(options=options)

    yield browser

    print('\n quit browser....')
    browser.quit()
