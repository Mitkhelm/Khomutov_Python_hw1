import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class MainPageCalc:

    @allure.step("Открывает страницу браузера")
    def __init__(self, driver):
        """
        Конструктор класса MainPageCalc.
        :param driver: WebDriver - объект драйвера Selenium.
        """
        self._driver = driver
        """
        Открывает страницу калькулятора.
        """
        with allure.step("Находит поле задержки"):
            """
            Находит поле задержки.
            """
            self.search_delay = (By.ID, "delay")
        with allure.step("Вводит в поле задержки новое значение"):
            self.enter_value = (By.XPATH, "//span[text()]")
        with allure.step("Находит окно результата"):
            self.results_selector = (By.CSS_SELECTOR, ".screen")

    @allure.step("Замена значения в поле задержки")
    def change_delay(self, query):
        with allure.step("Выделяет поле задержки"):
            search_delay_element = self._driver.find_element(By.ID, "delay")
        with allure.step("Очищает поле задержки"):
            search_delay_element.clear()
        with allure.step("Вводит в поле задержки новое значение"):
            search_delay_element.send_keys(query)
        with allure.step("Выделяет поле задержки"):
            search_delay_element.send_keys(Keys.RETURN)

    @allure.step("Клик по клавишам")
    def press_button(self):
        with allure.step("Клик по клавише '7'"):
            seven = self._driver.find_element(By.XPATH, "//span[text()='7']")
            seven.click()
        with allure.step("Клик по клавише '+'"):
            plus = self._driver.find_element(By.XPATH, "//span[text()='+']")
            plus.click()
        with allure.step("Клик по клавише '8'"):
            eight = self._driver.find_element(By.XPATH, "//span[text()='8']")
            eight.click()
        with allure.step("Клик по клавише '='"):
            equals = self._driver.find_element(By.XPATH, "//span[text()='=']")
            equals.click()

    @allure.step("Ожидание результата")
    def wait_for_result(self):
        """
        Возвращает результат.
        :return: str - текст результата на экране калькулятора.
        """
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((self.results_selector), "15")
            )
        return self._driver.find_element(By.CSS_SELECTOR, ".screen")
    
