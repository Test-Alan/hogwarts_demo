from appium import webdriver
import yaml
def driver():
    caps = {}
    caps["platformName"] = "android"
    caps["deviceName"] = "mumu"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps["autoGrantPermissions"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(20)
    return driver

