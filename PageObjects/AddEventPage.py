import time
from HelperTestBase import HelperTestBase
from PageObjects.ProductEditorPage import ProductEditorPage
from selenium.webdriver.common.keys import Keys


class AddEventPage(ProductEditorPage):
    def AddEventPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickBackFromEvent(self):
        self.driver.find_element_by_css_selector("[data-test-id='backFromEvent']").click()
        time.sleep(5)


    def searchMarket(self, marketName):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(marketName)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(3)

    def selectMarket(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(5)

    def getModalHeader(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalHeader']").text
        return text

    def getModalMessage(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalMessage']").text
        return text