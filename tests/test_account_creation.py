import allure


class TestAccountCreation:

    @allure.title('Переход на страницу авторизации после создания аккаунта')
    def test_redirect_to_signin_after_account_creation(self, signup_page, signin_page):
        signup_page.open_page_by_direct_url()
        signup_page.fill_signup_form()
        signup_page.click_create_account_button()

        assert signin_page.is_expected_url()

    @allure.title('Отображение формы авторизации после создания аккаунта')
    def test_signin_form_displayed_after_account_creation(self, signup_page, signin_page):
        signup_page.open_page_by_direct_url()
        signup_page.fill_signup_form()
        signup_page.click_create_account_button()

        assert signin_page.is_displayed_signin_form()
