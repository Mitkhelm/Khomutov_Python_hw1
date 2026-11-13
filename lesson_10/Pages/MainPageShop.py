import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class MainPageShop:

    @allure.step("Открывает главную страницу")
    def __init__(self, browser):
        """
        Конструктор класса MainPageShop.
        Открывает страницу браузера, находит
        карточки товаров, добавляет их в корзину, переходит
        на страницу корзины.
        :param driver: WebDriver - объект драйвера Selenium.
        :return: None
        """
        self._driver = browser

        with allure.step("Находит рюкзак"):
            self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

        with allure.step("Находит футболку"):
            self.t_short = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            
        with allure.step("Находит комбинезон"):
            self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

        with allure.step("Находит кнопку перехода в корзину"):
            self.cart = (By.CSS_SELECTOR, "a.shopping_cart_link")

        with allure.step("Находит кнопку перехода к странице оформления заказа"):
            self.checkout_button = (By.ID, "checkout")

    @allure.step("Добавляет товары в корзину")
    def add_good(self):
        """
        Находит и прожимает кнопку 'Добавить товар в корзину'
        в карточках товаров.
        :return: None.
        """

        with allure.step("Добавляет рюкзак в корзину"):
            add_backpack = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
            add_backpack.click()

        with allure.step("Добавляет футболку в корзину"):
            add_t_short = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
            add_t_short.click()

        with allure.step("Добавляет комбинезон в корзину"):
            add_onesie = self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
            add_onesie.click()

    @allure.step("Переходит на страницу корзины")
    def go_to_cart(self):
        """
        Находит и прожимает кнопку подтверждения заказа.
        :return: None.
        """
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout")))    

    @allure.step("Переходит на страницу оформления заказа")
    def push_checkout(self):
        """
        Находит и прожимает кнопку 'Далее'.
        :return: None.
        """
        self._driver.find_element(By.ID, "checkout").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )