from page_objects.diary_page.diary_page import DiaryPage
from utils.db_conn_handler import DatabaseEntry
from web_elements.button import Button
from web_elements.input_field import InputField
from .create_page_locators import CreateEntryPageLocators as Locators


class CreateEntryPage(DiaryPage):

    title = InputField(Locators.TITLE)
    content = InputField(Locators.CONTENT)
    save_button = Button(Locators.SAVE_BUTTON)

    def wait_for_page_to_load(self, timeout: int):
        self.wait_for_visibility_of_element_located(Locators.CONTENT)

    def is_page_displayed(self):
        return self.is_element_located_displayed(Locators.CONTENT)

    def fill_new_entry(self, entry: DatabaseEntry):
        self.title.value = entry.title
        self.content.value = entry.content
