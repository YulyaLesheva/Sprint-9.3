import allure
from helpers import get_resource_path
from locators.locators import (
    CREATE_RECIPE_NAME, CREATE_RECIPE_TAGS, CREATE_RECIPE_INGREDIENT_INPUT,
    CREATE_RECIPE_INGREDIENT_DROPDOWN, CREATE_RECIPE_ADD_INGREDIENT_BUTTON,
    CREATE_RECIPE_INGREDIENT_QNT, CREATE_RECIPE_DURATION,
    CREATE_RECIPE_DESCRIPTION, CREATE_RECIPE_IMAGE_INPUT,
    CREATE_RECIPE_CREATE_BUTTON
)
from pages.base_page import BasePage
from urls.urls import BASE_URL_FRONT, CREATE_RECIPE_PAGE


class CreateRecipePage(BasePage):
    page_url = f'{BASE_URL_FRONT}{CREATE_RECIPE_PAGE}'

    @allure.step('Открыть страницу создания рецепта')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Сбросить теги по умолчанию')
    def clear_default_tags(self):
        tags = self.get_list_of_elements_by_xpath(CREATE_RECIPE_TAGS)
        for tag in tags:
            if tag.get_attribute('class').find('checked') != -1:
                tag.click()

    @allure.step('Выбрать тег по индексу')
    def select_tag_by_index(self, index):
        tags = self.get_list_of_elements_by_xpath(CREATE_RECIPE_TAGS)
        self.click_on_element_by_index(tags, index)

    @allure.step('Добавить ингредиент')
    def add_ingredient(self, name, quantity):
        input_element = self.get_element_by_xpath(CREATE_RECIPE_INGREDIENT_INPUT)
        self.type_slowly(input_element, name)
        
        dropdown_elements = self.get_list_of_elements_by_xpath(CREATE_RECIPE_INGREDIENT_DROPDOWN + "//*")
        self.click_on_element_by_index(dropdown_elements, 0)
        
        self.fill_input_element_with_value(CREATE_RECIPE_INGREDIENT_QNT, str(quantity))
        self.click_on_element_by_xpath(CREATE_RECIPE_ADD_INGREDIENT_BUTTON)

    @allure.step('Заполнить название рецепта')
    def fill_recipe_name(self, name):
        self.fill_input_element_with_value(CREATE_RECIPE_NAME, name)

    @allure.step('Заполнить время приготовления')
    def fill_recipe_duration(self, duration):
        self.fill_input_element_with_value(CREATE_RECIPE_DURATION, str(duration))

    @allure.step('Заполнить описание рецепта')
    def fill_recipe_description(self, description):
        self.fill_input_element_with_value(CREATE_RECIPE_DESCRIPTION, description)

    @allure.step('Загрузить изображение рецепта')
    def upload_recipe_image(self, image_path):
        file_input = self.get_hidden_element_by_xpath(CREATE_RECIPE_IMAGE_INPUT)
        file_path = get_resource_path(image_path)
        file_input.send_keys(file_path)

    @allure.step('Заполнить данные рецепта')
    def complete_recipe_form(self, recipe_data):
        self.clear_default_tags()
        self.fill_recipe_name(recipe_data['name'])
        
        for tag_index in recipe_data['tags']:
            self.select_tag_by_index(tag_index)
        
        for ingredient in recipe_data['ingredients']:
            self.add_ingredient(ingredient['name'], ingredient['quantity'])
        
        self.fill_recipe_duration(recipe_data['time'])
        self.fill_recipe_description(recipe_data['description'])
        self.upload_recipe_image(recipe_data['image'])

    @allure.step('Сохранить рецепт')
    def save_recipe(self):
        self.click_on_element_by_xpath(CREATE_RECIPE_CREATE_BUTTON)
