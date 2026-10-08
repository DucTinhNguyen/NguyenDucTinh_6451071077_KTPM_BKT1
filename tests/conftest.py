import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.login_page import LoginPage


@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def login_page(browser):
    url = os.environ.get(
        "LOGIN_URL",
        "https://vanphongdientu.utc.edu.vn/Login?r=https%3A%2F%2Fvanphongdientu.utc.edu.vn%2F",
    )
    browser.get(url)
    WebDriverWait(browser, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    page = LoginPage(browser)
    page.wait_until_loaded()
    return page
