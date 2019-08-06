import logging
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,

}


class BasePage:

    def __init__(self, driver: WebDriver, url=None):
        self._driver = driver
        self.root_uri = url if url else getattr(self._driver, 'url', None)

    def get(self, uri, cookies=None):
        root_uri = self.root_uri or ''
        self._driver.get(root_uri + uri)
        if cookies:
            for k, v in cookies.items():
                self._driver.add_cookie({"name": k, "value": v})
            self._driver.get(root_uri + uri)




    def run_script(self, js=None):
        if js is None:
            raise ValueError("Please input js script")
        else:
            self.driver.execute_script(js)

    # 定位单个元素
    def find_element(self, locator, value=None, timeout=5):

        try:
            timeout_int = int(timeout)
        except TypeError:
            raise ValueError("Type 'timeout' error, must be type int() ")
        for i in range(timeout_int):
            if value is None:
                if not locator:
                    raise ValueError("Please specify a locator")
                self.k, self.v = locator
                try:
                    self.locator = (LOCATOR_LIST[self.k], self.v)
                except KeyError:
                    raise KeyError(
                        "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
                elm = self._driver.find_element(*self.locator)
            else:
                elm = self._driver.find_element(LOCATOR_LIST[locator], value)
            if elm is not None:
                if elm.is_displayed() is True:
                    break
                else:
                    sleep(1)
            else:
                sleep(1)
        else:
            raise TimeoutError("Timeout, element invisible")
        return elm

    # 定位多个元素
    def find_elements(self, locator, value=None, timeout=5):

        try:
            timeout_int = int(timeout)
        except TypeError:
            raise ValueError("Type 'timeout' error, must be type int() ")
        for i in range(timeout_int):
            if value is None:
                if not locator:
                    raise ValueError("Please specify a locator")
                self.k, self.v = locator
                try:
                    self.locator = (LOCATOR_LIST[self.k], self.v)
                except KeyError:
                    raise KeyError(
                        "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
                elm = self._driver.find_elements(*self.locator)
            else:
                elm = self._driver.find_elements(LOCATOR_LIST[locator], value)
            if elm is not None:
                if elm.is_displayed() is True:
                    break
                else:
                    sleep(1)
            else:
                sleep(1)
        else:
            raise TimeoutError("Timeout, element invisible")
        return elm
