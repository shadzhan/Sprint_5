import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from curl import *
from locators import Locators
from data import Credentials


def test_access_personal_account(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Locators.ENTER_SECTION)
    )
    assert "/login" in driver.current_url


def test_switch_to_constructor(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON)
    )
    assert driver.current_url == main_site


def test_switch_to_constructor_from_personal_account_by_logo(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGO_STELLAR_SIGN)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON)
    )

    assert driver.current_url == main_site


def test_logout(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys("arcticshine@ya.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(Locators.ENTER_SECTION)
    )
    assert "/login" in driver.current_url
