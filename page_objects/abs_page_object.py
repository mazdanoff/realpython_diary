from typing import Tuple

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class AbsPageObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_element_located_present(self, locator: Tuple[str, str]):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_located_displayed(self, locator: Tuple[str, str]) -> bool:
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    def wait_for_presence_of_element_located(self, locator, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            pass

    def wait_for_visibility_of_element_located(self, locator, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            pass
