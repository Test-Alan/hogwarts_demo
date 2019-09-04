from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from po_appium_test.pages.base import Page


class StockPage(Page):

    snb_tip_wrapper = Page.by_location(_id="com.xueqiu.android:id/snb_tip_wrapper")      # 浮层
    delete = Page.by_location(xpath="//*[@text='删除']")  # 删除自选股
    message = Page.by_location(xpath="//*[@text='已从自选删除']")     # 删除成功提示
    stock_list = Page.by_location(_id="com.xueqiu.android:id/portfolio_stockName")   # 自选列表
    optional_tab = Page.by_location(xpath="//*[contains(@resource-id, 'tab_name') and @text='自选']")  # 自选tab

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

    # 点击取消浮层
    def press_cancel_supernatant(self):
        try:
            if self.show_wait_find_element(self.snb_tip_wrapper):
                width, height = self.get_size()
                TouchAction(self.driver).press(x=width * 0.5, y=height * 0.5).release().perform()
        except:
            pass