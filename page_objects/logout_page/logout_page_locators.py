from selenium.webdriver.common.by import By


class LogoutPageLocators:

    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    LOGIN_AGAIN = (By.XPATH, "//a[text()='Log in again']")
