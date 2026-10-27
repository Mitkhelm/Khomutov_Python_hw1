import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageCalc:

    def __init__(self, driver):
        self._driver = driver
        self.search_delay = (By.ID, "delay")
        self.enter_value = (By.XPATH, "//span[text()]")
        self.results_selector = (By.CSS_SELECTOR, ".screen")

    def change_delay(self, query):
        search_delay_element = self._driver.find_element(By.ID, "delay")
        search_delay_element.clear()
        search_delay_element.send_keys(query)
        search_delay_element.send_keys(Keys.RETURN)

    def press_button(self):
        seven = self._driver.find_element(By.XPATH, "//span[text()='7']")
        seven.click()
        plus = self._driver.find_element(By.XPATH, "//span[text()='+']")
        plus.click()
        eight = self._driver.find_element(By.XPATH, "//span[text()='8']")
        eight.click()
        equals = self._driver.find_element(By.XPATH, "//span[text()='=']")
        equals.click()

    def wait_for_result(self):
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((self.results_selector), "15")
            )
        return self._driver.find_element(By.CSS_SELECTOR, ".screen")
    
