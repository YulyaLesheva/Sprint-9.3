import allure
import re
from locators.locators import RECIPE_DETAILS_NAME
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, RECIPE_DETAILS_PAGE


class RecipeDetailsPage(BasePage):
    page_url_pattern = f'{BASE_URL_FRONT}{RECIPE_DETAILS_PAGE}'

    @allure.step('Проверить что открылась страница рецепта')
    def is_recipe_page_opened(self):
        pattern = re.compile(rf"^{re.escape(self.page_url_pattern)}\d+$")
        return self.wait_for_current_url_match_pattern(pattern)

    @allure.step('Получить название рецепта')
    def get_recipe_title(self):
        return self.get_element_by_xpath(RECIPE_DETAILS_NAME).text
