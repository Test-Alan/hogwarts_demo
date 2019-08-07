import sys
import os
from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

class Driver:

    def browser(self, browser="chrome"):
        if browser == "chrome":
            driver_path = BASE_DIR + '/webdriver/chromedriver'
            self.driver = webdriver.Chrome(driver_path)
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
        return self.driver

    def quit(self):
        self.driver.quit()
