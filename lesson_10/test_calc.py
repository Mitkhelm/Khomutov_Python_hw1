import pytest
from selenium import webdriver
from Pages.MainPageCalc import MainPageCalc
import allure

@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
  yield driver
  driver.quit()

@allure.suite("Калькулятор")
@allure.title("Тест работы калькулятора")
@allure.description("Ввод значение в поле задержки, проведение математического"
                    " действия")
@allure.feature("Ввод значений в поля страницы")
@allure.severity("CRITICAL")
def test_calc(driver):
  page = MainPageCalc(driver)
  page.change_delay("3")
  page.press_button()
  page.wait_for_result()
  
