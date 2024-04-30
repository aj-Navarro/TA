import pytest
from selenium.webdriver.common.by import By
from .common import CommonOps



class ContextMenu(CommonOps):

    CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    CONTEXT_BOX = (By.ID, "hot-spot")
    PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")
    CONTENT = (By.ID, "content")


    def navigate_to_context_menu_page(self):
        self.wait_for(self.CONTEXT_MENU).click()

    def right_click_context_menu(self):
        context_menu = self.find(self.CONTEXT_BOX)
        self.context_click(context_menu).perform()

    def check_alert_message(self):
        return self.alert().text

    def accept_alert(self):
        return self.alert().accept()

    def alert_is_accepted(self):
        return self.wait_for(self.PAGE_TITLE).text

    def dismiss_context_menu(self):
        content = self.find(self.CONTENT)
        self.double_click(content).perform()
    
    # def dismiss_context_menu(self):
    #    self.escape_key_down()