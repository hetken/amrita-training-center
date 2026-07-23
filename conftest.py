import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker


@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()

@pytest.fixture(scope='session')
def fake():
    return Faker('ru-RU')
