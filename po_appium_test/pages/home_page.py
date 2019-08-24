# coding=utf-8
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from po_appium_test.pages.base import Page


class HomePage(Page):
    iamge_cancel = (By.ID, "image_cancel")
    home_search = (By.ID, "com.xueqiu.android:id/home_search")  # 搜索框
    search_input_text = (By.ID, "com.xueqiu.android:id/search_input_text")  # 搜索文本框
    name = (By.ID, "com.xueqiu.android:id/name")    # 匹配列表
    stock_name = (By.ID, "com.xueqiu.android:id/stockName")     # 搜索结果
    action_close = (By.ID, "com.xueqiu.android:id/action_close")    # 取消

    optional_tab = (By.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='自选']")     # 自选tab

    xue_qiu_tab = (By.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='雪球']")      # 雪球tab
    negative = (By.ID, "com.xueqiu.android:id/md_buttonDefaultNegative")    # 评价提示框
    snb_tip_wrapper = (By.ID, "com.xueqiu.android:id/snb_tip_wrapper")      # 浮层

    delete = (By.XPATH, "//*[@text='删除']")  # 删除自选股
    message = (By.XPATH, "//*[@text='已从自选删除']")     # 删除成功提示
    stock_list = (By.ID, "com.xueqiu.android:id/portfolio_stockName")   # 自选列表
    # 加自选
    def follow_btn(self, stock_type):
        return (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
                            "//*[contains(@resource-id, 'follow_btn')]")

    # 已添加
    def followed_btn(self, stock_type):
        return (By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='" + stock_type + "']/../../.."
                              "//*[contains(@resource-id, 'followed_btn')]")

    # 判断是否提示更新
    def cancel_update(self):
        elm = self.show_wait_find_element(self.iamge_cancel)
        if elm:
            elm.click()

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

    # 获取自选股text
    def get_stock_name(self, index):
        return self.show_wait_find_elements(self.stock_list)[index].text

    # 删除自选股
    def delete_optional(self, index):
       elm = self.show_wait_find_elements(self.stock_list)[index]
       TouchAction(self.driver).long_press(el=elm, duration=3000).release().perform()
       self.show_wait_find_element(self.delete).click()

    # 去到自选页面
    def go_to_optional(self, timeout=5):
        width, height = self.get_size()
        xd_x = (209 / 750) * width + (209 / 750) * (width - 750)
        xd_y = (1304 / 1334) * height + (1304 / 1334) * (height - 1334)
        offset_x = xd_x - 209
        offset_y = xd_y - 1304
        for i in range(timeout):
            if (offset_x < 2 or offset_x > -2) and (offset_y < 2 or offset_y > -2):
                self.show_wait_find_element(self.optional_tab).click()
                break
            else:
                sleep(1)

    # 去到雪球页面
    def go_to_xue_qiu(self):
        self.show_wait_find_element(self.xue_qiu_tab).click()

    # 点击取消浮层
    def press_cancel_supernatant(self):
        try:
            if self.show_wait_find_element(self.snb_tip_wrapper):
                width, height = self.get_size()
                TouchAction(self.driver).press(x=width * 0.5, y=height * 0.5).release().perform()
        except:
            pass