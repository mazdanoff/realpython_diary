from pytest import mark
from hamcrest import assert_that

from conf.urls import *
from page_objects.diary_page.diary_page import DiaryPage
from page_objects.login_page.login_page import LoginPage
from page_objects.logout_page.logout_page import LogoutPage

test_urls = [
    MAIN_PAGE,
    f"{MAIN_PAGE}/create",
    f"{MAIN_PAGE}/entry/1",
    f"{MAIN_PAGE}/entry/1/update",
    f"{MAIN_PAGE}/entry/1/delete",
]


def test_login_page_loads_up(driver):
    """
    Checking if server is alive
    """
    login_page = LoginPage(driver, url=MAIN_PAGE).open()
    login_page.wait_for_page_to_load(timeout=5)
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")


@mark.parametrize("url", test_urls)
def test_login_required(driver, url):
    """
    If user didn't log in first, any diary page visit should be redirected to the login page
    """
    page = DiaryPage(driver, url=url).open()
    login_page = LoginPage(driver)

    login_page.wait_for_page_to_load(timeout=5)  # we expect a login page to be displayed
    assert_that(page.is_page_displayed() is False, f"URL: {url} is not redirecting to login page")

    assert_that(login_page.is_page_displayed(), "Login page is not displayed")


def test_diary_page_login_logout(driver):
    """
    Verifying that:
    - logging in is not broken
    - main page is displayed
    - logging in is required after logging out
    """
    login_page = LoginPage(driver, MAIN_PAGE).open()
    login_page.wait_for_page_to_load(5)
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")

    login_page.username.value = "admin"
    login_page.password.value = "1amp1amp"
    login_page.log_in.click()

    diary_page = DiaryPage(driver)
    diary_page.wait_for_page_to_load(5)
    assert_that(diary_page.is_page_displayed(), "Diary main page is not displayed")
    assert_that(diary_page.log_out.is_displayed(), "Logout link not displayed")

    diary_page.log_out.click()

    logout_page = LogoutPage(driver)
    logout_page.wait_for_page_to_load(5)
    assert_that(logout_page.is_page_displayed(), "Logout page is not displayed")

    diary_page.open(MAIN_PAGE)
    login_page.wait_for_page_to_load(5)  # we expect a login page to be displayed
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")
