import time

from po_study.pages.base_page import BasePage
from po_study.pages.manage_tools_page import ManageTools
from po_study.pages.profile_page import ProfilePage


class ContactPage(BasePage):

    _contact_nav = ("xpath", '//*[@id="menu_contacts"]/span')                     # 导航栏
    _add_member_but = ("link_text", "添加成员")     # 添加成员
    _username_input = ("id", "username")                                             # 姓名
    _english_name_input = ("id", "memberAdd_english_name")                           # 别名
    _acctid_input = ("id", "memberAdd_acctid")                                       # 账号
    _gender_radio = ("name", "gender")                                               # 性别
    _phone_input = ("id", "memberAdd_phone")                                         # 手机
    _telephone_input = ("id", "memberAdd_telephone")                                 # 座机
    _mail_input = ("id", "memberAdd_mail")                                           # 邮箱
    _address_input = ("id", "memberEdit_address")                                    # 地址
    _position_input = ("id", "memberAdd_title")                                      # 职务
    _identity_stat_radio = ("name", "identity_stat")                                 # 身份
    _extern_position_set_radio = ("name", "extern_position_set")                     # 职务
    _extern_position_input = ("name", "extern_position")                             # 自定义
    _sendInvite_checkbox = ("name", "sendInvite")                                    # 通过邮件或短信发送企业邀请
    _save_but = ("link_text", "保存")                                                 # 保存按钮
    _search_input = ("id", "memberSearchInput")                                       # 搜索
    _tips = ("id", "js_tips")

    def click_contact_nav(self):
        self.find_element(*self._contact_nav).click()

    def add_member(self):
        time.sleep(2)
        self.find_elements(*self._add_member_but)[-1].click()

    # 保存用户信息
    def save_member(self, data):
        if data.get("username"):
            username = self.find_element(*self._username_input)
            username.clear()
            username.send_keys(data.get("username"))

        if data.get("english_name"):
            english_name = self.find_element(*self._english_name_input)
            english_name.clear()
            english_name.send_keys(data.get("english_name"))

        if data.get("acctid"):
            acctid = self.find_element(*self._acctid_input)
            acctid.clear()
            acctid.send_keys(data.get("acctid"))

        if data.get("gender"):

            gender = self.find_elements(*self._gender_radio)
            self.radio_checked(gender, data.get("gender")).click()

        if data.get("phone"):
            phone = self.find_element(*self._phone_input)
            phone.clear()
            phone.send_keys(data.get("phone"))

        if data.get("telephone"):
            telephone = self.find_element(*self._telephone_input)
            telephone.clear()
            telephone.send_keys(data.get("telephone"))

        if data.get("mail"):
            mail = self.find_element(*self._mail_input)
            mail.clear()
            mail.send_keys(data.get("mail"))

        if data.get("address"):
            address = self.find_element(*self._address_input)
            address.clear()
            address.send_keys(data.get("address"))

        if data.get("position"):
            position = self.find_element(*self._position_input)
            position.clear()
            position.send_keys(data.get("position"))

        if data.get("identity"):
            identity_stat = self.find_elements(*self._identity_stat_radio)
            self.radio_checked(identity_stat, data.get("identity")).click()

        if data.get("extern_position_set"):
            extern_position_set = self.find_elements(*self._extern_position_set_radio)
            self.radio_checked(extern_position_set, data.get("extern_position_set")).click()
            if data.get("extern_position_set") == "custom":
                custom_data = self.find_element(*self._extern_position_input)
                custom_data.clear()
                custom_data.send_keys(data.get("custom_data"))

        if data.get("sendInvite"):
            self.find_element(*self._sendInvite_checkbox).click()

        self.find_element(*self._save_but).click()

    # 提示
    def get_tips(self, tips):
        return self.tips_text_in_element(*self._tips, tips=tips)

    # 搜索
    def search(self, key):
        search_input = self._driver.find_element(*self._search_input)
        search_input.clear()
        search_input.send_keys(key)
        return ProfilePage(self._driver)

    def go_to_search_page(self):
        return ProfilePage(self._driver)

    # 管理工具页面
    def go_to_manage_tools_page(self):
        self.find_element("xpath", '//*[@id="menu_manageTools"]/span').click()
        return ManageTools(self._driver)