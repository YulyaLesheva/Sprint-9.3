import allure
from data.test_data import recipe_1


class TestRecipeCreation:

    @allure.title('Отображение карточки созданного рецепта')
    def test_recipe_card_displayed_after_creation(self, set_token, recipes_page, header_page, create_recipe_page, recipe_details_page):
        
        recipes_page.open_page_by_direct_url()

        header_page.navigate_to_section('Создать рецепт')
        create_recipe_page.complete_recipe_form(recipe_1)
        create_recipe_page.save_recipe()
        
        assert recipe_details_page.is_recipe_page_opened()

    @allure.title('Название рецепта отображается в карточке')
    def test_recipe_name_displayed_in_card(self, set_token, recipes_page, header_page, create_recipe_page, recipe_details_page):
        
        recipes_page.open_page_by_direct_url()

        header_page.navigate_to_section('Создать рецепт')
        create_recipe_page.complete_recipe_form(recipe_1)
        create_recipe_page.save_recipe()
        
        assert recipe_details_page.get_recipe_title() == recipe_1['name'] 