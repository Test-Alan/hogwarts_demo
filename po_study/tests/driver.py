from selenium import webdriver


class Driver:

    def browser(self, browser="chrome"):
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
        return self.driver

    def quit(self):
        self.driver.quit()

