import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_calculator(driver):
    calculator_page = CalculatorPage(
        driver,
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calculator_page.open()
    calculator_page.set_delay()
    calculator_page.enter_expression()
    calculator_page.get_result()

    assert calculator_page.get_result() == "15"

    driver.quit()
