from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' "
                      f"and @data-test='{product_name}']"
        ).click()

    def go_to_cart(self):
        self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link').click()

    class CartPage:
        def __init__(self, driver):
            self.driver = driver

        def checkout(self):
            self.driver.find_element(By.ID, 'checkout').click()

        def verify_cart_contents(self, expected_items):
            cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
            actual_items = [item.text for item in cart_items]
            for item in expected_items:
                assert item in actual_items,  \
                    f"Товар {item} отсутствует в корзине"

    class CheckoutPage:
        def __init__(self, driver):
            self.driver = driver

        def fill_form(self, first_name, last_name, postal_code):
            self.driver.find_element(
                By.ID, 'first-name').send_keys(first_name)
            self.driver.find_element(
                By.ID, 'last-name').send_keys(last_name)
            self.driver.find_element(
                By.ID, 'postal-code').send_keys(postal_code)
            self.driver.find_element(
                By.ID, 'continue').click()

        def verify_total(self, expected_total):
            total_element = self.driver.find_element(
                By.CLASS_NAME, 'summary_total_label')
            actual_total = total_element.text.split("$")[-1]

            assert actual_total == expected_total, \
                (f"Итоговая стоимость {actual_total} "
                 f"не совпадает с ожидаемой {expected_total}")
