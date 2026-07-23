from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator),
               message=f'Element {locator} is not clickable.')
        self.browser.execute_script("arguments[0].click();", element)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator),
               message=f'Element {locator} is not on the page.')

    @allure.step('Open page')
    def open(self):
        self.browser.get(self.url)
