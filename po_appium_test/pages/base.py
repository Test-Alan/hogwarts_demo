from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.DEBUG)


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 黑名单，用来处理一些不定时的弹框。
        self.black_list = [(By.ID, "image_cancel")]
        # 限制查找次数
        self.count = 0

    # 显示等待定位单个元素
    def show_wait_find_element(self, *loc):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*loc))

        except Exception as msg:
            if self.count > 2:
                raise ("查找黑名单中元素已经超过最大次数!")
            self.count += 1
            print("count=", self.count)
            # 判断黑名单元素是否出现
            for black in self.black_list:
                black_elements = self.driver.find_elements(*black)
                if len(black_elements) >= 1:
                    black_elements[0].click()
                    logging.info("找到黑名单{}元素，已点击!".format(black))

                else:
                    logging.info("未找到黑名单{}元素!".format(black))
            else:
                return self.show_wait_find_element(*loc)

        else:
            return element

    # 显示等待等位多个元素
    def show_wait_find_elements(self, *loc):
        try:
            elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(*loc))
        except Exception as msg:
            logging.info(msg)
            return []
        else:
            return elements

    def get_size(self):
        location = self.driver.get_window_size()
        width = location['width']
        height = location['height']
        return width, height

    @classmethod
    def by_location(cls, **kwargs):
        try:
            print("22222222", kwargs)
            k, v = list(kwargs.items())[0]
            k = k.lower()
            if k == "_id":
                location = (By.ID, v)
            elif k == "class_name":
                location = (By.CLASS_NAME, v)
            elif k == "xpath":
                location = (By.XPATH, v)
        except Exception as e:
            logging.info(e)
        else:
            print("33333333333333", location)
            return location