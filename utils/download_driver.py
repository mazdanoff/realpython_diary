import json
import requests
from zipfile import ZipFile

from conf.urls import GECKODRIVER_URL
from conf.paths import drivers_dir, geckodriver_zip

def download_gecko_driver():
    response = requests.get(GECKODRIVER_URL, stream=True)

    with open(geckodriver_zip, mode="wb") as file:
        for chunk in response.iter_content(chunk_size=10 * 1024): # 10 kilobytes
            file.write(chunk)

    with ZipFile(geckodriver_zip, "r") as zipped_driver:
        zipped_driver.extractall(drivers_dir)

if __name__ == '__main__':
    download_gecko_driver()
