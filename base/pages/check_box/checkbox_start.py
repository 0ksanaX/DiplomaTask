import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.check_box.check_box_methods import CheckBoxMethods
from base.pages.check_box.check_box_page import CheckBoxPage


class CheckBoxStart:
    @staticmethod
    def check_box(page: Page, check_box: CheckBoxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.check_box(page)

            with allure.step("Click check boxes"):
                CheckBoxMethods.click_check_box(check_box)

        except AssertionError as e:
            errors.append(str(e))


