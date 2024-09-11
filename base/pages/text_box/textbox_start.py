import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.text_box.text_box_methods import TextBoxMethods
from base.pages.text_box.text_box_page import TextBoxPage


class TextBoxStart:
    @staticmethod
    def text_box(page: Page, text_box: TextBoxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.text_box(page)

            with allure.step("Ввод данных пользователя"):
                TextBoxMethods.fill_text_input(text_box)

        except AssertionError as e:
            errors.append(str(e))


