import time

from HelperTestBase import HelperTestBase


class ChangePasswordPage(HelperTestBase):
    def ChangePasswordPage(self):
        driver = self.driver
        driver.get(self.base_url)

        ### Submit Change Password form :

    def fillChangePasswordForm(self, oldPassword=None, newPassword=None, repeatPassword=None):
        self.driver.find_element_by_css_selector("[data-test-id='oldPassword']").send_keys(oldPassword)
        self.driver.find_element_by_css_selector("[data-test-id='newPassword']").send_keys(newPassword)
        self.driver.find_element_by_css_selector("[data-test-id='repeatPassword']").send_keys(repeatPassword)
        self.driver.find_element_by_css_selector("[data-test-id='showPassword']").click()
        self.driver.find_element_by_css_selector("[data-test-id='changePassword']").click()
        time.sleep(2)

    def fillChangePasswordFormInvalidData(self, oldPassword=None, newPassword=None, repeatPassword=None):
        self.driver.find_element_by_css_selector("[data-test-id='oldPassword']").send_keys(oldPassword)
        self.driver.find_element_by_css_selector("[data-test-id='newPassword']").send_keys(newPassword)
        self.driver.find_element_by_css_selector("[data-test-id='repeatPassword']").send_keys(repeatPassword)
        self.driver.find_element_by_css_selector("[data-test-id='showPassword']").click()
        time.sleep(2)

    def getMessage(self):
        message = self.driver.find_element_by_css_selector("[data-test-id='errorNewPassword']").text
        return message

    def clickBackIcon(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='backLink']")
