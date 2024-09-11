import allure
from playwright.sync_api import Page


from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.modal_dialogs.modaldialogs_start import ModalDialogsStart
from conftest import modal_dialogs


class TestModalDialogs:

    @allure.epic("Modal test")
    @allure.feature("Modal dialog")
    @allure.title("Modal dialogs test")
    def test_modal_dialogs(self, page: Page, modal_dialogs: ModalDialogsPage):
        ModalDialogsStart.modal_dialogs(page, modal_dialogs)