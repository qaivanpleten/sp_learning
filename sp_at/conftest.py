import pytest
from selenium import webdriver


@pytest.fixture
def fixture_webdriver() -> webdriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://console.stage.sonikpass.com/")

    yield driver
    driver.quit()