import time

from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase


class ResetPasswordPage(HelperTestBase):
    def ResetPasswordPage(self):
        driver = self.driver
        driver.get(self.base_url)

        ### Submit user's Email action :

    # def submitEmail(self, userEmail=None):
    #     self.driver.find_element_by_name("email").send_keys(userEmail)
    #     sendButton = self.driver.find_element_by_xpath("//body/app-root/div/div/password-reset/div/form/button")
    #     sendButton.click()


    #### Success Reset password action:   ########
    def openResetPasswordForm(self):
        self.driver.find_element_by_id("identifierId").send_keys('svetatestbox@gmail.com')
        self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element_by_name('password').send_keys('ss@1234567')
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get('https://mail.google.com/mail/u/0/#inbox')
        time.sleep(9)
        self.driver.find_elements_by_xpath("//span/b[contains(text(), 'Password reset on BiziBAZA')]")[0].click()
        time.sleep(3)
        self.driver.find_element_by_partial_link_text("https://bizibaza.com/password-reset-confirm?reset").click()
        time.sleep(5)


    def fillResetPasswordForm(self, password=None, confirmPassword=None):
        self.driver.find_element_by_id('password1').send_keys(password)
        self.driver.find_element_by_id('password2').send_keys(confirmPassword)
        self.driver.find_element_by_id('password1').send_keys(Keys.ENTER)
        time.sleep(5)

    def openConfirmResetPasswordByEmail(self):
        self.driver.find_element_by_id("identifierId").send_keys('svetatestbox@gmail.com')
        self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element_by_name('password').send_keys('ss@1234567')
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get('https://mail.google.com/mail/u/0/#inbox')
        time.sleep(9)
        self.driver.find_elements_by_xpath("//span/b[contains(text(), 'Password was changed')]")[0].click()

    def getMessage(self):
        message = self.driver.find_element_by_css_selector(".alert.alert-danger>p").text
        return message

