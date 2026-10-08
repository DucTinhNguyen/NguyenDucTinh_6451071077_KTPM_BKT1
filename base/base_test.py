from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BaseTest:
    @staticmethod
    def create_driver() -> WebDriver:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        return driver
