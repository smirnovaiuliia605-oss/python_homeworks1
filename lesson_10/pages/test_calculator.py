import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    WebDriver: Экземпляр драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


@allure.title("Функциональность калькулятора с задержкой")
@allure.description("Тест проверяет функциональные возможности калькулятора:"
                    " установку задержки, "
                    "ввода выражения '7+8=', получение результата '15'")
@allure.feature("Функциональность вычислений калькулятора")
@allure.severity("severity_level. CRITICAL")
def test_calculator(driver) -> None:
    """Тест для проверки операции сложения на калькуляторе."""
    with allure.step("Открыть страницу по ссылке"):
        calculator_page = CalculatorPage(
            driver, "https://bonigarcia.dev/selenium-webdriver-java/"
                    "slow-calculator.html")
    with allure.step("Открывает страницу калькулятора"):
        calculator_page.open()
    with allure.step("Устанавливает задержку на 45 секунд"):
        calculator_page.set_delay()
    with allure.step("Выводит выражение 7+8="):
        calculator_page.enter_expression()
    with allure.step("Получает результат"):
        calculator_page.get_result()
    with allure.step("Выводит на экран результат 15"):
        assert calculator_page.get_result() == "15"

    driver.quit()
