import allure
import pytest
from po_study.pages.contact_page import ContactPage
from po_study.tests.driver import Driver

cookies = {
    "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9",
    "wwrtx.i18n_lan": "zh-cn",
    "_ga": "GA1.2.1433189943.1565267279",
    "wwrtx.ref": "direct",
    "wwrtx.refid": "23846621401033848",
    "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d": "1565267279,1565310770,1565315922,1565612217",
    "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d": "1565612217",
    "_gid": "GA1.2.259574219.1565612218",
    "wwrtx.d2st": "a2289299",
    "wwrtx.sid": "fuRcYhZmS48cZPCtZjGO57fJA6NlcQzCbvp4rwQwmEqMKOdU7f50UAqOpmon587_",
    "wwrtx.ltype": "1",
    "wxpay.corpid":"1970325081082440",
    "wxpay.vid": "1688853073376133",
    "wwrtx.vst": "-JeP8OdV96P-8J-HD5HzBnRPlJf6tOrfnfip6FmLBHZmOBclShXsJQLiGtmrki5TA-mqmAGX-RrJUUI6IeRWIdyYc6Br-jx_l6TijCXlMDDdF7gh9v6VpNx7E0Dz83Vdm0bPlm2F3fEtgEasyI6bNSPmGwEv5GwUj8cPDGRPcxWrZ93izu9_0jXe4my2mRt-hXnwmlYmnM73QuTM5ylLPSdzV4KTX7fjYoX3we4EjkuuoGYWfTVSEmTrH3RYSiLdf2vcHPmSSzQUmhpL0Y3jbg",
    "wwrtx.vid": "1688853073376133",
    "wwrtx.logined": "true",
    "_gat": "1",
}


@allure.feature("第十期_Selenium PO 与企业微信实战_20190804课后作业")
class TestContact:

    @classmethod
    def setup_class(cls):
        cls.driver = Driver().browser()
        cls.contact_page = ContactPage(cls.driver)
        cls.contact_page.get("https://work.weixin.qq.com/wework_admin/frame", cookies=cookies)
        
    @pytest.mark.parametrize('data', [
        ({
            "username": "张三",
            "english_name": "zhangsan",
            "acctid": "tester_0000001",
            "gender": "2",
            "phone": "13912345678",
            "telephone": "12345678",
            "mail": "1234567@qq.com",
            "address": "上海市",
            "position": "测试开发",
            "identity": "1",
            "extern_position_set": "custom", "custom_data": "测试",
            "sendInvite": "1"

        }),
        ({
            "username": "李四",
            "english_name": "lisi",
            "acctid": "tester_0000002",
            "phone": "13912345679",

        }),

    ])
    @pytest.mark.run(order=1)
    @allure.story("测试添加成员")
    def test_add_user(self, data):
        self.contact_page.click_contact_nav()
        self.contact_page.add_user()
        self.contact_page.save_user(data)
        assert self.contact_page.get_tips() == "保存成功"

    @pytest.mark.parametrize('data', [
        ({
            "username": "王五",

        }),

    ])
    @pytest.mark.run(order=2)
    @allure.story("测试更新成员信息")
    def test_update_user(self, data):
        self.contact_page.click_contact_nav()
        self.contact_page.search("张三")
        self.contact_page.go_to_search_page().update()
        self.contact_page.save_user(data)
        assert self.contact_page.get_tips() == "保存成功"


    @pytest.mark.run(order=3)
    @allure.story("测试成员禁用")
    def test_disable(self):
        self.driver.refresh()
        self.contact_page.click_contact_nav()
        self.contact_page.search("李四")
        self.contact_page.go_to_search_page().disable()
        assert self.contact_page.get_tips() == "禁用成功"


    @pytest.mark.run(order=4)
    @allure.story("测试成员启用")
    def test_enable(self):
        self.driver.refresh()
        self.contact_page.click_contact_nav()
        self.contact_page.search("李四")
        self.contact_page.go_to_search_page().enable()
        assert self.contact_page.get_tips() == "启用成功"
