from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage


class ForgotPasswordPage(LoginPage):
    def ForgotPasswordPage(self):
        driver = self.driver
        driver.get(self.base_url)

# The method for submitting the 'Forgot password?' form:

    def typeEmail(self, userEmail=None):
        self.driver.find_element_by_css_selector("[data-test-id='emailInput']").send_keys(userEmail)




    def clickSendButton(self):
        wait = WebDriverWait(self.driver, 50)
        sendButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='resendBtn']")))
        sendButton.click()







 # get the 'Please, enter the valid email address associated to BiziBAZA and enter a new password.' in the 'Forgot password' page:

    def getSupportMessage(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/div/password-reset/div/div/p[1]").text
        return text

        # get the 'Success!' title of the modal window:

    def getSuccessTitle(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/h3").text
        return text

   # get the 'Reset instruction has been sent to your email address' message in the modal window:

    def getSuccessMessage(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/p").text
        return text

  # get the 'error alert title' text:
    def getErrorTitle(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/h3").text
        return text


   # get 'error alert title' text:

    def getErrorMessage(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/p").text
        return text

# close alert - click on 'OK' button in error dialog box during registration :
    def clickOkButton(self):
        self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/button").click()

