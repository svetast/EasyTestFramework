import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class MessagesPage(LoginPage):
    def MessagesPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def searchMessage(self, someUser=None):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(someUser)

    def clickCancel(self, locator=None):
        HelperTestBase.clickAndWait(self, "[data-test-id='searchCancel']")

    def removeMessage(self):
        deleteButtons = self.driver.find_elements_by_css_selector("[data-test-id='removeItem']")
        deleteButtons[0].click()


    ####### these methods are duplicate in HelperTestBase   #########
    def getModalHeader(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modal__header']").text
        return text

    def getModalMessage(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modal__msg']").text
        return text


    def sendMessage(self, message=None):
        self.driver.find_element_by_name("message").send_keys(message)
        self.driver.find_element_by_css_selector("[data-test-id='sendMessage']").click()
        time.sleep(10)
