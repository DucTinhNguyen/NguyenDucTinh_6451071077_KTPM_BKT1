from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    REMEMBER_ME = (By.ID, "persistent")
    REMEMBER_ME_CONTROL = (By.CSS_SELECTOR, "label.check[for='persistent']")
    SUBMIT = (By.CSS_SELECTOR, "form[action='/Login'] input[type='submit']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/Login/GetPass']")
    UTC_EMAIL_LOGIN = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'Đăng nhập bằng e-mail UTC')]",
    )
    LOGIN_FORM = (By.CSS_SELECTOR, "form[action='/Login']")
    REDIRECT = (By.CSS_SELECTOR, "form[action='/Login'] input[name='r']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def wait_until_loaded(self) -> None:
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.USERNAME)
        )

    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)
