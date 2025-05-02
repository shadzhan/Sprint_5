from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from data import Credentials
from locators import Locators
from curl import *

class TestSauceSectionNavigation:

    def test_switch_to_sauces_section(self, driver):

        sauces_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.SAUCES_SECTION)
        )
        sauces_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Соусы"
        assert "current" in sauces_tab.get_attribute("class")

    def test_switch_to_toppings_section(self, driver):

        toppings_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.TOPPINGS_SECTION)
        )
        toppings_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Начинки"
        assert "current" in toppings_tab.get_attribute("class")

    def test_switch_to_buns_section(self, driver):

        buns_tab = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.BUNS_SECTION)
        )

        buns_tab.click()

        active_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )
        assert active_tab.text == "Булки"
        assert "current" in buns_tab.get_attribute("class")