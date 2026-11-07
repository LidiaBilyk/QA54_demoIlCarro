from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click_element(self, locator, timeout=10):
        # For a click, it's more reliable to wait for clickability, not just visibility.
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def check_alert_text(self, text, timeout=10):
        alert = WebDriverWait(self.driver, timeout).until(
           EC.alert_is_present()
        )
        return alert.text == text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()