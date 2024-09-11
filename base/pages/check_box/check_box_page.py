from playwright.sync_api import Page
from base.page_factory.button import Button


class CheckBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: text box"""
        self.expand = Button(page, locator='//*[@aria-label="Expand all"]', name='Expand all')
        self.home = Button(page, locator='//*[@for="tree-node-home"]', name='Home')
        self.collapse = Button(page, locator= '//*[@aria-label="Collapse all"]', name='Collapse all')


        """Ожидания"""
        self.Wait_expand = '//*[@aria-label="Expand all"]'

