from po_appium_test.pages.base import Page


class LoginPage(Page):
    user_profile_icon = Page.by_location(_id='com.xueqiu.android:id/user_profile_icon')  # 用户配置
    iv_login_more = Page.by_location(_id="com.xueqiu.android:id/login_more")  # 更多登录
    login_account = Page.by_location(_id="com.xueqiu.android:id/login_account")  # 用户名
    login_password = Page.by_location(_id="com.xueqiu.android:id/login_password")  # 密码
    button_next = Page.by_location(_id="com.xueqiu.android:id/button_next")  # 登录按钮
    md_content = Page.by_location(_id="com.xueqiu.android:id/md_content")  # 提示
    md_buttonDefaultPositive = Page.by_location(_id="com.xueqiu.android:id/md_buttonDefaultPositive")  # 确认

    # 去到登录页面
    def go_to_phone_login(self):
        self.show_wait_find_element(self.user_profile_icon).click()
        self.show_wait_find_element(self.iv_login_more).click()

    # 输入手机号密码
    def send_phone_password(self, phone, password):
        phone_elm = self.show_wait_find_element(self.login_account)
        phone_elm.clear()
        phone_elm.send_keys(phone)

        password_elm = self.show_wait_find_element(self.login_password)
        password_elm.clear()
        password_elm.send_keys(password)
        self.show_wait_find_element(self.button_next).click()

    # 获取提示框text
    def get_prompt_text(self):
        text = self.show_wait_find_element(self.md_content).text
        self.show_wait_find_element(self.md_buttonDefaultPositive).click()
        return text

