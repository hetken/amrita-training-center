from selenium.webdriver.common.by import By

class CoursesPageLocators:
    COURSE_LINK = (By.CSS_SELECTOR, '.courses-list:first-of-type > .courses-list__item a')
    FORM_FIELD_COURSE = (By.CSS_SELECTOR, '.form-section [name="course"]')
    FORM_FIELD_PHONE_NUMBER = (By.CSS_SELECTOR, '.form-section [name="phone"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.form-section__form-button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.record-form_answer > h3')
    