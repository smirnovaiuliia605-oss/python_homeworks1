from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 10

    for link in links:
        assert link.is_displayed(), f"Link with text '{link.text}' is not displayed."
        first_link_text = links[0].text
        assert "1" in first_link_text, f"Expected '1' in first link text, but got '{first_link_text}'"

    driver.quit()
