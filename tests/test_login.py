import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from curl import *
from locators import Locators




def test_login_via_sign_in_button(driver):

    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys("arcticshine@ya.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                          (Locators.PLACE_ORDER_BUTTON)).text
    assert text == "Оформить заказ"



def test_login_via_personal_account_button(driver):

    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL).send_keys("arcticshine@ya.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                           (Locators.PLACE_ORDER_BUTTON)).text
    assert text == "Оформить заказ"




def test_login_via_registration_form(driver):

    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.NEW_ACCOUNT_LINK).click()
    driver.find_element(*Locators.REG_NAME).send_keys("Максим")
    driver.find_element(*Locators.REG_EMAIL).send_keys("arcticshine@ya.ru")
    driver.find_element(*Locators.REG_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.REG_BUTTON).click()
    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                           (Locators.PLACE_ORDER_BUTTON)).text
    assert text == "Оформить заказ"




def test_login_via_forgot_password(driver):
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.LOGIN_FORGOT_PASSWORD).click()
    driver.find_element(*Locators.REG_EMAIL).send_keys("arcticshine@ya.ru")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.PASSWORD_RECOVERY_SECTION))
    driver.find_element(*Locators.REG_PASSWORD).send_keys("123456789")
    driver.find_element(*Locators.EMAIL_CODE).send_keys("1234")
    driver.find_element(*Locators.SAVE_BUTTON).click()
    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                           (Locators.PLACE_ORDER_BUTTON)).text
    assert text == "Оформить заказ"





