import time

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class ProfilePage(NavigationMenuPage):
    def ProfilePage(self):
        driver = self.driver
        driver.get(self.base_url)


    def clickAddress(self):
        self.driver.find_element_by_css_selector("[data-test-id='profileAddressEdit']").click()

    def editWebField(self, webpagestring=None):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        fields[0].clear()
        fields[0].send_keys(webpagestring)
        self.driver.find_element_by_css_selector(".app-header__container").click()


    def getWebString(self):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        text = fields[0].text
        return text

    def getEmailString(self):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        text = fields[1].text
        return text


    def getPpString(self):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        text = fields[2].text
        return text



    def editEmailField(self, emailestring=None):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        fields[1].clear()
        fields[1].send_keys(emailestring)
        self.driver.find_element_by_css_selector(".app-header__container").click()


    def editPayPalField(self, paypalstring=None):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='text']")
        fields[2].clear()
        fields[2].send_keys(paypalstring)
        self.driver.find_element_by_css_selector(".app-header__container").click()


    def clickCancelAddress(self):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='profileLink']")
        fields[0].click()


    def clickDoneAddress(self):
        fields = self.driver.find_elements_by_css_selector("[data-test-id='profileLink']")
        fields[1].click()

    def uploadPhoto(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='uploadBtn']")
        time.sleep(3)
        self.driver.switch_to_active_element()





    def closeModalWindow(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='cancelButton']")
        time.sleep(2)
