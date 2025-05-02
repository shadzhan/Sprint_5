import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from curl import *
from helper import generate_registration_data
from locators import Locators
from data import Credentials

class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):

        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.NEW_ACCOUNT_LINK).click()
        driver.find_element(*Locators.REG_NAME).send_keys("Максим")
        driver.find_element(*Locators.REG_EMAIL).send_keys("arcticshine@ya.ru")
        driver.find_element(*Locators.REG_PASSWORD).send_keys("123456789")
        driver.find_element(*Locators.REG_BUTTON).click()
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                               (Locators.PLACE_ORDER_BUTTON)).text
        assert text == "Оформить заказ"



def test_invalid_password_registration(driver,):

    name, email, password = generate_registration_data()

    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.NEW_ACCOUNT_LINK).click()
    driver.find_element(*Locators.REG_NAME).send_keys(name)
    driver.find_element(*Locators.REG_EMAIL).send_keys(email)
    driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
    driver.find_element(*Locators.REG_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ERROR_MESSAGE)
    )

    assert "Некорректный пароль" in error_message.text



def test_empty_name_registration(driver):
    email, password = generate_registration_data()
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.NEW_ACCOUNT_LINK).click()
    driver.find_element(*Locators.REG_EMAIL).send_keys(email)
    driver.find_element(*Locators.REG_PASSWORD).send_keys(password)

    reg_button = driver.find_element(*Locators.REG_BUTTON)
    assert not reg_button.is_enabled(), "Кнопка регистрации должна быть неактивной"


def test_registration_with_existing_account(driver):
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.NEW_ACCOUNT_LINK).click()
    driver.find_element(*Locators.REG_NAME).send_keys("Максим")
    driver.find_element(*Locators.REG_EMAIL).send_keys("savir@ya.ru")
    driver.find_element(*Locators.REG_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.REG_BUTTON).click()

    error_message_of_existing_account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.ERROR_MESSAGE_OF_EXISTING_ACCOUNT))

    assert "Такой пользователь уже существует" in error_message_of_existing_account.text