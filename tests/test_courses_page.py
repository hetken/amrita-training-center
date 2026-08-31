import pytest
from pages.courses_page import CoursesPage
import allure


pytestmark = allure.epic('Courses page')

@pytest.mark.cant_find_course_form
@allure.feature('Form "Can\'t find the right course?"')
class TestForm:
    @pytest.fixture(scope='function')
    def page(self, browser):
        page = CoursesPage(browser)
        page.open()
        return page

    @pytest.mark.skip
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Guest can submit form with correct data')
    def test_guest_can_submit_form_with_correct_data(self, page, fake):
        course = fake.word()
        phone_number = fake.phone_number()

        page.submit_form(course, phone_number)
        page.should_see_success_message()

    @allure.title('Guest can\'t submit form without phone number')
    def test_guest_cant_submit_form_without_phone_number(self, page, fake):
        course = fake.word()

        page.submit_form_without_phone_number(course)
        page.should_be_submit_button_disabled()

    @allure.title('Guest can\'t submit form without course')
    def test_guest_cant_submit_form_without_course(self, page, fake):
        phone_number = fake.phone_number()

        page.submit_form_without_course(phone_number)
        page.should_be_submit_button_disabled()

    @allure.title('Guest can\'t submit form with empty fields')
    def test_guest_cant_submit_form_with_empty_fields(self, page):
        page.should_be_submit_button_disabled()


@pytest.mark.courses_links
@allure.feature('Links on courses page')
class TestCoursesLinks:
    @allure.title('Guest can open all active courses pages')
    def test_guest_can_open_all_active_courses_pages(self, browser):
        page = CoursesPage(browser)
        page.open()
        links = page.collect_links()
        page.should_open_all_active_courses_pages(links)
