import time

from PageObjects.ProductEditorPage import ProductEditorPage


class PayPalPage(ProductEditorPage):
    def PayPalPage(self):
        driver = self.driver
        driver.get("https://www.paypal.com/webscr?cmd=_ap-payment&paykey=AP-65289572T27117508&Z3JncnB0=")

    def clickLogInPayPalButton(self):
        self.driver.find_element_by_id("loadLogin").click()
        time.sleep(4)

    def checkEmailFieldPresent(self):
        state = self.driver.find_element_by_id("login_email").is_displayed()
        return state

    def checkPasswordFieldPresent(self):
        state = self.driver.find_element_by_id("login_password").is_displayed()
        return state

    def checkLogInButtonPresent(self):
        state = self.driver.find_element_by_id("submitLogin").is_displayed()
        return state

    def checkLogInToYourPayPalAccountButton(self):
        state = self.driver.find_element_by_id('loadLogin').is_displayed()
        return state
