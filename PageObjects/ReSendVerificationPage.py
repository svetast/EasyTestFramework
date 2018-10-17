from HelperTestBase import HelperTestBase


class ReSendVerificationPage(HelperTestBase):
    def ReSendVerifikationPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def submitReSendVerificationForm(self, email=None):
        self.driver.find_element_by_css_selector("[data-test-id='resetEmailInp']").send_keys(email)
        self.driver.find_element_by_css_selector("[data-test-id='resetBtn']").click()

    def closeReSendVerificationForm(self):
        self.driver.find_element_by_css_selector("[data-test-id='loginLink']").click()

    def checkSendButton(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='resetBtn']").click()
        return state
