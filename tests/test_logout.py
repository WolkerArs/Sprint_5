from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import User
from locators import Locators

class TestLogoutChrome:

    def test_logout_button_from_personal_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        (WebDriverWait(driver, 3).
         until(EC.element_to_be_clickable(Locators.BUT_PERSONAL_ACC)).click())
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUT_LOGOUT)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TEXT_LOGIN))
        assert driver.current_url == login_page