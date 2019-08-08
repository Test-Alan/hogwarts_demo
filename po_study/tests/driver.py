from selenium import webdriver
from po_study.pages.base_page import BasePage

class Driver:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "safari":
            self.driver = webdriver.Safari()
        else:
            raise ValueError("browser parameter error")
        # 最大窗口
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login(self):
        cookies = {
            "xxx": "xxx",
            "xxx": "xxx",
            "xxx": "xxx",
        }
        page = BasePage(self.driver)
        page.get("https://work.weixin.qq.com/wework_admin/frame", cookies=cookies)
        return self.driver

    def quit(self):
        self.driver.quit()
