import time

from HelperTestBase import HelperTestBase
from PageObjects.ResetPasswordPage import ResetPasswordPage


class Test_WWW_ResetPassword(ResetPasswordPage):

        # @pytest.mark.skip

    def test_WWW_SubmitResetPasswordForm(self):
        driver = self.driver
        driver.get('https://accounts.google.com/signin')
        driver.maximize_window()
        text1 = 'Restore password'
        text2 = 'Password must contains one uppercase letter, one digit and be more than 8 symbols!'
        text3 = "The passwords don't match."
        text4 = "Will be Error message!!!"
        text5 = "Success!"
        text6 = "Password was successfully changed"

        ResetPasswordPage.openResetPasswordForm(self)
        driver.switch_to_window(driver.window_handles[1])

        time.sleep(6)
        self.assertEqual(text1, HelperTestBase.getTitle(self))
        # Test scope - check that fields are present:
        self.assertIs(HelperTestBase.checkPasswordFieldEnabled(self, "password1"), True)
        self.assertIs(HelperTestBase.checkPasswordFieldEnabled(self, "password2"), True)

        # Test scope - check validation fields :

        ResetPasswordPage.fillResetPasswordForm(self, '', '')
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, '12345678', '12345678')
        self.assertEqual(text2, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, 'Asdfghjk', 'Asdfghjk')
        self.assertEqual(text2, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, 'Ss1234567', 'Ss123456')
        self.assertEqual(text3, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, '', 'Ss123456')
        self.assertEqual(text3, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, 'Ss123456', '')
        self.assertEqual(text2, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, 'Ss123456', 'Ss123456')
        self.assertEqual(text2, ResetPasswordPage.getMessage(self))
        self.assertEqual(text1, HelperTestBase.getTitle(self))

        ResetPasswordPage.fillResetPasswordForm(self, 'Ss1234567', 'Ss1234567')
        time.sleep(4)
        self.assertIn(text5, self.driver.page_source)
        self.assertIn(text6, self.driver.page_source)
        # self.assertEqual(text4, ResetPasswordPage.getMessage(self))

        # @pytest.mark.skip

    def test_ZZZ_CheckConfirmResetPasswordForm(self):
        driver = self.driver
        driver.get('https://accounts.google.com/signin')
        driver.maximize_window()
        text1 = 'This email is to confirm your password was changed.'
        text2 = 'Thank you for using BiziBAZA.'
        text3 = 'Sincerely,'
        text4 = 'BiziBAZA Support'
        ResetPasswordPage.openConfirmResetPasswordByEmail(self)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        self.assertIn(text4, self.driver.page_source)
