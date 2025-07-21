import allure

from locators.locators import RECIPIES_MENU
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Перейти к разделу')
    def navigate_to_section(self, section_name):
        tabs = self.get_list_of_elements_by_xpath(RECIPIES_MENU)

        for tab in tabs:
            if tab.text == section_name:
                return tab.click()

        raise Exception(f"Не удалось найти раздел с текстом '{section_name}'")
