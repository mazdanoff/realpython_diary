from selenium.webdriver.common.by import By


class EntryPageLocators:
    DATE_TIME = (By.CSS_SELECTOR, "h2#entry-date-created")
    TITLE = (By.CSS_SELECTOR, "h3#entry-title")
    ENTRY_TEXT = (By.CSS_SELECTOR, "p#entry-content")
