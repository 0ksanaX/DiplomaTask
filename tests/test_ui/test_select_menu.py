import allure
from playwright.sync_api import Page

from base.pages.text_box.text_box_page import TextBoxPage

from base.pages.text_box.textbox_start import TextBoxStart
from conftest import text_box


class TestTextBox:

    @allure.epic("Тесты потока 2")
    @allure.feature("Text Box")
    @allure.title("Заполнение формы регистрации пользователя 1")
    def test_text_box(self, page: Page, text_box: TextBoxPage):
        TextBoxStart.text_box (page, text_box)