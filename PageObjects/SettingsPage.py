import time

from HelperTestBase import HelperTestBase


class SettingsPage(HelperTestBase):
    def SettingsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def clickChangePasswordButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='goToChangePassword']")

    def clickAbout(self):
        HelperTestBase.reliableClick(self, "[data-test-id='goToAbout']")
        time.sleep(3)

    def sendFeedback(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='sendFeedback']")
        time.sleep(3)


    def clickLogoutFromAll(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='logoutFromAll']")
        time.sleep(3)

    def clickLogout(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='logout']")
        time.sleep(2)

    def clickHomeIcon(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='backLink']")
        time.sleep(2)
