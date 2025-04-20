from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

class TestConstructorSectionsChrome:

    def test_sauces_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.SAUCES_SECTION).click()
        assert (EC.text_to_be_present_in_element_attribute
                (Locators.SAUCES_SECTION, 'class', 'tab_tab_type_current__2BEPc'))

    def test_toppings_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.TOPPINGS_SECTION).click()
        assert (EC.text_to_be_present_in_element_attribute
                (Locators.TOPPINGS_SECTION, 'class', 'tab_tab_type_current__2BEPc'))

    def test_buns_section_from_main_page(self, driver_start):
        driver = driver_start
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        assert (EC.text_to_be_present_in_element_attribute
                (Locators.BUNS_SECTION, 'class', 'tab_tab_type_current__2BEPc'))