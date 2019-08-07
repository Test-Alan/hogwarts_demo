from po_study.pages.base_page import BasePage


class ProfilePage(BasePage):

    _editor_link = ("css", ".js_edit")        # 编辑
    _disable_enable_link = ("css", ".js_disable")      # 禁用/启用
    _delete_link = ("css", ".js_del_member")   # 删除
    _invite_link = ("css", ".member_display_cover_detail_inviteBtn")    # 邀请
    _submit_link = ("link_text", "确认")        # 确认

    def update(self):
        self.find_element(*self._editor_link).click()

    def disable(self):
        self.find_element(*self. _disable_enable_link).click()
        self.find_element(*self._submit_link).click()

    def enable(self):
        self.find_element(*self. _disable_enable_link).click()

    def delete(self):
        self.find_element(*self._delete_link).click()
        self.find_element(*self._submit_link).click()

    def invite(self):
        self.find_element(*self._invite_link).click()
        self.find_element(*self._submit_link).click()

    # 提示
    def get_tips(self):
        return self.find_element("id", "js_tips").text