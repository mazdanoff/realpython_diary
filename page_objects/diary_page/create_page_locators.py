from selenium.webdriver.common.by import By


class CreateEntryPageLocators:

    TITLE = (By.CSS_SELECTOR, "input#id_title")
    CONTENT = (By.CSS_SELECTOR, "textarea#id_content")
    SAVE_BUTTON = (By.CSS_SELECTOR, "input[value='Save']")
