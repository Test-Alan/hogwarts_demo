import allure
import pytest
from po_study.pages.contact_page import ContactPage
from po_study.tests.driver import Driver


@allure.feature("第十期_Selenium PO 与企业微信实战_20190804课后作业-添加成员")
class TestContact: 

    @classmethod
    def setup_class(cls):
        cls.driver = Driver().login()
        cls.contact_page = ContactPage(cls.driver)
        cls.contact_page.click_contact_nav()
    @pytest.mark.parametrize('data', [
        ({
            "username":  "张三",
            "english_name":  "zhangsan",
            "acctid":  "tester_0000001",
            "gender":  "2",
            "phone":  "13912345678",
            "telephone":  "12345678",
            "mail":  "1234567@qq.com",
            "address":  "上海市",
            "position":  "测试开发",
            "identity":  "1",
            "extern_position_set":  "custom", "custom_data":  "测试",
            "sendInvite":  "1"

        }),
        ({
            "username":  "李四",
            "english_name":  "lisi",
            "acctid":  "tester_0000002",
            "phone":  "13912345679",

        }),

    ])
    @pytest.mark.run(order=1)
    @allure.story("测试添加成员")
    def test_add_member(self, data):
        self.contact_page.add_member()
        self.contact_page.save_member(data)
        assert self.contact_page.get_tips("保存成功") == "保存成功"

    @pytest.mark.parametrize('data', [
        ({
            "username":  "王五",

        }),

    ])
    @pytest.mark.run(order=2)
    @allure.story("测试更新成员信息")
    def test_update_member(self, data):
        self.contact_page.search("张三").update()
        self.contact_page.save_member(data)
        assert self.contact_page.get_tips("保存成功") == "保存成功"

    @pytest.mark.run(order=3)
    @allure.story("测试成员禁用")
    def test_disable(self):
        self.contact_page.search("王五").disable()
        assert self.contact_page.get_tips("禁用成功") == "禁用成功"

    @pytest.mark.run(order=4)
    @allure.story("测试成员启用")
    def test_enable(self):
        self.contact_page.search("王五").enable()
        assert self.contact_page.get_tips("启用成功") == "启用成功"

    @pytest.mark.run(order=5)
    @allure.story("测试删除成员")
    def test_delete(self):
        self.contact_page.search("王五").delete()
        assert self.contact_page.get_tips("删除成功") == "删除成功"

