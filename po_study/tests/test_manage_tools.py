import allure
from po_study.pages.manage_tools_page import ManageTools
from po_study.tests.driver import Driver


@allure.feature("第十期_Selenium PO 与企业微信实战_20190804课后作业-上传图片")
class TestManageTool:
    @classmethod
    def setup_class(cls):
        cls.driver = Driver().login()
        cls.manage_page = ManageTools(cls.driver)
        cls.manage_page.click_manage_tools()

    @allure.story("测试上传图片")
    def test_upload_image(self):
        self.manage_page.click_material_lib()
        image_manage_page = self.manage_page.go_to_image_manage()
        image_manage_page.upload_image()

