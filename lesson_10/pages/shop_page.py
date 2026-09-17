import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
            Конструктор класса LoginPage.
            :param driver: WebDriver — объект драйвера Selenium.
         """
        self.driver = driver

    @allure.step("Пройти авторизацию в интернет-магазин")
    def login(self, username, password):
        """Ввести имя пользователя"""
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        """Ввести пароль"""
        self.driver.find_element(By.ID, 'password').send_keys(password)
        """Нажать кнопку войти"""
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:
    def __init__(self, driver):
        """
                    Конструктор класса MainPage.
                    :param driver: WebDriver — объект драйвера Selenium.
                 """
        self.driver = driver

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self, product_name):
        """Нажать на кнопку добавить в корзину и наименование товара"""
        self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' "
                      f"and @data-test='{product_name}']"
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link').click()


class CartPage:

    def __init__(self, driver):
        """
             Конструктор класса LoginPage.
            :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Проверить")
    def checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    @allure.step("Проверить содержимое корзины")
    def verify_cart_contents(self, expected_items):
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        actual_items = [item.text for item in cart_items]
        for item in expected_items:

            assert item in actual_items,  \
                    f"Товар {item} отсутствует в корзине"


class CheckoutPage:
    def __init__(self, driver):
        """
            Конструктор класса CheckoutPage.
            :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Оформление заказа")
    def fill_form(self, first_name, last_name, postal_code):
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

    @allure.step("Проверить результат")
    def verify_total(self, expected_total):
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        actual_total = total_element.text.split("$")[-1]

        assert actual_total == expected_total, \
            (f"Итоговая стоимость {actual_total} "
                f"не совпадает с ожидаемой {expected_total}")
