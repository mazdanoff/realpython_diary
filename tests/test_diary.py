from datetime import datetime
from time import sleep

from hamcrest import assert_that
from pytest import fixture

from conf.urls import MAIN_PAGE
from page_objects.diary_page.create_page import CreateEntryPage
from page_objects.diary_page.entry_page.entry_page import EntryPage
from page_objects.diary_page.main_page.main_page import MainPage
from page_objects.diary_page.update_page import UpdateEntryPage
from page_objects.login_page.login_page import LoginPage
from page_objects.logout_page.logout_page import LogoutPage
from utils.db_conn_handler import DatabaseEntry


class TestDiary:

    def test_entry_display(self, driver):

        # test data
        main_page = MainPage(driver)
        entry_page = EntryPage(driver)
        entry_title = "LOOKING FOR A JOB"
        expected_content = "I need to feed my fellow geese."

        # test body
        entry = main_page.entry_list.get_item_by_property(title=entry_title)
        title = getattr(entry, 'title')
        title.click()

        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == expected_content, "Content does not match the expected value")

    def test_create_entry(self, driver, delete_entry_from_db):

        # test data
        main_page = MainPage(driver)
        create_entry_page = CreateEntryPage(driver)

        # test body
        initial_entry_count = len(main_page.entry_list)
        test_entry = DatabaseEntry.new()

        add_new_entry = main_page.add_new_entry
        add_new_entry.click()
        create_entry_page.wait_for_page_to_load(5)
        assert_that(create_entry_page.is_page_displayed(), "Add New Entry page is not displayed")

        create_entry_page.fill_new_entry(test_entry)
        create_entry_page.save_button.click()

        main_page.wait_for_page_to_load(5)
        assert_that(main_page.is_page_displayed(), "Main page is not displayed after adding a new entry")

        new_entry_count = len(main_page.entry_list)
        assert_that(new_entry_count > initial_entry_count, "Entry count was not raised after adding an entry")

        new_entry = main_page.entry_list.get_entry(test_entry)
        assert_that(new_entry is not None, "Cannot find a newly added entry on the list")

        # teardown
        delete_entry_from_db(test_entry)

    def test_update_entry(self, driver, created_entry):

        # test data
        main_page = MainPage(driver)
        entry_page = EntryPage(driver)
        update_entry_page = UpdateEntryPage(driver)
        new_entry = created_entry
        main_page.wait_for_entry_to_appear_on_the_list(new_entry)

        # test body
        entry_element = main_page.entry_list.get_entry(new_entry)
        assert_that(entry_element is not None, "Inserted entry does not appear on the list")
        entry_element.title.click()

        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == new_entry.content, "Opened entry's content does not match")

        entry_page.edit.click()
        update_entry_page.wait_for_page_to_load(5)
        assert_that(update_entry_page.is_page_displayed(), "Update entry page is not displayed")
        new_content = f"New Content at {datetime.now()}"
        update_entry_page.content.value = new_content
        update_entry_page.save_button.click()

        entry_page.wait_for_page_to_load(5)
        assert_that(entry_page.is_page_displayed(), "Entry page is not displayed")
        assert_that(entry_page.content.value == new_content, "Opened entry's content does not match")
        assert_that(entry_page.message.is_displayed(), "No message present")
        assert_that(entry_page.message.value == "Your entry was updated!", "Message does not match the expected text")

    # def test_delete_entry(self, driver, created_entry):
    #
    #     main_page = MainPage(driver)
    #     entry_page = EntryPage(driver)
    #     delete_entry_page = DeleteEntryPage(driver)

    @fixture(autouse=True)
    def separate_session(self, driver, pytestconfig):
        """
        To handle each test case in separate session.
        If something goes awry, text next test case will still be in a separate session.

        This fixture is only visible by test cases within this test class
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

    @fixture
    def delete_entry_from_db(self, database):
        return database.delete_entry

    @fixture
    def created_entry(self, database):
        entry = DatabaseEntry.new()
        database.add_entry(entry)
        yield entry
        database.delete_entry(entry)
