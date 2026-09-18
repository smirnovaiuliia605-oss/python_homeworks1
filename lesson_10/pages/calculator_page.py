import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для взаимодействия со стрпницей
    калькулятора с задержкой.
    """

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url: str) -> None:
        """
                Конструктор класса CalculatorPage.
                :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 45)

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
                Открывает страницу калькулятора.
                :param url: Базовый url веб-сайта
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay: int = 45) -> None:
        """
                Устанавливает задержку для выполнения операций на калькуляторе.
                :param delay: int — 45 секунд.
        """
        """
                Устанавливает значение задержки в поле ввода на калькуляторе.
                delay: Время задержки в секундах. По умолчанию 45.
        """
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Введение математического выражения")
    def enter_expression(self) -> None:
        """
                Нажимает на кнопку калькулятора.
                :param button: int — 7 + 8 =.
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Ожидание и получение результата {expected_text}")
    def get_result(self, expected_text: str = "15") -> str:
        """Дожидается появления ожидаемого значения на экране и возвращает его.
            expected_text: Текст, появление которого ожидается на экране.
            По умолчанию "15".

            Returns:
            str: Итоговый текст, отображаемый на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_VALUE, "15"))
        result_element = self.driver.find_element(*self.RESULT_VALUE)

        return result_element.text
