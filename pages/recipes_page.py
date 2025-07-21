import allure
from locators.locators import RECIPIES_HEADER, HEADER_LOGOUT_BUTTON
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, RECIPES_PAGE


class RecipesPage(BasePage):
    page_url = f'{BASE_URL_FRONT}{RECIPES_PAGE}'

    @allure.step('Открыть страницу рецептов')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Проверить заголовок страницы')
    def has_page_title(self):
        return self.element_is_displayed_by_xpath(RECIPIES_HEADER)

    @allure.step('Проверить кнопку выхода')
    def shows_logout_button(self):
        return self.element_is_displayed_by_xpath(HEADER_LOGOUT_BUTTON)

    @allure.step('Проверить URL главной страницы')
    def is_expected_url(self):
        return super().is_expected_url(self.page_url)
