from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.DEBUG)

class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 显示等待定位单个元素
    def show_wait_find_element(self, *loc):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*loc))
        except Exception as msg:
            logging.info(msg)
            return None

    # 显示等待等位多个元素
    def show_wait_find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(*loc))
        except Exception as msg:
            logging.info(msg)
            return None

    def get_size(self):
        location = self.driver.get_window_size()
        width = location['width']
        height = location['height']
        return width, height

