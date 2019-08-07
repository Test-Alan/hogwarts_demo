from po_study.pages.base_page import BasePage


class ProfilePage(BasePage):

    _editor_link = ("css", ".js_edit")

    def update(self):
        self.find_element(*self._editor_link).click()


    def disable(self):
        pass

    def enable(self):
        pass

    def delete(self):
        pass

    def invite(self):
        pass