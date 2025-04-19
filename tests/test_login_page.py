from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver_start
from curl import *
from data import User
from locators import Locators

class TestLoginPageChrome:

    def test_login_page_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        assert (WebDriverWait(driver, 3).
         until(EC.visibility_of_element_located(Locators.GET_ORDER))).text == 'Оформить заказ'
        driver.quit()

    def test_login_page_from_account_button(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_PERSONAL_ACC).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        assert (WebDriverWait(driver, 3).
                until(EC.visibility_of_element_located(Locators.GET_ORDER))).text == 'Оформить заказ'
        driver.quit()

    def test_login_page_from_registration_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.BUT_REG).click()
        driver.find_element(*Locators.BUT_LOGIN_TEXT).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        assert (WebDriverWait(driver, 3).
                until(EC.visibility_of_element_located(Locators.GET_ORDER))).text == 'Оформить заказ'
        driver.quit()

    def test_login_page_from_forgot_password_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.BUT_LOGIN_MAIN).click()
        driver.find_element(*Locators.BUT_GET_PASSWORD).click()
        driver.find_element(*Locators.BUT_LOGIN_TEXT).click()
        driver.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(User.email)
        driver.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(User.password)
        driver.find_element(*Locators.BUT_LOGIN).click()
        assert (WebDriverWait(driver, 3).
                until(EC.visibility_of_element_located(Locators.GET_ORDER))).text == 'Оформить заказ'
        driver.quit()
