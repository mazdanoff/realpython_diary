from page_objects.abstract.abs_base_page import AbsBasePage
from web_elements.link import Link
from web_elements.text import Text

from .logout_page_locators import LogoutPageLocators as Locator


class LogoutPage(AbsBasePage):

    page_header = Text(Locator.PAGE_HEADER)
    log_in_again = Link(Locator.LOGIN_AGAIN)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locator.LOGIN_AGAIN)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locator.LOGIN_AGAIN)
