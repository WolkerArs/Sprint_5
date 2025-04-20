from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import User
from locators import Locators

class TestPersonalPageChrome:

    def test_get_personal_pege_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        (WebDriverWait(driver, 3).
         until(EC.element_to_be_clickable(Locators.BUT_PERSONAL_ACC)).click())
        assert driver.current_url == personal_page