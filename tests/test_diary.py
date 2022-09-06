from datetime import datetime
from hamcrest import assert_that
from pytest import fixture

from conf.urls import MAIN_PAGE
from page_objects.diary_page.create_page import CreateEntryPage
from page_objects.diary_page.entry_page.entry_page import EntryPage
from page_objects.diary_page.main_page.main_page import MainPage
from page_objects.login_page.login_page import LoginPage
from page_objects.logout_page.logout_page import LogoutPage


class TestDiary:

    @fixture(autouse=True)
    def separate_session(self, driver, pytestconfig):
        """
        To handle each test case in separate session.
        If something goes awry, text next test case will still be in a separate session.
        """
        login_page = LoginPage(driver, MAIN_PAGE).open()
        main_page = MainPage(driver)
        logout_page = LogoutPage(driver)

        login_page.username.value = pytestconfig.getini('username')
        login_page.password.value = pytestconfig.getini('password')
        login_page.log_in.click()
        main_page.wait_for_page_to_load(5)
        yield
        main_page.log_out.click()
        logout_page.wait_for_page_to_load(5)

    def test_entry_display(self, driver):
        main_page = MainPage(driver)
        entry = main_page.entry_list.get_item_by_property(title="LOOKING FOR A JOB")
        title = getattr(entry, 'title')
        title.click()

        entry_page = EntryPage(driver)
        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.entry_text.value == "I need to feed my fellow geese.", "Entry page is not displayed")

    def test_create_entry(self, driver):
        test_title = f"TEST ENTRY {datetime.now()}"
        test_content = f"TEST ENTRY CONTENT {datetime.now()}"
        main_page = MainPage(driver)
        create_entry_page = CreateEntryPage(driver)
        initial_entry_count = len(main_page.entry_list)

        add_new_entry = main_page.add_new_entry
        add_new_entry.click()
        create_entry_page.wait_for_page_to_load(5)
        assert_that(create_entry_page.is_page_displayed(), "Add New Entry page is not displayed")

        create_entry_page.title.value = test_title
        create_entry_page.content.value = test_content
        create_entry_page.save_button.click()

        main_page.wait_for_page_to_load(5)
        assert_that(main_page.is_page_displayed(), "Main page is not displayed after adding a new entry")
        new_entry_count = len(main_page.entry_list)
        assert_that(new_entry_count > initial_entry_count, "Entry count was not raised after adding an entry")

        new_entry = main_page.entry_list.get_item_by_property(title=test_title)
        assert_that(new_entry is not None, "Cannot find a newly added entry on the list")
