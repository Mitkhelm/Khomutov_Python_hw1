import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class AuthPageShop:

    def __init__(self, browser):
        self._driver = browser
        self.user_name = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def auth_us(self, query):
        user_name_element = self._driver.find_element(By.ID, "user-name")
        user_name_element.send_keys(query)

    def auth_pw(self, query):
        password_element = self._driver.find_element(By.ID, "password")
        password_element.send_keys(query)
    
    def auth_login(self):
        login_element = self._driver.find_element(By.ID, "login-button")
        login_element.click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
    def set_cookie_policy(self):
        cookie = {
            'name': 'session-username',
            'value': 'standard_user'
        }
                
        self._driver.add_cookie(cookie)