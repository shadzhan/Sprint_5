import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import main_site
from locators import Locators
from data import Credentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver, main_site):
    driver.get(main_site)

    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.REG_EMAIL)
    )
    email_field.send_keys(Credentials.email)

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.REG_PASSWORD)
    )
    password_field.send_keys(Credentials.password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.REG_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(main_site)
    )

    return driver
