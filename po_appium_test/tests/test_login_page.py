from time import sleep
import pytest
from po_appium_test.driver import driver
from po_appium_test.pages.login_page import LoginPage
import allure


@allure.feature("第十期_appium 进阶_20190825课后作业")
class TestLogin:

    # 初始化
    @classmethod
    def setup_class(cls):
        cls.driver = driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.cancel_update()
    # 结束
    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()

    @pytest.mark.run(order=1)
    @allure.story("测试手机号错误")
    def test_wrong_phone(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.go_to_phone_login()
        self.login_page.send_phone_password("1234567890", "123456")
        assert self.login_page.get_prompt_text() == "手机号码填写错误"

    @pytest.mark.run(order=2)
    @allure.story("测试密码错误")
    def test_wrong_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.send_phone_password("13812345678", "111111")
        assert self.login_page.get_prompt_text() == "用户名或密码错误"


if __name__ == '__main__':
    pytest.main()