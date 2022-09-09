from selenium.webdriver.common.by import By


class DiaryPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, "h1#diary-main > a[href='/']")
    LOGOUT = (By.CSS_SELECTOR, "a[href='/admin/logout/']")
    MESSAGE = (By.CSS_SELECTOR, "ul > li.message")
