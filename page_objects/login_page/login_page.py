from page_objects.abstract.abs_base_page import AbsBasePage
from web_elements.button import Button
from web_elements.input_field import InputField

from .login_page_locators import LoginPageLocators as Locator


class LoginPage(AbsBasePage):

    username = InputField(Locator.USERNAME)
    password = InputField(Locator.PASSWORD)
    log_in = Button(Locator.LOGIN_BUTTON)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locator.USERNAME)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locator.USERNAME)
