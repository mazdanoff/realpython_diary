from pytest import fixture
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxService

from conf.paths import geckodriver_exe
from utils.db_conn_handler import DatabaseConnectionHandler


@fixture
def driver():
    """Sets up the driver to operate the browser automatically."""
    options = FirefoxOptions()
    options.add_argument("--headless")
    service = FirefoxService(executable_path=geckodriver_exe)
    firefox = Firefox(options=options, service=service)
    firefox.maximize_window()
    yield firefox
    firefox.close()
    firefox.quit()


@fixture(scope="session")
def database():
    """Yields a db connection, useful to set up data for tests and cleanup afterward."""
    db_conn_handler = DatabaseConnectionHandler()
    yield db_conn_handler


def pytest_addoption(parser):
    """Retrieve credentials from an ini file."""
    # would probably be better to store these in env variables in a real setting
    parser.addini('username', help='Used to log in to diary')
    parser.addini('password', help='Used to log in to diary')
