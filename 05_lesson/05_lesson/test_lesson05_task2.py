from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()
    sleep(2)
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Юлия Смирнова")
    sleep(2)
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()
    sleep(2)

    assert "https://httpbin.org/post" in driver.current_url

    driver.quit()
