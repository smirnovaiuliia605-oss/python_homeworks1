import allure
import pytest
from selenium import webdriver
from allure_commons.types import Severity
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage



@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Оформление заказа в интернет-магазине")
@allure.description(
    "Тест проверяет оформление заказа на странице интернет магазина: "
    "авторизацию на главной странице, добавление товара в корзину,"
    "переход на страницу оформления заказа,"
    "заполнение формы с личными данными, "
    "проверку итоговой суммы заказа"
)
@allure.feature("Оформление заказа")
@allure.severity(Severity.BLOCKER)
def test_checkout_flow(driver):

    with allure.step("Пройти авторизацию: ввести имя пользователя и пароль"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        main_page = MainPage(driver)
        main_page.add_to_cart("sauce-labs-backpack")
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("sauce-labs-onesie")
        main_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполнить обязательные поля и проверить итоговую сумму"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Юлия", "Смирнова", "45660")
        checkout_page.verify_total("58.29")
