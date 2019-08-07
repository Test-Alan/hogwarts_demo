import logging
import time
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # 执行js
    def run_script(self, js=None):
        if js is None:
            raise ValueError("Please input js script")
        else:
            self._driver.execute_script(js)

     # 定位单个元素
    def find_element(self, locator, value, timeout=10):

        try:
            try:
                timeout_int = int(timeout)
            except TypeError:
                raise ValueError("Type 'timeout' error, must be type int() ")
            try:
                locator = LOCATOR_LIST[locator]
            except KeyError:
                raise KeyError(
                    "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
            element = WebDriverWait(self._driver, timeout_int).until(
                EC.presence_of_element_located((locator, value)))
            if element:
                return self._driver.find_element(locator, value)

        except:
            for i in range(timeout_int):
                element = self._driver.find_element(locator, value)
                if element.is_displayed() is True:
                    return element
                else:
                    sleep(1)

            else:

                # 截图
                self.screenshot()
                # 记录日志
                logger.info("timeout, element {} not found!".format(value))

    # 定位多个元素
    def find_elements(self, locator, value, timeout=5):

        try:
            try:
                timeout_int = int(timeout)
            except TypeError:
                raise ValueError("Type 'timeout' error, must be type int() ")
            try:
                locator = LOCATOR_LIST[locator]
            except KeyError:
                raise KeyError(
                    "Please use a locator：'id_'、'name'、'class_name'、'css'、'xpath'、'link_text'、'partial_link_text'.")
            element = WebDriverWait(self._driver, timeout_int).until(
                EC.presence_of_all_elements_located((locator, value)))
            if element:
                return self._driver.find_elements(locator, value)

        except:
            # 截图
            self.screenshot()
            # 记录日志
            logger.info("timeout, element {} not found!".format(value))

    # 点击单选按钮
    def radio_checked(self, radio_name, radio_value):
        try:
            for element in radio_name:
                value = str(element.get_attribute("value"))
                if value == radio_value:
                    return element
        except Exception as msg:
            return logging.info(msg)

    # 截图
    def screenshot(self, name="对象未找到的截图"):
        new_name = name + time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + ".jpg"
        img_path = '../images/' + new_name
        return self._driver.get_screenshot_as_file(img_path)

    def alert_accept(self):
        alert = self._driver.switch_to.alert
        alert.accept()

