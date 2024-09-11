from playwright.sync_api import Page
from base.page_factory.button import Button


class RadioButtonPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: radio button"""

        self.yes = Button(page, locator='//*[@for="yesRadio"]', name='Yes')
        self.impressive = Button(page, locator='//*[@for="impressiveRadio"]', name='Impressive')
        self.yes = Button(page, locator='//*[@for="yesRadio"]', name='Yes')
        self.impressive = Button(page, locator='//*[@for="impressiveRadio"]', name='Impressive')

        """Ожидания"""
        self.Wait_yes = '//*[@id="yesRadio"]'
