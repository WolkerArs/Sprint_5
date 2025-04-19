from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_start
from curl import *
from data import User
from locators import Locators

class TestConstructorPageChrome:

    def test_get_constructor_page_from_personal_page_constructor_button(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        (WebDriverWait(driver, 3).
         until(EC.element_to_be_clickable(Locators.BUT_PERSONAL_ACC)).click())
        driver.find_element(*Locators.BUT_CONSTRUCTOR).click()
        assert driver.current_url == main_page
        driver.quit()

    def test_get_constructor_page_from_personal_page_logo(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        (WebDriverWait(driver, 3).
         until(EC.element_to_be_clickable(Locators.BUT_PERSONAL_ACC)).click())
        driver.find_element(*Locators.LOGO).click()
        assert driver.current_url == main_page
        driver.quit()