from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def click(self, locator: Locator) -> None:
        self._wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: Locator, text: str) -> None:
        element = self._wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self._wait.until(EC.visibility_of_element_located(locator)).text

    def get_attribute(self, locator: Locator, attribute: str) -> str | None:
        return self._driver.find_element(*locator).get_attribute(attribute)

    def is_displayed(self, locator: Locator) -> bool:
        return self._driver.find_element(*locator).is_displayed()

    def is_enabled(self, locator: Locator) -> bool:
        return self._driver.find_element(*locator).is_enabled()

    def is_selected(self, locator: Locator) -> bool:
        return self._driver.find_element(*locator).is_selected()

    def get_title(self) -> str:
        return self._driver.title

    def get_current_url(self) -> str:
        return self._driver.current_url

    def open(self, url: str) -> None:
        self._driver.get(url)
