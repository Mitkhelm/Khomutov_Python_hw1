import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:

    @allure.step("Открывает страницу оформления заказа")
    def __init__(self, browser):
        """
        Конструктор класса CartPage.
        Открывает страницу браузера, находит
        поля 'Имя', 'Фамилия', 'Индекс', 'Итоговая сумма'.
        :param driver: WebDriver - объект драйвера Selenium.
        :param first-name: WebElement — имя.
        :param last-name: WebElement - фамилия.
        :param postal-code: WebElement - почтовый индекс.
        :param div.summary_total_label: WebElement - сумма.
        :return: None
        """
        self._driver = browser

        with allure.step("Находит поле 'Имя'"):
            self.my_first_name = (By.ID, "first-name")

        with allure.step("Находит поле 'Фамилия'"):
            self.my_last_name = (By.ID, "last-name")

        with allure.step("Находит поле 'Индекс'"):
            self.my_zip = (By.ID, "postal-code")

        with allure.step("Находит поле 'Сумма заказа'"):
            self.result = (By.CSS_SELECTOR, "div.summary_total_label")   

    @allure.step("Заполняет поле 'Имя'")
    def first_name(self, query):
        """
        Запоняет поле 'first-name'
        :param: query - вводимое значение
        :return: WebElement - введенное значение query.
        """

        with allure.step("Находит поле 'Имя'"):
            my_first_name_element = self._driver.find_element(By.ID, "first-name")

        with allure.step("Запоняет поле 'Имя'"):
            my_first_name_element.send_keys(query)

    @allure.step("Заполняет поле 'Фамилия'")
    def last_name(self, query):
        """
        Запоняет поле 'last-name'
        :param: query - вводимое значение
        :return: WebElement - введенное значение query.
        """

        with allure.step("Находит поле 'Фамилия'"):
            my_last_name_element = self._driver.find_element(By.ID, "last-name")

        with allure.step("Заполняет поле 'Фамилия'"):
            my_last_name_element.send_keys(query)

    @allure.step("Заполняет поле 'Индекс'")
    def zip(self, query):
        """
        Запоняет поле 'postal-code'
        :param: query - вводимое значение
        :return: WebElement - введенное значение query.
        """

        with allure.step("Находит поле 'Индекс'"):
            my_zip_element = self._driver.find_element(By.ID, "postal-code")

        with allure.step("Заполняет поле 'Индекс'"):
            my_zip_element.send_keys(query)

    @allure.step("Прожимает кнопку 'Далее'")
    def next(self):
        """
        Находит кнопку 'Далее' и нажимает на нее.
        :return: None.
        """
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Сравнивает итоговую сумму с заданной в ТЗ")
    def total_cost(self):
        """
        Находит поле с итоговой суммой и сравнивает с ожидаемым результатом.
        :return: str — текст итоговой суммы.
        """
        WebDriverWait(self._driver, 7).until(
            EC.text_to_be_present_in_element((self.result), "$58.29")
            )
        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text 
