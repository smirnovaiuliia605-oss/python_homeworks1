from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(
        (By.NAME, 'add-to-cart-sauce-labs-backpack')
    ))

    backpack = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    shirt = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    shirt.click()
    onesie = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    shopping_cart_container = driver.find_element(
        By.ID, "shopping_cart_container")
    shopping_cart_container.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    wait.until(EC.element_to_be_clickable((By.ID, 'first-name')))

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Юлия")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Смирнова")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("456060")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    print(f"Получена итоговая стоимость: {total_text}")

    assert total_text == "$58.29"

    driver.quit()
