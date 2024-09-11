import allure

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from conftest import modal_dialogs
from src.config.expectations import Wait


class ModalDialogsMethods:

    @staticmethod
    def click_modal_dialogs (modal_dialogs: ModalDialogsPage):
        errors = []
        Wait.set_page(modal_dialogs.page)

        try:
            with allure.step("Small and large modals"):
                modal_dialogs.small_modal.click()
                modal_dialogs.close_small_modal.click()
                modal_dialogs.large_modal.click()
                modal_dialogs.close_large_modal.click()


        except AssertionError as e:
            errors.append(str(e))





