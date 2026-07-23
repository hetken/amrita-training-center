from pages.base_page import BasePage
from pages.locators import CoursesPageLocators
import requests
import allure


class CoursesPage(BasePage):
    COURSES_PAGE_URL = 'https://edu.amrita-dent.ru/courses/'

    def __init__(self, browser):
        super().__init__(browser, CoursesPage.COURSES_PAGE_URL)

    @allure.step('Collect all active courses links')
    def collect_links(self):
        links_elements = self.browser.find_elements(*CoursesPageLocators.COURSE_LINK)
        links = [element.get_attribute('href') for element in links_elements]
        return links

    @allure.step('Enter course name')
    def _enter_course(self, course):
        field = self.find_element(CoursesPageLocators.FORM_FIELD_COURSE)
        field.send_keys(course)

    @allure.step('Enter phone number')
    def _enter_phone_number(self, phone_number):
        field = self.find_element(CoursesPageLocators.FORM_FIELD_PHONE_NUMBER)
        field.send_keys(phone_number)

    @allure.step('Check the button status')
    def should_be_submit_button_disabled(self):
        button = self.find_element(CoursesPageLocators.SUBMIT_BUTTON)
        assert button.get_attribute('disabled') is not None, 'Submit button is active, but shouldn\'t be.'

    @allure.step('Check courses pages links')
    def should_open_all_active_courses_pages(self, links):
        broken_links = []

        for link in links:
            response = requests.get(link)
            if response.status_code != 200:
                broken_links.append(link)

        assert not broken_links, f'List of broken links: {"\n".join(broken_links)}'

    @allure.step('Check success message')
    def should_see_success_message(self):
        message = self.find_element(CoursesPageLocators.SUCCESS_MESSAGE)
        assert 'отправлена' in message.text,\
               f'Expected "отправлена" to be in message text, but got {message.text}'

    @allure.step('Submit form')
    def submit_form(self, course, phone_number):
        self._enter_course(course)
        self._enter_phone_number(phone_number)
        self.click_element(CoursesPageLocators.SUBMIT_BUTTON)

    @allure.step('Submit form without course')
    def submit_form_without_course(self, phone_number):
        self._enter_phone_number(phone_number)

    @allure.step('Submit form without phone number')
    def submit_form_without_phone_number(self, course):
        self._enter_course(course)
