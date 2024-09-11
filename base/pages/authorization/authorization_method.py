from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def text_box(page: Page):
        BasePage.open_page(page, Url.TEXT_BOX)

    @staticmethod
    def check_box(page: Page):
        BasePage.open_page(page, Url.CHECKBOX)

    @staticmethod
    def radio_button(page: Page):
        BasePage.open_page(page, Url.RADIO_BUTTON)

    @staticmethod
    def buttons(page: Page):
        BasePage.open_page(page, Url.BUTTONS)



