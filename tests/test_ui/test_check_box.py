import allure
from playwright.sync_api import Page

from base.pages.check_box.check_box_page import CheckBoxPage
from base.pages.check_box.checkbox_start import CheckBoxStart
from conftest import check_box


class TestCheckBox:

    @allure.epic("Тесты потока 1")
    @allure.feature("Check Button")
    @allure.title("Click check boxes")
    def test_check_box(self, page: Page, check_box: CheckBoxPage):
        CheckBoxStart.check_box (page, check_box)