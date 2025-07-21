import allure
from helpers import generate_random_string, generate_email
from locators.locators import (
    SIGNUP_HEADER, SIGNUP_FIRSTNAME_INPUT, SIGNUP_LASTNAME_INPUT,
    SIGNUP_USERNAME_INPUT, SIGNUP_EMAIL_INPUT, SIGNUP_PASSWORD_INPUT,
    SIGNUP_CREATE_ACCOUNT_BUTTON, HEADER_CREATE_ACCOUNT_BUTTON
)
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, SIGNUP_PAGE


class SignupPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{SIGNUP_PAGE}'

    @allure.step('Открыть страницу регистрации')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Кликнуть кнопку "Создать аккаунт" в шапке')
    def click_create_account_button_in_header(self):
        self.click_on_element_by_xpath(HEADER_CREATE_ACCOUNT_BUTTON)

    @allure.step('Заполнить форму регистрации')
    def fill_signup_form(self):
        first_name = generate_random_string(10)
        last_name = generate_random_string(10)
        username = generate_random_string(10)
        email = generate_email()
        password = generate_random_string(10)
        
        self.fill_input_element_with_value(SIGNUP_FIRSTNAME_INPUT, first_name)
        self.fill_input_element_with_value(SIGNUP_LASTNAME_INPUT, last_name)
        self.fill_input_element_with_value(SIGNUP_USERNAME_INPUT, username)
        self.fill_input_element_with_value(SIGNUP_EMAIL_INPUT, email)
        self.fill_input_element_with_value(SIGNUP_PASSWORD_INPUT, password)

    @allure.step('Кликнуть кнопку "Создать аккаунт"')
    def click_create_account_button(self):
        self.click_on_element_by_xpath(SIGNUP_CREATE_ACCOUNT_BUTTON)

    @allure.step('Проверить отображение формы регистрации')
    def is_displayed_signup_form(self):
        return self.element_is_displayed_by_xpath(SIGNUP_HEADER)
