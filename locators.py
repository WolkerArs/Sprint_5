from selenium.webdriver.common.by import By

class Locators:
    # личный кабинет
    BUT_PERSONAL_ACC = (By.XPATH, './/a[@href="/account"]')
    BUT_CONSTRUCTOR = (By.XPATH,
                       './/p[@class="AppHeader_header__linkText__3q_va ml-2"][text()="Конструктор"]')
    LOGO = (By.XPATH, './/a[@href="/"]')
    BUT_LOGOUT = (By.XPATH,
                  './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')

    # войти в аккаунт на главной
    BUT_LOGIN_MAIN = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
                      "[text()='Войти в аккаунт']")

    # кнопка оформить заказ на главной
    GET_ORDER = (By.XPATH,
                 "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
                 "[text()='Оформить заказ']")

    # кнопка регистрации на странице входа
    BUT_REG = (By.XPATH, './/a[@href="/register"]')

    # кнопка восстановить пароль на странице входа
    BUT_GET_PASSWORD = (By.XPATH, './/a[@href="/forgot-password"]')

    # кнопка войти на странице регистрации и восстановления пароля
    BUT_LOGIN_TEXT = (By.XPATH, './/a[@href="/login"][text()="Войти"]')

    # форма входа
    TEXT_LOGIN = (By.XPATH, "//h2[.='Вход']")
    EMAIL_LOGIN_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    PASSWORD_LOGIN_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    BUT_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # форма регистрации
    TEXT_REG = (By.XPATH, "//h2[.='Регистрация']")
    NAME_REG_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    EMAIL_REG_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    PASSWORD_REG_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    BUT_REG_FORM = (By.XPATH,
                    './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
                    '[text()="Зарегистрироваться"]')
    ERROR_REG_FORM = (By.XPATH, './/p[@class="input__error text_type_main-default"]'
                                '[text()="Некорректный пароль"]')

    # конструктор
    BUNS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
    SAUCES_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
    TOPPINGS_SECTION = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')


