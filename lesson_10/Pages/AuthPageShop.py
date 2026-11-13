import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class AuthPageShop:

    @allure.step("Открывает страницу авторизации")
    def __init__(self, browser):
        """
        Конструктор класса AuthPageShop.
        Открывает страницу браузера, находит
        поля user-name и password, кнопку login-button.
        :param driver: WebDriver - объект драйвера Selenium.
        :param user-name: WebElement — логин пользователя.
        :param password: WebElement - пароль.
        :param login-button: WebElement - кнопка login-button
        :return: None
        """
        self._driver = browser

        with allure.step("Находит поле 'user-name'"):
            self.user_name = (By.ID, "user-name")

        with allure.step("Находит поле 'password'"):
            self.password = (By.ID, "password")

        with allure.step("Находит кнопку 'login-button'"):
            self.login_button = (By.ID, "login-button")

    @allure.step("Запоняет поле 'user-name'")
    def auth_us(self, query):
        """
        Запоняет поле 'user-name'
        :param: query - вводимое значение
        :return: WebElement - введенное значение query.
        """
        with allure.step("Находит поле 'user-name'"):
            user_name_element = self._driver.find_element(By.ID, "user-name")

        with allure.step("Запоняет поле 'user-name'"):
            user_name_element.send_keys(query)

    @allure.step("Запоняет поле 'password'")
    def auth_pw(self, query):
        """
        Запоняет поле 'password'
        :param: query - вводимое значение.
        :return: WebElement - введенное значение query.
        """
        with allure.step("Находит поле 'password'"):
            password_element = self._driver.find_element(By.ID, "password")

        with allure.step("Заполняет поле 'password'"):
            password_element.send_keys(query)

    @allure.step("Прожимает кнопку 'login-button'")
    def auth_login(self):
        """
        Находит и прожимает кнопку 'login-button'.
        :param: WebElement - кнопка 'login-button'.
        :return: None
        """
        with allure.step("Находит кнопку 'login-button'"):
            login_element = self._driver.find_element(By.ID, "login-button")

        with allure.step("Прожимает кнопку 'login-button'"):
            login_element.click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )

    def set_cookie_policy(self):
        """
        Меняет настройки cookie на странице.
        :param name: WebElement - меняемый параметр.
        :param value: WebElement - новое значение.
        :return: None
        """
        cookie = {
            'name': 'session-username',
            'value': 'standard_user'
        }
        self._driver.add_cookie(cookie)