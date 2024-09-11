import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.buttons.buttons_methods import ButtonsMethods
from base.pages.buttons.buttons_page import ButtonsPage


class ButtonsStart:
    @staticmethod
    def buttons(page: Page, buttons: ButtonsPage):
        errors = []
        try:
            with allure.step("Page openning"):
                AuthorizationMethod.buttons(page)

            with allure.step("Buttons check"):
                ButtonsMethods.double_click_buttons(buttons)

        except AssertionError as e:
            errors.append(str(e))
