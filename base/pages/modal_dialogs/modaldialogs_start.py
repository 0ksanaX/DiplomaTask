import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.modal_dialogs.modal_dialogs_methods import ModalDialogsMethods
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage


class ModalDialogsStart:
    @staticmethod
    def modal_dialogs(page: Page, modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Opening page"):
                AuthorizationMethod.modal_dialogs(page)

            with allure.step("Click on small modal"):
                ModalDialogsMethods.click_modal_dialogs(modal_dialogs)


        except AssertionError as e:
            errors.append(str(e))


