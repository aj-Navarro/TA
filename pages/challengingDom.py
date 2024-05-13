from selenium.webdriver.common.by import By

from .common import CommonOps



class ChallengingDom(CommonOps):
    
    CHALLENGING_DOM = (By.LINK_TEXT, "Challenging DOM")
    EDIT_LINK = (By.XPATH, "//a[text()='edit'][1]")
    DELETE_LINK = (By.XPATH, "//a[text()='delete'][1]")
    SECOND_BUTTON = (By.XPATH, "//div[@class='large-2 columns']/a[2]")
    PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def navigate_to_challenging_dom_page(self):
        self.wait_for(self.CHALLENGING_DOM).click()

    def click_edit(self):
        self.find(self.EDIT_LINK).click()

    def click_delete(self):
        self.find(self.DELETE_LINK).click()
    
    def click_second_button(self):
        self.find(self.SECOND_BUTTON).click()

    def page_displayed(self):
        return self.wait_for(self.PAGE_TITLE).text