from po_study.pages.base_page import BasePage


class MaterialLibPage(BasePage):
    _image = ("css", '[href="#material/image"]')    # 图片
    _add_image = ("css", ".js_upload_file_selector")     # 添加图片按钮
    _up_image = ("id", "js_upload_input")
    _up_cencel = ("css", ".js_uploadProgress_cancel")
    _next = ("css", ".js_next")

    # 上传图片
    def upload_image(self):
        self.find_element(*self._image).click()
        self._driver.refresh()
        element_add = self.find_element(*self._add_image)
        self.run_script("arguments[0].click();", element_add)
        image_path = self.file_path('/images/upload/test.jpeg')
        self.find_element(*self._up_image).send_keys(image_path)
        self.invisibility_of_element(*self._up_cencel)
        next_elm = self.find_element(*self._next)
        self.run_script("arguments[0].click();", next_elm)
