from typing import Tuple

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    def __init__(self, locator: Tuple[str, str], wait_con=None,
                 timeout: int = 10, name: str = "Element"):
        self._locator = locator
        self._page_object = None
        self.wait_con = wait_con
        self.timeout = timeout
        self.name = name

    def __get__(self, obj, owner):
        self._page_object = obj
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", by="{self._locator[0]}", what="{self._locator[1]}")'

    @property
    def element(self) -> WebElement:
        if self.wait_con is not None:
            wait = WebDriverWait(self._page_object.driver, self.timeout)
            condition = self.wait_con(self._locator)
            return wait.until(condition)
        return self._page_object.driver.find_element(*self._locator)

    def is_present(self):
        try:
            if self.element:
                return True
        except NoSuchElementException:
            return False

    def is_displayed(self):
        try:
            return self.element.is_displayed()
        except NoSuchElementException:
            return False
