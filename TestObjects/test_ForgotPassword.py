from HelperTestBase import HelperTestBase
from PageObjects.ForgotPasswordPage import ForgotPasswordPage
from PageObjects.LoginPage import LoginPage


class TestForgotPassword(ForgotPasswordPage):
    ###  Test scope:  click on the 'Forgot password?' button. => 1.'Password reset' page is displayed.

    # 2. "Please, enter the valid email address associated to BiziBAZA and enter a new password. We will send you an email with a link to confirm your new password.

    # If you have forgotten your email or password please contact BiziBAZA support at support@BiziBAZA.com." message is displayed.

    # 3. The 'Email' field is anabled.

    # 4.The 'Send' button is enabled.
    # 5. Click on < Log In link on 'Forgot password' page => Log In page is opened:



    # @pytest.mark.skip
    def test_ForgotPasswordStartClose(self):
        url = self.base_url + '/login'
        url1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)

        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='emailInput']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='resendBtn']"), True)
        HelperTestBase.clickAndWait(self, "[data-test-id='loginLink']")
        self.assertEqual(url, HelperTestBase.getURL(self))

    # Test scope - Input a valid email on the 'Forgot password' form and press the "Send link" button=>
    # 1.The "You've been sent an email instruction on acquiring a new password." message  is displayed.

    #@pytest.mark.skip
    def test_ForgotPasswordSuccess(self):
        url_1 = self.base_url + '/password-reset'
        text = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        text1 = 'Success!'
        text2 = 'Reset instruction has been sent to your email address.'
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)

        self.assertEqual(text, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, 'svetatestbox@gmail.com')
        ForgotPasswordPage.clickSendButton(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)




 # Test scope - Input a spaces before  valid email on the 'Forgot password' form and press the "Send link" button=>
 # 1.The "You've been sent an email instruction on acquiring a new password." message  is displayed.

        # @pytest.mark.skip
    def test_ForgotPasswordSuccess1(self):
        url_1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        text2 = 'Success!'
        text3 = 'Reset instruction has been sent to your email address.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)

        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, '  svetatestbox@gmail.com')
        ForgotPasswordPage.clickSendButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

    # Test scope : type an invalid email, press the 'Send' button =>	The 'Send' button isn't active: +++ add cases
        # @pytest.mark.skip
    def test_ForgotPasswordUnSuccess1(self):
        url_1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, 'werty@')
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertIs(False, HelperTestBase.checkElementEnabled(self, "[data-test-id='resetBtn']" ))
        #self.assertIs(False, ForgotPasswordPage.checkSendButton_IsEnabled(self))

        # Test scope : don't fill out the 'Email' field, press the 'Send' button, press the 'Send' button => The 'Send' button isn't active:
        # @pytest.mark.skip

        # @pytest.mark.skip
    def test_ForgotPasswordUnSuccess2(self):
        url_1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, '')
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertIs(False, HelperTestBase.checkElementEnabled(self, "[data-test-id='resetBtn']"))
        #self.assertIs(False, ForgotPasswordPage.checkSendButton_IsEnabled(self))


        # Input a registered invalid email 'stepanova@dnt-lab.co', press the 'Send' button => 1.Alert with title 'Unable to send email' is displayed.
        # 2. The 'User with email: stepanova@dnt-lab.co, not found' is displayed."

    #@pytest.mark.skip
    def test_ForgotPasswordUnSuccess3(self):
        url_1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        text2 = 'Unable to send an email:'
        text3 = 'User with email:stepanova@dnt-lab.co, not found'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, 'stepanova@dnt-lab.co')
        ForgotPasswordPage.clickSendButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)


        # Test scope : Input an unregistered valid 'favorit@dnt-lab.com' email, press the 'Send' button:
        # 1.Alert with title 'Unable to send email' is displayed. 2. The 'User with email: favorit@dnt-lab.com, not found' is displayed."

    #@pytest.mark.skip

    def test_ForgotPasswordUnSuccess4(self):
        url_1 = self.base_url + '/password-reset'
        text1 = 'Please, enter the valid email address associated to BiziBAZA and enter a new password.'
        text2 = 'Unable to send an email:'
        text3 = 'User with email:favorit@dnt-lab.com, not found'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickForgotPasswordButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text1, ForgotPasswordPage.getSupportMessage(self))
        ForgotPasswordPage.typeEmail(self, 'favorit@dnt-lab.com')
        ForgotPasswordPage.clickSendButton(self)
        self.assertEqual(url_1, HelperTestBase.getURL(self))
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
















