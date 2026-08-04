from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    url_user1 = driver.add_cookie({
        "name": "SESSION",
        "value": "YzA3YjI0NDMtOGNlZi00YzE5LWJkNGEtNDhjNTI1MmMwOTky",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/julia8742")

    WebDriverWait(driver, 20).until(EC.url_changes("url_user1"))
    url_user1 = driver.current_url
    driver.delete_all_cookies()
    print(f"URL пользователя 1: {url_user1}")

    driver.refresh()

    url_user2 = driver.add_cookie({
        "name": "SESSION",
        "value": "MzgzMGUwYTEtODNhZi00NDZkLWIzMTgtNjk0ZDc4NmYzZTE0",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/smirno8877")

    WebDriverWait(driver, 20).until(EC.url_changes("url_user2"))
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

    assert url_user1 != url_user2

    driver.quit()
