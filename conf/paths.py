import os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

drivers_dir = os.path.join(project_path, "drivers")
geckodriver_zip = os.path.join(drivers_dir, "geckodriver.zip")
geckodriver_exe = os.path.join(drivers_dir, "geckodriver.exe")

database_path = os.path.join(project_path, "db.sqlite3")
