import time

from HelperTestBase import HelperTestBase
from PageObjects.ChangePasswordPage import ChangePasswordPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.SettingsPage import SettingsPage


class Test_ChangePassword(ChangePasswordPage):
    # @pytest.mark.skip
    def test_check_ChangePasswordFormOpenBuyer(self):
        # Test scope - Buyer clicks on Change Password = > ChangePassword page is opened, the elementts are present:
        url1 = self.base_url + '/shopping-list'
        url3 = self.base_url + '/change-password'
        url2 = self.base_url + '/settings'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        self.assertEqual(url1, HelperTestBase.getURL(self))
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        time.sleep(2)
        SettingsPage.clickChangePasswordButton(self)
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='oldPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='newPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='repeatPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='showPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='backLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='changePassword']"), True)
        # Test scope - click on back button = > Settings page is opened:
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_check_ChangePasswordFormOpenSeller(self):
        # Test scope - Buyer clicks on Change Password = > ChangePassword page is opened, the elementts are present:
        url1 = self.base_url + '/shopping-list'
        url3 = self.base_url + '/change-password'
        url2 = self.base_url + '/settings'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        self.assertEqual(url1, HelperTestBase.getURL(self))
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        time.sleep(2)
        SettingsPage.clickChangePasswordButton(self)
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='oldPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='newPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='repeatPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='showPassword']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='backLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='changePassword']"), True)
        # Test scope - click on back button = > Settings page is opened:
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_submitChangePasswordForm(self):
        url1 = self.base_url + '/shopping-list'
        url3 = self.base_url + '/change-password'
        url2 = self.base_url + '/settings'
        text1 = 'Password must contain form 8 to 20 characters: upper+lowercase and digit(s).'
        text2 = 'The new passwords mismatch!'
        text3 = 'Cannot to change password'
        text4 = 'Passwords can not be the same'
        text5 = 'Your old password is incorrect'
        text6 = "Password successfully changed"


        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        time.sleep(2)
        # validation change password form":
        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordFormInvalidData(self, 'Ss123456', 'Ss12345', 'Ss12345')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordFormInvalidData(self, 'Ss123456', '12345678', '12345678')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordFormInvalidData(self, 'Ss123456', 'Asdfghjkl', 'Asdfghjkl')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordFormInvalidData(self, 'Ss123456', 'Ss123456', 'Ss1234567')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text2, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordFormInvalidData(self, 'Ss123456', 'Ss123456', 'ss1234567')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")


        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ss123456', 'Ss123456', 'Ss123456')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertEqual(text3, HelperTestBase.getModalHeader(self))
        self.assertEqual(text4, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ss123', 'Ss123456', 'Ss123456')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertEqual(text3, HelperTestBase.getModalHeader(self))
        self.assertEqual(text5, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ss123456', '', 'Ss123456')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text2, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ss123456', 'Ss123456', '.')
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        # test scope - successfully change password:

        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ss123456', 'Ff123456', 'Ff123456')
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertEqual(text6, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickYesButton(self)
        SettingsPage.clickLogout(self)
        HelperTestBase.clickYesButton(self)

        # test scope - after successfully change password user can login using new password:

        LoginPage.loginAction(self, 'Bob', 'Ff123456')
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        time.sleep(2)
        # return to start:
        SettingsPage.clickChangePasswordButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        SettingsPage.clickChangePasswordButton(self)
        ChangePasswordPage.fillChangePasswordForm(self, 'Ff123456', 'Ss123456', 'Ss123456')
        # self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertEqual(text6, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickYesButton(self)
