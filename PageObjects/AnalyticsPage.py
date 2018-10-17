import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class AnalyticsPage(LoginPage):
    def AnalyticsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickHistoryButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='history']")
        time.sleep(3)

    def clickDutiesButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='duties']")
        time.sleep(3)

    def clickBackFromHistoryAndDuties(self):
        HelperTestBase.reliableClick(self, "[data-test-id='analyticLink']")
        time.sleep(3)

    def clickBackFromAnalytics(self):
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(4)



#### Click on History of Buyer: use on test_Reviews:


    def clickHistoryBuyer(self):
        HelperTestBase.click(self, "[data-test-id ='historyItem_0']")
        time.sleep(3)

    def clickOnReviewButton(self):
        HelperTestBase.click(self, "[data-test-id ='review_0']")

    def openProductWitchBought(self):
        HelperTestBase.click(self, "[data-test-id='imgItem_0']")
        time.sleep(3)

    def goToReviewsPage(self):
        self.clickHistoryButton()
        self.clickHistoryBuyer()







            # ####### these methods are duplicate in HelperTestBase   #########
    # def getModalHeader(self):
    #     text = self.driver.find_element_by_css_selector("[data-test-id='modal__header']").text
    #     return text
    #
    # def getModalMessage(self):
    #     text = self.driver.find_element_by_css_selector("[data-test-id='modal__msg']").text
    #     return text
    #
    #
    # def sendMessage(self, message=None):
    #     self.driver.find_element_by_name("message").send_keys(message)
    #     self.driver.find_element_by_css_selector("[data-test-id='sendMessage']").click()
    #     time.sleep(6)
