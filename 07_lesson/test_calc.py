import pytest
from selenium import webdriver
from Pages.MainPageCalc import MainPageCalc


@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
  yield driver
  driver.quit()
  
def test_calc(driver):
  page = MainPageCalc(driver)
  page.change_delay("45")
  page.press_button()
  page.wait_for_result()
  
