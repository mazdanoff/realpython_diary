import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DRIVERS_DIR = os.path.join(PROJECT_PATH, "drivers")
GECKODRIVER = os.path.join(DRIVERS_DIR, "geckodriver.exe")
