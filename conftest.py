import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from locators import Locators
from curl import *

@pytest.fixture
def driver_start():
    driver = webdriver.Chrome()
    driver.get(main_page)
    yield driver

@pytest.fixture
def register_page(driver_start):
    driver_start.find_element(*Locators.BUT_PERSONAL_ACC).click()
    WebDriverWait(driver_start, 3).until(EC.visibility_of_element_located(Locators.TEXT_LOGIN))
    driver_start.find_element(*Locators.BUT_REG).click()
    return driver_start

@pytest.fixture
def login(driver_start, email, password):
    driver_start.find_element(*Locators.EMAIL_LOGIN_INPUT).send_keys(email)
    driver_start.find_element(*Locators.PASSWORD_LOGIN_INPUT).send_keys(password)
    driver_start.find_element(*Locators.BUT_LOGIN).click()

    return driver_start

