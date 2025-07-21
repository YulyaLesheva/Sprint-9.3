import allure
from locators.locators import (
    SIGNIN_HEADER, SIGNIN_EMAIL_INPUT, SIGNIN_PASSWORD_INPUT,
    SIGNIN_LOGIN_BUTTON, HEADER_SIGNIN_BUTTON
)
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, SIGNIN_PAGE


class SigninPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{SIGNIN_PAGE}'

    @allure.step('Открыть страницу авторизации')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Кликнуть кнопку "Войти" в шапке')
    def click_signin_button_in_header(self):
        self.click_on_element_by_xpath(HEADER_SIGNIN_BUTTON)

    @allure.step('Заполнить форму авторизации')
    def fill_signin_form(self, email, password):
        self.fill_input_element_with_value(SIGNIN_EMAIL_INPUT, email)
        self.fill_input_element_with_value(SIGNIN_PASSWORD_INPUT, password)

    @allure.step('Кликнуть кнопку "Войти"')
    def click_signin_button(self):
        self.click_on_element_by_xpath(SIGNIN_LOGIN_BUTTON)

    @allure.step('Проверить отображение формы авторизации')
    def is_displayed_signin_form(self):
        return self.element_is_displayed_by_xpath(SIGNIN_HEADER)

    @allure.step('Проверить URL страницы авторизации')
    def is_expected_url(self):
        return super().is_expected_url(self.page_url)
