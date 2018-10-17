import time

from HelperTestBase import HelperTestBase
from PageObjects.ForgotPasswordPage import ForgotPasswordPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ReSendVerificationPage import ReSendVerificationPage


class TestReSendVerification(ForgotPasswordPage):
    ###  Test scope:  1.Click on the 'Re-send' button. => 'Re-send verifikation page' page is opened.
    # 2. Click on < link => Login page is opened.




    # @pytest.mark.skip
    def test_reSendVerificationFormOpenClose(self):
        url = self.base_url + '/login'
        url1 = self.base_url + '/email-verification'
        driver = self.driver
        driver.get(self.base_url)
        ###  Test scope:  1.Click on the 'Re-send' button. => 'Re-send verification page' page is opened:
        LoginPage.clickReSendVerification(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='resetEmailInp']"), True)
        # 2. Click on the "< back" link => Login page is opened:
        time.sleep(3)
        ReSendVerificationPage.closeReSendVerificationForm(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_checkReSendVerificationForm(self):
            url = self.base_url + '/login'
            url1 = self.base_url + '/email-verification'
            driver = self.driver
            driver.get(self.base_url)
            text = 'Unable to send an email:'
            text1 = "User with this email not found"
            text3 = 'User email is already verified.'
            text4 = 'Email verification has been sent to your email address.'
            text5 = 'Success!'
            LoginPage.clickReSendVerification(self)
            self.assertEqual(url1, HelperTestBase.getURL(self))

            ### Write the correct email and click on the "Send" button	=> "Your email has been sent. Check your email box and junk box." is displayed:
            ReSendVerificationPage.submitReSendVerificationForm(self, 'svetatestbox+1562@gmail.com')
            self.assertEqual(text5, HelperTestBase.getModalHeader(self))
            self.assertEqual(text4, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            ######### Check Validation:   ########
            ###  Test scope:  Don't fill out Email field => Send button isn't active:
            LoginPage.clickReSendVerification(self)
            ReSendVerificationPage.submitReSendVerificationForm(self, '')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))



            ### Write the email which isn't exist and click on the "Send" button => Error with title 'Unable to send email' "User with this email not found" is displayed:

            ReSendVerificationPage.submitReSendVerificationForm(self, 'kolobok@gmail.com')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            ### Enter the email after confirmed verification = >  "User email is already verified" is displayed:


            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanova@dnt-lab.com')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text3, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            time.sleep(2)

            ### Write the invalid email = >  Send button isn't active:

            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanova@')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))


            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanovadnt-lab.com')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))


            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanova"dnt-labcom')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))

            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanova@dnt-lab  com')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))

            # LoginPage.clickReSendVerification(self)
            ReSendVerificationPage.submitReSendVerificationForm(self, '@gmail.com')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))

            #  LoginPage.clickReSendVerification(self)
            ReSendVerificationPage.submitReSendVerificationForm(self, 'kolobok')
            self.assertEqual(False, hasattr(ReSendVerificationPage.checkSendButton(self), 'send_keys'))

            #  LoginPage.clickReSendVerification(self)
            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepa   nova@dnt-lab.com')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            #  LoginPage.clickReSendVerification(self)
            ReSendVerificationPage.submitReSendVerificationForm(self, 'stepanova@@dnt-lab.com')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
