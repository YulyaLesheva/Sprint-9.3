import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from client.http_client import HttpClient
from client.account_client import AccountClient
from helpers import generate_email, generate_random_string
from pages.base_page import BasePage
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from pages.create_recipe_page import CreateRecipePage
from pages.recipe_details_page import RecipeDetailsPage
from pages.header_page import HeaderPage
from urls.urls import BASE_URL_BACK


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.fixture
def http_client():
    return HttpClient(BASE_URL_BACK)


@pytest.fixture
def account_service(http_client):
    return AccountClient(http_client)


@pytest.fixture
def test_user_data(account_service):
    first_name = generate_random_string(10)
    last_name = generate_random_string(10)
    username = generate_random_string(10)
    email = generate_email()
    password = generate_random_string(10)

    payload = account_service.build_signup_payload(email, password, username, first_name, last_name)
    account_service.signup_request(payload)

    return {"email": email, "password": password}


@pytest.fixture
def auth_token(test_user_data, account_service):
    payload = account_service.build_signin_payload(test_user_data["email"], test_user_data["password"])
    response = account_service.signin_request(payload)
    return response.json()["auth_token"]


@pytest.fixture
def set_token(auth_token, signin_page):
    signin_page.open_page_by_direct_url()
    signin_page.set_local_storage_variable('token', auth_token)


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)


@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)


@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)


@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)


@pytest.fixture
def recipe_details_page(driver):
    return RecipeDetailsPage(driver)


@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)
