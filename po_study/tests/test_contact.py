import allure
import pytest


@allure.feature("第十期_Selenium PO 与企业微信实战_20190804课后作业")
class TestContact:

    @allure.story("测试添加成员")
    def test_add_user(self, Page, data):
        Page.click_contact_nav()
        Page.add_user()
        Page.save_user(data)
        assert Page.get_tips() == "保存成功"

    @pytest.mark.parametrize('data', [
        ({
            "username": "王五",

        }),

    ])
    @allure.story("测试更新成员信息")
    def test_update_user(self, data):
        self.contact_page.search("张三").update()
        self.contact_page.save_user(data)
        assert self.contact_page.get_tips() == "保存成功"