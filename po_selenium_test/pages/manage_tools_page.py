from po_selenium_test.pages.base_page import BasePage
from po_selenium_test.pages.material_lib_page import MaterialLibPage


class ManageTools(BasePage):
    _manage_tools_nav = ("xpath", '//*[@id="menu_manageTools"]/span')   # 管理工具
    _material_lib = ("xpath",  "//*[text()='素材库']")     # 素材库

    # 点击管理工具
    def click_manage_tools(self):
        self.find_element(*self._manage_tools_nav).click()

    # 点击素材库
    def click_material_lib(self):
        self.find_element(*self._material_lib).click()

    # 去到素材库页面
    def go_to_image_manage(self):
        return MaterialLibPage(self._driver)