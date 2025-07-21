import allure


class TestAuthorization:

    @allure.title('Переход на главную страницу при авторизации')
    def test_redirect_to_main_page_after_signin(self, test_user_data, signin_page, recipes_page):
        signin_page.open_page_by_direct_url()
        signin_page.fill_signin_form(test_user_data["email"], test_user_data["password"])
        signin_page.click_signin_button()

        assert recipes_page.is_expected_url()

    @allure.title('Отображение кнопки "Выход" после авторизации')
    def test_logout_button_displayed_after_signin(self, test_user_data, signin_page, recipes_page):
        signin_page.open_page_by_direct_url()
        signin_page.fill_signin_form(test_user_data["email"], test_user_data["password"])
        signin_page.click_signin_button()

        assert recipes_page.shows_logout_button()
