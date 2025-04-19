from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_start
from curl import *
from data import User
from locators import Locators

class TestConstructorSectionsChrome:

    def test_sauces_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.SAUCES_SECTION).click()
        assert ('tab_tab_type_current__2BEPc'
                in driver.find_element(*Locators.SAUCES_SECTION).get_attribute('class'))
        driver.quit()

    def test_toppings_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.TOPPINGS_SECTION).click()
        assert ('tab_tab_type_current__2BEPc'
                in driver.find_element(*Locators.TOPPINGS_SECTION).get_attribute('class'))
        driver.quit()

    def test_buns_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.SAUCES_SECTION).click()
        (WebDriverWait(driver, 3).until
         (EC.element_to_be_clickable(Locators.BUNS_SECTION)).click())
        (WebDriverWait(driver, 5).until
         (EC.visibility_of_element_located(Locators.BUNS_SECTION)))
        assert ('tab_tab_type_current__2BEPc'
                in driver.find_element(*Locators.BUNS_SECTION).get_attribute('class'))
        driver.quit()