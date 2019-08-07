from po_study.pages.base_page import BasePage


class ManageTools(BasePage):
    _manage_tools_nav = ("xpath", '//*[@id="menu_manageTools"]/span')
    _material_lib = ("xpath",  "//*[text()='素材库']")
    _image = ("css", ".ww_icon_GrayPic")
    _add_image = ("css", ".ww_commonImg_AddMember")

    def click_manage_tools(self):
        self.find_element(*self._manage_tools_nav).click()

    def up_images(self):
        self.find_element(*self._material_lib).click()
        self.find_element(*self._image).click()
        self.find_element(*self._add_image).click()
