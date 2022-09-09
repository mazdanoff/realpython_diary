from page_objects.diary_page.diary_page import DiaryPage
from utils.db_conn_handler import DatabaseEntry
from .form_page_mixin_locators import FormPageMixinLocators as Locators
from .form_page_mixin import FormPageMixin


class UpdateEntryPage(FormPageMixin, DiaryPage):

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locators.CONTENT, timeout=timeout)

    def is_page_displayed(self):
        return self._is_url_correct() and self._is_content_field_displayed()

    def fill_new_entry(self, entry: DatabaseEntry):
        self.title.value = entry.title
        self.content.value = entry.content

    def _is_url_correct(self):
        return "update" in self.driver.current_url

    def _is_content_field_displayed(self):
        return self.is_element_located_displayed(Locators.CONTENT)
