import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class TestAActualUserState(LoginPage):
    # @pytest.mark.skip
    def test_checkActualTestData(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'Your cart is currently empty'
        ### Checking is user present:

        LoginPage.loginActionWithoutKeepMeLogged(self, 'svetast', 'Ss1234567')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()

        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'SA1', 'Bizibaza111')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()

        ###

        LoginPage.loginActionWithoutKeepMeLogged(self, 'Bob', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()

        ###




        LoginPage.loginActionWithoutKeepMeLogged(self, 'SellerTestcjd', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()

        ###

        LoginPage.loginActionWithoutKeepMeLogged(self, 'SellerTestavm', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()

        ###

        LoginPage.loginActionWithoutKeepMeLogged(self, 'SellerTestcjd', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.driver.refresh()
