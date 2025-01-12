from selenium.webdriver.common.by import By

class DeleteEntryPageLocators:

    PAGE_HEADER = (By.CSS_SELECTOR, "h1#diary-main > a[href='/']")
    CONFIRM = (By.CSS_SELECTOR, "form[method='post'] > input[type='submit']")
    CANCEL = (By.CSS_SELECTOR, "form[method='post'] > a")
