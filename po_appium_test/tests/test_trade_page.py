from time import sleep

from po_appium_test.driver import driver
from po_appium_test.pages.trade_page import TradePage


class TestTrade:
    # 初始化
    @classmethod
    def setup_class(cls):
        cls.driver = driver()
        cls.trade_page = TradePage(cls.driver)


    # 结束
    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()

    def test_a(self):
        self.trade_page.click_reade()