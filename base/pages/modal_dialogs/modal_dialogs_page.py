from asyncio import timeout

from playwright.sync_api import Page, expect
from pyexpat.errors import messages

from base.page_factory.button import Button


class ModalDialogsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""

        self.small_modal = Button(page, locator='//*[@id="showSmallModal"]', name='Open small modal')
        self.small_modal_text = page.locator('//*[@id="example-modal-sizes-title-sm"]')
        self.close_small_modal = Button(page, locator='//*[@id="closeSmallModal"]', name='Open small modal')
        self.large_modal = Button(page, locator='//*[@id="showLargeModal"]', name='Open large modal')
        self.large_modal_text = page.locator('//*[@id="example-modal-sizes-title-lg"]')
        self.close_large_modal = Button(page, locator='//*[@id="closeLargeModal"]', name='Close large modal')


        """Ожидания"""
        self.Wait_small_modal = '//*[@id="showSmallModal"]'
        self.Wait_large_modal = '//*[@id="showLargeModal"]'
        self.Wait_small_modal_text = '//*[@id="example-modal-sizes-title-sm"]'


