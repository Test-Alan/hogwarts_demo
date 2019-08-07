import pytest

from po_study.pages.contact_page import ContactPage
from po_study.tests.driver import Driver


cookies = {

}


@pytest.fixture(scope="session")
def Page():
    driver = Driver().browser()
    page = ContactPage(driver)
    page.get("https://work.weixin.qq.com/wework_admin/frame", cookies=cookies)
    return page