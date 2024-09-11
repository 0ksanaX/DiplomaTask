from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def modal_dialogs(page: Page):
        BasePage.open_page(page, Url.MODAL_DIALOGS)



