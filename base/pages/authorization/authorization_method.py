from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def date_picker(page: Page):
        BasePage.open_page(page, Url.DATE_PICKER)

    @staticmethod
    def select_menu(page: Page):
        BasePage.open_page(page, Url.SELECT_MENU)


