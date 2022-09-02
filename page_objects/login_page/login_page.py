from page_objects.abstract.abs_base_page import AbsBasePage

from .login_page_locators import LoginPageLocators


class LoginPage(AbsBasePage):

    def is_page_displayed(self):
        return self.is_element_located_displayed(LoginPageLocators.USERNAME)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(LoginPageLocators.USERNAME)
