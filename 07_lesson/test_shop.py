import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def driver():
    driver = webdriver.FireFox()
    driver.get("https://www.saucedemo.com/")


login_page = LoginPage(driver)
login_page.login("standard_user", "secret_sauce")

main_page = MainPage(driver)
main_page.add_to_cart("sauce-labs-backpack")
main_page.add_to_cart("sauce-labs-bolt-t-shirt")
main_page.add_to_cart("sauce-labs-onesie")
main_page.go_to_cart()

cart_page = CartPage(driver)
cart_page.checkout()

checkout_page = CheckoutPage(driver)
checkout_page.fill_form("Юлия", "Смирнова", "45660")
checkout_page.verify_total("58.29")

driver.quit()
