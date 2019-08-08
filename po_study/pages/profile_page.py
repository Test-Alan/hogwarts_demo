from po_study.pages.base_page import BasePage


class ProfilePage(BasePage):

    _editor_link = ("css", ".js_edit")        # 编辑
    _disable_enable_link = ("css", ".js_disable")      # 禁用/启用
    _delete_link = ("css", ".js_del_member")   # 删除
    _invite_link = ("css", ".member_display_cover_detail_inviteBtn")    # 邀请
    _submit_link = ("link_text", "确认")        # 确认
    _tips = ("id", "js_tips")

    # 编辑成员
    def update(self):
        self.find_element(*self._editor_link).click()

    # 禁用成员
    def disable(self):
        self.find_element(*self. _disable_enable_link).click()
        self.find_element(*self._submit_link).click()

    # 启用成员
    def enable(self):
        self.find_element(*self. _disable_enable_link).click()

    # 删除成员
    def delete(self):
        self.find_element(*self._delete_link).click()
        self.find_element(*self._submit_link).click()

    # 邀请成员
    def invite(self):
        self.find_element(*self._invite_link).click()
        self.find_element(*self._submit_link).click()

