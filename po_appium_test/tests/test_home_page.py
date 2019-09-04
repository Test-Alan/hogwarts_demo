from time import sleep
import allure
from po_appium_test.driver import driver
from po_appium_test.pages.home_page import HomePage
import pytest


@allure.feature("第十期_appium 进阶_20190825课后作业")
class TestSearch:

    # 初始化
    @classmethod
    def setup_class(cls):
        cls.driver = driver()
        cls.home_page = HomePage(cls.driver)
    # 结束
    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()

    @pytest.mark.parametrize('name, expect', [
        ("alibab", "阿里巴巴"),
        ("xiaomi", "小米集团-W"),
        ("Google", "谷歌A"),
    ])
    @pytest.mark.run(order=1)
    @allure.story("测试搜索")
    def test_search(self, name, expect):
        """
        测试搜索
        :param name: 搜索名称
        :param expect: 预期结果
        :return:
        """
        self.home_page.search(name, expect)
        assert self.home_page.get_search_result() == expect
        sleep(1)
        self.home_page.click_action_close()

    @pytest.mark.parametrize('name, expect', [
        ("alibab", "阿里巴巴"),
    ])
    @pytest.mark.run(order=2)
    @allure.story("测试添加自选股")
    def test_add_optional(self, name, expect):
        self.home_page.search(name, expect)
        self.home_page.click_add_optional("BABA")
        self.home_page.click_action_close()
        self.home_page.go_to_optional()
        self.home_page.press_cancel_supernatant()
        assert self.home_page.get_stock_name(index=0) == "阿里巴巴"

    @pytest.mark.parametrize('name, expect', [
        ("alibab", "阿里巴巴"),
    ])
    @pytest.mark.run(order=3)
    @allure.story("测试自选股已添加")
    def test_optional_added(self, name, expect):
        self.home_page.go_to_xue_qiu()
        self.home_page.search(name, expect)
        assert self.home_page.get_added_text("BABA") == "已添加"
        self.home_page.click_action_close()

    @pytest.mark.parametrize('name, expect', [
        ("alibab", "阿里巴巴"),
    ])
    @pytest.mark.run(order=4)
    @allure.story("测试删除自选股")
    def test_delete_optional(self, name, expect):
        self.home_page.go_to_optional()
        self.home_page.press_cancel_supernatant()
        self.home_page.delete_optional(index=0)
        self.home_page.go_to_xue_qiu()
        self.home_page.search(name, expect)
        assert self.home_page.get_add_optional_text("BABA") == "加自选"