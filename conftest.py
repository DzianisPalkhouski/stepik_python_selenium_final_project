import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\nstart browser for test...')
    browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield browser
    print('\nquit browser...')
    browser.quit()
