import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class MainPageShop:

    def __init__(self, browser):
        self._driver = browser
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.t_short = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart = (By.CSS_SELECTOR, "a.shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    
    def add_good(self):
        add_backpack = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_backpack.click()
        add_t_short = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_t_short.click()
        add_onesie = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_onesie.click()


    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout")))    
        
    def push_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )