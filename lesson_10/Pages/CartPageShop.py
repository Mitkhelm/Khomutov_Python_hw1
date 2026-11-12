import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self.my_first_name = (By.ID, "first-name")
        self.my_last_name = (By.ID, "last-name")
        self.my_zip = (By.ID, "postal-code")
        self.result = (By.CSS_SELECTOR, "div.summary_total_label")   

    def first_name(self, query):
        my_first_name_element = self._driver.find_element(By.ID, "first-name")
        my_first_name_element.send_keys(query)

    def last_name(self, query):
        my_last_name_element = self._driver.find_element(By.ID, "last-name")
        my_last_name_element.send_keys(query)

    def zip(self, query):
        my_zip_element = self._driver.find_element(By.ID, "postal-code")
        my_zip_element.send_keys(query)

    def next(self):
        self._driver.find_element(By.ID, "continue").click()

    def total_cost(self):
        WebDriverWait(self._driver, 7).until(
            EC.text_to_be_present_in_element((self.result), "$58.29")
            )
        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text 
