from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRY_LIST = (By.CSS_SELECTOR, "div#entry-list")
    ADD_NEW_ENTRY = (By.CSS_SELECTOR, "a > button")
