from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from po_appium_test.pages.base import Page


class TradePage(Page):

    reade_tab = Page.by_location(xpath="//*[contains(@resource-id, 'tab_name') and @text='交易']")

    def click_reade(self):
        print("1111111", self.reade_tab)
        self.show_wait_find_element(self.reade_tab).click()
