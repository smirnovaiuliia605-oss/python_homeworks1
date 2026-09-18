import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver) -> None:
        """
            Класс для взаимодействия со страницей авторизации
            Инициализирует страницу авторизации.
            driver: Экземпляр Selenium WebDriver.
         """
        self.driver = driver

    @allure.step("Пройти авторизацию в интернет-магазин"
                 " под пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """Ввести имя пользователя"""
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        """Ввести пароль"""
        self.driver.find_element(By.ID, 'password').send_keys(password)
        """Нажать кнопку войти"""
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:
    def __init__(self, driver) -> None:
        """Класс для взаимодействия
        с главной страницей каталога товаров.
        driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Добавить товар {product_name} в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет выбранный товар в корзину по его имени (data-test).
        product_name: Значение атрибута data-test для кнопки товара.
        """
        self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' "
                      f""f"and @data-test='{product_name}']"
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины нажатием на иконку.
        """
        self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link').click()


class CartPage:
    """Класс для взаимодействия со страницей корзины."""

    def __init__(self, driver) -> None:
        """
             Отображает страницу корзины на экране.
            :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Пезеходит к оформлению заказа")
    def checkout(self) -> None:
        self.driver.find_element(By.ID, 'checkout').click()

    @allure.step("Проверить содержимое корзины")
    def verify_cart_contents(self, expected_items: str) -> None:
        """Проверяет, что все ожидаемые
        товары отображаются в корзине.
         expected_items: Список названий товаров,
         которые должны быть в корзине.
        AssertionError: Если какой-либо из ожидаемых товаров не найден.
        """
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        actual_items = [item.text for item in cart_items]
        for item in expected_items:

            assert item in actual_items,  \
                    f"Товар {item} отсутствует в корзине"


class CheckoutPage:
    """Класс для взаимодействия со страницей оформления заказа."""
    def __init__(self, driver) -> None:
        """
            Конструктор класса CheckoutPage.
            :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Оформление заказа")
    def fill_form(self, first_name: str,
                  last_name: str, postal_code: str) -> None:
        """Ввести данные пользователя:
        фамилия, имя, почтовый индекс,
        нажать кнопку Продолжить.
        """
        self.driver.find_element(
                By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(
                By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(
                By.ID, 'postal-code').send_keys(postal_code)
        self.driver.find_element(
                By.ID, 'continue').click()

    @allure.step("Проверbnm итоговой стоимости заказа. "
                 "Ожидается: ${expected_total}")
    def verify_total(self, expected_total: str) -> None:
        """Проверяет, что финальная стоимость заказа совпадает с ожидаемой.
            expected_total: Ожидаемая сумма в виде строки (например, '43.18').
            AssertionError: Если фактическая
            стоимость не совпадает с ожидаемой.
                """
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        actual_total = total_element.text.split("$")[-1]

        assert actual_total == expected_total, \
            (f"Итоговая стоимость {actual_total} "
                f"не совпадает с ожидаемой {expected_total}")
