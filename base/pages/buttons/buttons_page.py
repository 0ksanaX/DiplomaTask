from playwright.sync_api import Page
from base.page_factory.button import Button



class ButtonsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: buttons"""


        self.dclick_me = Button(page, locator='//*[@id="doubleClickBtn"]', name='Double Click Me')
        self.dclick_message = Button( page, locator= '//*[@id="doubleClickMessage"]', name='double Click Message')





