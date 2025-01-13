from datetime import datetime

from hamcrest import assert_that
from pytest import fixture

from conf.urls import MAIN_PAGE_URL
from page_objects.diary_page.create_entry_page import CreateEntryPage
from page_objects.diary_page.delete_entry_page import DeleteEntryPage
from page_objects.diary_page.entry_page.entry_page import EntryPage
from page_objects.diary_page.main_page.main_page import MainPage
from page_objects.diary_page.update_entry_page import UpdateEntryPage
from page_objects.login_page.login_page import LoginPage
from page_objects.logout_page.logout_page import LogoutPage
from utils.db_conn_handler import DatabaseEntry


class TestDiary:

    def test_entry_display(self, driver):

        # set up test data
        main_page = MainPage(driver)
        entry_page = EntryPage(driver)
        entry_title = "LOOKING FOR A JOB"
        expected_content = "I need to feed my fellow geese."

        # 1. Click the title of a known entry
        entry = main_page.entry_list.get_item_by_property(title=entry_title)
        assert_that(entry is not None, "Cannot find the predefined entry")
        entry.title.click()

        # 2. Check that the entry page is displayed
        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == expected_content, "Content does not match the expected value")

    def test_create_entry(self, driver):

        # set up test data
        main_page = MainPage(driver)
        create_entry_page = CreateEntryPage(driver)
        initial_entry_count = len(main_page.entry_list)
        test_entry = DatabaseEntry.new()

        # 1. Click "Add new entry" button and verify that a page for creating a new entry is displayed
        main_page.add_new_entry.click()
        create_entry_page.wait_for_page_to_load(5)
        assert_that(create_entry_page.is_page_displayed(), "Add New Entry page is not displayed")

        # 2. Fill given fields with predefined values and click "Save"
        create_entry_page.fill_new_entry(test_entry)
        create_entry_page.save_button.click()

        # 3. Verify that main page with entry list is displayed
        main_page.wait_for_page_to_load(5)
        assert_that(main_page.is_page_displayed(), "Main page is not displayed after adding a new entry")

        # 4. Verify that entry count has increased
        new_entry_count = len(main_page.entry_list)
        assert_that(new_entry_count > initial_entry_count, "Entry count was not raised after adding an entry")

        # 5. Verify that a new entry with predefined values is present
        new_entry = main_page.entry_list.get_entry(test_entry)
        assert_that(new_entry is not None, "Cannot find a newly added entry on the list")

    def test_update_entry(self, driver, created_entry):

        # set up test data
        main_page = MainPage(driver)
        entry_page = EntryPage(driver)
        update_entry_page = UpdateEntryPage(driver)
        new_entry = created_entry
        main_page.wait_for_entry_to_appear_on_the_list(new_entry)  # a new entry was fabricated via direct db connection

        # 1. Click on the predefined test entry
        entry_element = main_page.entry_list.get_entry(new_entry)
        assert_that(entry_element is not None, "Inserted entry does not appear on the list")
        entry_element.title.click()

        # 2. Verify that the exact entry page is displayed
        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == new_entry.content, "Opened entry's content does not match")

        # 3. Click "Edit" button,
        #    check that the page for updating the entry is displayed,
        #    change entries' contents and click "Save"
        entry_page.edit.click()
        update_entry_page.wait_for_page_to_load(5)
        assert_that(update_entry_page.is_page_displayed(), "Update entry page is not displayed")
        new_content = f"New Content at {datetime.now()}"
        update_entry_page.content.value = new_content
        update_entry_page.save_button.click()

        # 4. Verify that entry page is displayed, entries' contents are changed and a confirmation message showed up
        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == new_content, "Opened entry's content does not match")
        assert_that(entry_page.message.is_displayed(), "No message present")
        assert_that(entry_page.message.value == "Your entry was updated!", "Message does not match the expected text")

    def test_delete_entry(self, driver, created_entry):

        # set up test data
        main_page = MainPage(driver)
        entry_page = EntryPage(driver)
        delete_entry_page = DeleteEntryPage(driver)
        new_entry = created_entry
        main_page.wait_for_entry_to_appear_on_the_list(new_entry)

        # 1. Click on the predefined test entry
        entry_element = main_page.entry_list.get_entry(new_entry)
        assert_that(entry_element is not None, "Inserted entry does not appear on the list")
        entry_element.title.click()

        # 2. Verify that the exact entry page is displayed
        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == new_entry.content, "Opened entry's content does not match")

        # 3. Click "Delete" button, check that a confirmation page is displayed and click "Confirm"
        entry_page.delete.click()
        delete_entry_page.wait_for_page_to_load(5)
        assert_that(delete_entry_page.is_page_displayed(), "Delete entry page is not displayed")
        delete_entry_page.confirm.click()

        # 4. Check that the main page is displayed and that the predefined entry is nowhere to be found
        main_page.wait_for_page_to_load(5)
        assert_that(main_page.is_page_displayed(), "Main page was not displayed after deletion")
        deleted_entry = main_page.entry_list.get_entry(new_entry)
        assert_that(deleted_entry is None, "Deletion did not succeed, found test entry")

    @fixture(autouse=True)
    def separate_session(self, driver, pytestconfig):
        """
        To handle each test case separately.
        NOTE: This fixture is only visible by test cases within this test class.
        """
        login_page = LoginPage(driver, MAIN_PAGE_URL).open()
        main_page = MainPage(driver)
        logout_page = LogoutPage(driver)

        login_page.username.value = pytestconfig.getini('username')
        login_page.password.value = pytestconfig.getini('password')
        login_page.log_in.click()
        main_page.wait_for_page_to_load(5)
        yield
        main_page.log_out.click()
        logout_page.wait_for_page_to_load(5)

    @fixture(autouse=True)
    def delete_test_entries_from_db(self, database):
        """Cleans up the database from entries created in test session."""
        yield
        test_entries = database.read_entries()
        for entry in test_entries:
            if "New Test Entry:" in entry.title:
                database.delete_entry(entry)

    @fixture
    def created_entry(self, database):
        """Fabricates an entry to manipulate in test."""
        new_entry = DatabaseEntry.new()
        database.add_entry(new_entry)
        yield new_entry
        database.delete_entry(new_entry)
