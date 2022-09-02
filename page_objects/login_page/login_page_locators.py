from selenium.webdriver.common.by import By


class LoginPageLocators:

    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    USERNAME = (By.CSS_SELECTOR, "input#id_username")
    PASSWORD = (By.CSS_SELECTOR, "input#id_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log in']")
