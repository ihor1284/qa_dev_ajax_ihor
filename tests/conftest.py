import subprocess
import time

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server(request) -> None:
    process = subprocess.Popen(
        [
            'appium',
            '-a',
            '0.0.0.0',
            '-p',
            '4723',
            '--allow-insecure',
            'adb_shell'
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server: None) -> WebDriver:
    driver = webdriver.Remote(
        'http://localhost:4723', desired_capabilities=android_get_desired_capabilities()
    )
    yield driver
    driver.quit()
