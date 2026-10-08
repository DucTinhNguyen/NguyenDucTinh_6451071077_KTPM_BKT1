import os
from collections.abc import Iterator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from base.base_test import BaseTest
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def browser() -> Iterator[WebDriver]:
    driver = BaseTest.create_driver()
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def login_page(browser: WebDriver) -> LoginPage:
    url = os.environ.get(
        "LOGIN_URL",
        "https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F",
    )
    page = LoginPage(browser)
    page.open(url)
    WebDriverWait(browser, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    page.wait_until_loaded()
    return page
