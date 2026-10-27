import pytest
from selenium import webdriver
from Pages.AuthPageShop import AuthPageShop
from Pages.MainPageShop import MainPageShop
from Pages.CartPageShop import CartPage
from time import sleep



@pytest.fixture()
def browser():
  driver = webdriver.Firefox()
  driver.maximize_window()
  yield driver
  driver.quit()
 

def test_shop(browser):
   browser.get("https://www.saucedemo.com/")
   auth = AuthPageShop(browser)
   auth.auth_us("standard_user")
   auth.auth_pw("secret_sauce")
   auth.auth_login()

   buy = MainPageShop(browser)
   buy.add_good()
   buy.go_to_cart()
   buy.push_checkout()

   checkout = CartPage(browser)
   checkout.first_name("Игорь")
   checkout.last_name("Хомутов")
   checkout.zip("123456")
   checkout.next()
   checkout.total_cost()


   
