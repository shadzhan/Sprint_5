from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):

        name, email, password = generate_registration_data()
        driver.find_element(*Locators.REG_SECTION).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)

        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_contains("login"))

        assert "login" in driver.current_url

