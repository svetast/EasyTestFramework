import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class InventoryListPage(LoginPage):
    def InventoryListPage(self):
        driver = self.driver
        driver.get(self.base_url)



    def getModalHeader(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalHeader']").text
        return text

    def getModalMessage(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalMessage']").text
        return text

    def clickBiziPixButton(self):
        self.driver.find_element_by_css_selector("[data-test-id='biziPixLink']").click()
        time.sleep(5)

    def deleteItemsFromFromList(self):
        i = 1
        while (i <= 10):
            self.driver.find_element_by_css_selector("[data-test-id='removeItem_0']").click()
            HelperTestBase.clickYesButton(self)
            i += 1

    def deleteItem(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='removeItem_0']")
