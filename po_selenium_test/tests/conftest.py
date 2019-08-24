import time

import pytest
from selenium import webdriver

cookies = {
    "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9",
    "wwrtx.i18n_lan": "zh-cn",
    "_ga": "GA1.2.1433189943.1565267279",
    "_gid": "GA1.2.477060706.1565445192",
    "wwrtx.ref": "direct",
    "wwrtx.refid": "3885476261061215",
    "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d": "1565315922,1565612217,1565445192,1565489863",
    "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d": "1565489863",
    "wwrtx.d2st": "a3809524",
    "wwrtx.sid": "fuRcYhZmS48cZPCtZjGO5wfLdeosmScaS7VDTL79Du6wdNh9Wf_GcUTb76yLrnI1",
    "wwrtx.ltype": "1",
    "wxpay.corpid": "1970325081082440",
    "wxpay.vid": "1688853073376133",
    "wwrtx.vst": "bibRHY6dbBxy19I2A1QkspIAC6bGj3n4Aimmg3zDm30d2_kxvo9XrGjxDv6gG0MseAPMQz3tklSrhDY7QWudPLS3kftd7Gg7aD_TQrs054R-Zi_zcWaJeo3sjzknaD79m2J7QJs0bbWkrV0eM2vx9k9uaRkZQ9v8g8lcICnC5wtcy7XLXoPfyzJEedxhF_DD4jwp7LCTpDxp3kZwV1uxa6OrcSSBbKBBL_77Kgl2qR6decbIx_mjXeCpIkOK70K1s6bUGyzJ4gKcbHRAxDR6OA",
    "wwrtx.vid": "1688853073376133",
    "wwrtx.logined": "true",
    "_gat": "1",
}

url = "https://work.weixin.qq.com/wework_admin/frame"
# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser(driver_type="chrome"):
    """
    全局定义浏览器驱动
    :return:
    """
    global driver

    if driver_type == "chrome":
        driver = webdriver.Chrome("/usr/local/Cellar/python/3.7.3/bin/chromedriver")
    elif driver_type == "firefox":
        driver = webdriver.Firefox()
    elif driver_type == "ie":
        driver = webdriver.Ie()
    elif driver_type == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("driver_type parameter error")
    # 最大窗口
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    if cookies:
        for k, v in cookies.items():
            driver.add_cookie({"name": k, "value": v})
    driver.get(url)


    return driver

# 关闭浏览器
# @pytest.fixture(scope="session", autouse=True)
# def driver_type_close():
#     yield driver
#     driver.quit()
#     time.sleep(2)
#     print("test end!")