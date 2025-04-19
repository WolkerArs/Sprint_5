from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import register_page
from curl import *
from locators import Locators
from helper import generate_user

class TestRegistrationChrome:

    def test_success_registration(self, register_page):
        name, email, password = generate_user()
        driver = register_page
        driver.find_element(*Locators.NAME_REG_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_REG_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REG_INPUT).send_keys(password)
        driver.find_element(*Locators.BUT_REG_FORM).click()
        WebDriverWait(driver, 5).until(visibility_of_element_located(Locators.TEXT_LOGIN))
        assert driver.current_url == login_page
        driver.quit()


    def test_failed_registration_if_password_less_then_six(self, register_page):
        name = 'Арсений Дунаев'
        email = 'arsdunaev18111@mail.ru'
        password = '12345'
        driver = register_page
        driver.find_element(*Locators.NAME_REG_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_REG_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REG_INPUT).send_keys(password)
        driver.find_element(*Locators.BUT_REG_FORM).click()
        error_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_REG_FORM)).text
        assert error_text == 'Некорректный пароль'
        driver.quit()







