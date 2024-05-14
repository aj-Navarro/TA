from selenium.webdriver.common.by import By

from .common import CommonOps



class Checkboxes(CommonOps):
    
    CHECKBOXES = (By.LINK_TEXT, "Checkboxes")
    CHECKBOX_1 = (By.XPATH, "//form[@id='checkboxes']/input[1]")
    CHECKBOX_2 = (By.XPATH, "//form[@id='checkboxes']/input[2]")
    PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")

    def navigate_to_checkboxes_page(self):
        self.wait_for(self.CHECKBOXES).click()

    def click_checkbox_01(self):
        self.find(self.CHECKBOX_1).click()

    def click_checkbox_02(self):
        self.find(self.CHECKBOX_2).click()

    def page_displayed(self):
        return self.wait_for(self.PAGE_TITLE).text