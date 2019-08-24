
from po_selenium_test.pages.base_page import BasePage


class ProfilePage(BasePage):

    _editor_link = ("css", ".js_edit")                # 编辑
    _disable_link = ("css", "a.qui_btn.ww_btn.js_disable")      # 禁用
    _enable_link = ("css", "a.qui_btn.ww_btn.js_disable")      # 启用
    _delete_link = ("css", "a.qui_btn.ww_btn.js_del_member")         # 删除
    _invite_link = ("css", ".member_display_cover_detail_inviteBtn")    # 邀请
    _submit_link = ("css", '[d_ck="submit"]')        # 确认
    _tips = ("id", "js_tips")


    # 编辑成员
    def update(self):
        self.find_element(*self._editor_link).click()

    # 禁用成员
    def disable(self):
        print("关闭")
        self.find_element(*self. _disable_link).click()
        self.find_element(*self._submit_link).click()

    # 启用成员
    def enable(self):
        print("打开")
        self.find_element(*self. _enable_link).click()

    # 删除成员
    def delete(self):
        delete_element = self.find_element(*self._delete_link)
        self.run_script("arguments[0].click();", delete_element)
        self.find_element(*self._submit_link).click()

    # 邀请成员
    def invite(self):
        self.find_element(*self._invite_link).click()
        self.find_element(*self._submit_link).click()

    # 提示
    def get_tips(self, tips):
        return self.tips_text_in_element(*self._tips, tips=tips)