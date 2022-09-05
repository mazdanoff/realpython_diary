from pytest import fixture
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions

from conf.paths import GECKODRIVER
from conf.urls import MAIN_PAGE
from page_objects.diary_page.main_page.main_page import MainPage
from page_objects.login_page.login_page import LoginPage
from page_objects.logout_page.logout_page import LogoutPage


@fixture
def driver():
    options = FirefoxOptions()
    firefox = Firefox(options=options, executable_path=GECKODRIVER)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()


@fixture
def separate_session(driver, request):
    """
    To handle each test case in separate session.
    If something goes awry, text next test case will still be in a separate session.
    """
    login_page = LoginPage(driver, MAIN_PAGE).open()
    main_page = MainPage(driver)
    logout_page = LogoutPage(driver)

    login_page.username.value = request.config.getini('username')
    login_page.password.value = request.config.getini('password')
    login_page.log_in.click()
    main_page.wait_for_page_to_load(5)
    yield
    main_page.log_out.click()
    logout_page.wait_for_page_to_load(5)


def pytest_addoption(parser):
    parser.addini('username', help='Used to log in to diary')
    parser.addini('password', help='Used to log in to diary')
