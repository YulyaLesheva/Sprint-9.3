import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу по URL')
    def open_page_by_direct_url(self, url):
        self.driver.get(url)

    @allure.step('Заполнить поле ввода')
    def fill_input_element_with_value(self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(value)

    @allure.step('Получить элемент по xpath')
    def get_element_by_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element(By.XPATH, xpath)
        
    def try_get_element_by_xpath(self, xpath, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath)
        except:
            return None

    @allure.step('Получить скрытый элемент по xpath')
    def get_hidden_element_by_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Кликнуть по элементу')
    def click_on_element_by_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        self.get_element_by_xpath(xpath).click()

    @allure.step('Проверить текущий URL')
    def is_expected_url(self, expected_url):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.url_to_be(expected_url))
            return self.driver.current_url == expected_url
        except:
            return False

    @allure.step('Проверить отображение элемента')
    def element_is_displayed_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except:
            return False

    @allure.step('Установить переменную local storage')
    def set_local_storage_variable(self, key, value):
        self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    @allure.step('Получить список элементов по xpath')
    def get_list_of_elements_by_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        return self.driver.find_elements(By.XPATH, xpath)

    @allure.step('Получить список дочерних элементов по xpath')
    def get_list_of_child_elements_by_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        parent = self.driver.find_element(By.XPATH, xpath)
        return parent.find_elements(By.XPATH, "./*")

    @allure.step('Кликнуть на элемент по индексу')
    def click_on_element_by_index(self, elements, index):
        elements[index].click()

    def type_slowly(self, element, text, delay=0.1):
        action = ActionChains(self.driver)
        action.click(element)
        for char in text:
            action.send_keys(char).perform()

    def wait_for_current_url_match_pattern(self, pattern, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            def url_matches_pattern(driver):
                return bool(pattern.match(driver.current_url))
            wait.until(url_matches_pattern)
            return True
        except:
            return False
