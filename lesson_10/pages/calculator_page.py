import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, '#delay')
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
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
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self):
        """
                Устанавливает задержку для выполнения операций на калькуляторе.
                :param delay: int — 45 секунд.
        """
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Нажатие кнопок '{button}'")
    def enter_expression(self):
        """
                Нажимает на кнопку калькулятора.
                :param button: int — 7 + 8 =.
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
                Возвращает текущий результат с экрана калькулятора.
                :return: int - число 15.
                """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_VALUE, "15"))
        result_element = self.driver.find_element(*self.RESULT_VALUE)
        return result_element.text
