# coding=utf-8
from selenium.webdriver.common.by import By
from po_appium_test.pages.base import Page


class HomePage(Page):

    home_search = Page.by_location(_id="com.xueqiu.android:id/home_search")  # 搜索框
    search_input_text = Page.by_location(_id="com.xueqiu.android:id/search_input_text")  # 搜索文本框
    name = Page.by_location(_id="com.xueqiu.android:id/name")    # 匹配列表
    stock_name = Page.by_location(_id="com.xueqiu.android:id/stockName")     # 搜索结果
    action_close = Page.by_location(_id="com.xueqiu.android:id/action_close")    # 取消
    xue_qiu_tab = Page.by_location(xpath="//*[contains(@resource-id, 'tab_name') and @text='雪球']")      # 雪球tab
    negative = Page.by_location(_id="com.xueqiu.android:id/md_buttonDefaultNegative")    # 评价提示框

    # 加自选
    def follow_btn(self, stock_type):
        return (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
                            "//*[contains(@resource-id, 'follow_btn')]")

    # 已添加
    def followed_btn(self, stock_type):
        return (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
                              "//*[contains(@resource-id, 'followed_btn')]")

    # 搜索
    def search(self, name, expect):
        self.show_wait_find_element(self.home_search).click()
        self.show_wait_find_element(self.search_input_text).send_keys(name)
        name_list = self.show_wait_find_elements(self.name)
        for itme in name_list:
            if itme.text == expect:
                itme.click()
                break

    # 获取搜索结果text
    def get_search_result(self):
        return self.show_wait_find_element(self.stock_name).text

    # 点击取消按钮
    def click_action_close(self):
        self.show_wait_find_element(self.action_close).click()

    # 点击加自选
    def click_add_optional(self, stock_type):
        self.show_wait_find_element(self.follow_btn(stock_type)).click()
        try:
            elm = self.show_wait_find_element(self.negative)
        except:
            pass
        else:
            elm.click()

    # 获取加自选text
    def get_add_optional_text(self, stock_type):
        return self.show_wait_find_element(self.follow_btn(stock_type)).text

    # 获取已添加text
    def get_added_text(self, stock_type):
        return self.show_wait_find_element(self.followed_btn(stock_type)).text

    # 去到雪球页面
    def go_to_xue_qiu(self):
        self.show_wait_find_element(self.xue_qiu_tab).click()

