import pytest
from hamcrest import assert_that

from conf.urls import *
from page_objects.diary_page.diary_page import DiaryPage
from page_objects.login_page.login_page import LoginPage

test_urls = [
    MAIN_PAGE,
    f"{MAIN_PAGE}/create",
    f"{MAIN_PAGE}/entry/1",
    f"{MAIN_PAGE}/entry/1/update",
    f"{MAIN_PAGE}/entry/1/delete",
]


def test_login_page_loads_up(driver):
    login_page = LoginPage(driver).open(LOGIN_PAGE)
    login_page.wait_for_page_to_load(timeout=5)
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")


@pytest.mark.parametrize("url", test_urls)
def test_login_required(driver, url):
    """
    Visiting any diary page should redirect to login page
    if user didn't log in first
    """
    page = DiaryPage(driver).open(url)
    page.wait_for_page_to_load(timeout=5)
    assert_that(page.is_page_displayed() is False, f"URL: {url} is not redirecting to login page")

    login_page = LoginPage(driver)
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")


def test_diary_page_login_logout():
    # load up page
    # check if displayed
    # enter admin:pass
    # click login
    # check if diary displayed
    # click logout
    # check if logged out page is displayed
    pass

