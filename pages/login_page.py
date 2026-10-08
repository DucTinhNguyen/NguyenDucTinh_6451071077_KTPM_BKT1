from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage, Locator


class LoginPage(BasePage):
    _USERNAME: Locator = (By.NAME, "username")
    _PASSWORD: Locator = (By.NAME, "userpwd")
    _REMEMBER_ME: Locator = (By.ID, "persistent")
    _REMEMBER_ME_CONTROL: Locator = (By.CSS_SELECTOR, "label.check[for='persistent']")
    _SUBMIT: Locator = (By.CSS_SELECTOR, "form[action='/Login'] input[type='submit']")
    _FORGOT_PASSWORD: Locator = (By.CSS_SELECTOR, "a[href='/Login/GetPass']")
    _UTC_EMAIL_LOGIN: Locator = (
        By.XPATH,
        "//a[contains(normalize-space(.), 'Đăng nhập bằng e-mail UTC')]",
    )
    _LOGIN_FORM: Locator = (By.CSS_SELECTOR, "form[action='/Login']")
    _REDIRECT: Locator = (By.CSS_SELECTOR, "form[action='/Login'] input[name='r']")
    _HEADING: Locator = (By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def wait_until_loaded(self) -> None:
        self._wait.until(EC.visibility_of_element_located(self._USERNAME))

    def is_on_login_page(self) -> bool:
        return "/Login" in self.get_current_url()

    def get_heading(self) -> str:
        return self.get_text(self._HEADING)

    def get_username_type(self) -> str | None:
        return self.get_attribute(self._USERNAME, "type")

    def get_username_placeholder(self) -> str | None:
        return self.get_attribute(self._USERNAME, "placeholder")

    def enter_username(self, username: str) -> None:
        self.type_text(self._USERNAME, username)

    def get_username_value(self) -> str | None:
        return self.get_attribute(self._USERNAME, "value")

    def get_password_type(self) -> str | None:
        return self.get_attribute(self._PASSWORD, "type")

    def get_password_placeholder(self) -> str | None:
        return self.get_attribute(self._PASSWORD, "placeholder")

    def enter_password(self, password: str) -> None:
        self.type_text(self._PASSWORD, password)

    def get_password_value(self) -> str | None:
        return self.get_attribute(self._PASSWORD, "value")

    def get_remember_me_type(self) -> str | None:
        return self.get_attribute(self._REMEMBER_ME, "type")

    def is_remember_me_selected(self) -> bool:
        return self.is_selected(self._REMEMBER_ME)

    def toggle_remember_me(self) -> None:
        self.click(self._REMEMBER_ME_CONTROL)

    def is_submit_displayed(self) -> bool:
        return self.is_displayed(self._SUBMIT)

    def is_submit_enabled(self) -> bool:
        return self.is_enabled(self._SUBMIT)

    def get_submit_text(self) -> str | None:
        return self.get_attribute(self._SUBMIT, "value")

    def get_form_method(self) -> str | None:
        return self.get_attribute(self._LOGIN_FORM, "method")

    def get_form_action_path(self) -> str:
        action = self.get_attribute(self._LOGIN_FORM, "action")
        return urlparse(action or "").path

    def get_redirect_input_type(self) -> str | None:
        return self.get_attribute(self._REDIRECT, "type")

    def get_redirect_value(self) -> str | None:
        return self.get_attribute(self._REDIRECT, "value")

    def is_forgot_password_displayed(self) -> bool:
        return self.is_displayed(self._FORGOT_PASSWORD)

    def get_forgot_password_path(self) -> str:
        href = self.get_attribute(self._FORGOT_PASSWORD, "href")
        return urlparse(href or "").path

    def is_utc_email_login_displayed(self) -> bool:
        return self.is_displayed(self._UTC_EMAIL_LOGIN)

    def get_utc_email_login_text(self) -> str:
        return self.get_text(self._UTC_EMAIL_LOGIN)

    def get_utc_email_login_host(self) -> str | None:
        href = self.get_attribute(self._UTC_EMAIL_LOGIN, "href")
        return urlparse(href or "").hostname
