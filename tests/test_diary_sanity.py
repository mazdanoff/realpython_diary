# runserver fixture
from hamcrest import assert_that

from conf.urls import LOGIN_PAGE
from page_objects.login_page.login_page import LoginPage


def test_login_page_loads_up(driver):
    login_page = LoginPage(driver).open(LOGIN_PAGE)
    login_page.wait_for_page_to_load(timeout=5)
    assert_that(login_page.is_page_displayed(), "Login page is not displayed")


def test_login_required():
    # try displaying any other page (create, read, update, delete)
    # check if login page displayed
    pass


def test_diary_page_login_logout():
    # load up page
    # check if displayed
    # enter admin:pass
    # click login
    # check if diary displayed
    # click logout
    # check if logged out page is displayed
    pass

