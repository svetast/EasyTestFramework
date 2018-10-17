import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.SettingsPage import SettingsPage


class TestSettings(SettingsPage):
    ####### Test scope - Buyer clicks on SettingsLink => Settings page is opened:
    # @pytest.mark.skip

    def test_clickSettingsLinkByuerAndBack(self):
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')

        # HelperTestBase.clickSettingsButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        # HelperTestBase.waitURL(self, url2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='settingsTitle']"), True)
        HelperTestBase.clickHomeIcon(self)
        time.sleep(2)
        self.assertEqual(url1, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_loginLogOutAll_Devices(self):
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/login'
        url2 = self.base_url + '/settings'
        text = 'Logout:'
        text3 = 'Do you want to logout from all devices ?'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')

        HelperTestBase.logOutAllDevices(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='logoutFromAll']")
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='username']"), True)











        ####### Test scope - Seller clicks on SettingsLink => Settings page is opened:

    # @pytest.mark.skip
    def test_clickSettingsLinkSellerAndBack(self):
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        url3 = self.base_url + '/inventory-list'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        # HelperTestBase.waitURL(self, url2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='settingsTitle']"), True)
        HelperTestBase.clickHomeIcon(self)
        time.sleep(2)
        self.assertEqual(url3, HelperTestBase.getURL(self))

    def test_clickGoToAboutSeller(self):
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        url3 = self.base_url + '/about'
        url = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.waitSettingsButton(self)
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # Test scope -  Seller clicks on About icon => About page is opened:
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='goToAbout']")
        self.assertEqual(url3, HelperTestBase.getURL(self))
        # Click on <  icon => Settings page is opened:
        HelperTestBase.clickBackIcon(self)
        # HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # Click on 'Home' icon => The Inventory list is opened
        SettingsPage.clickHomeIcon(self)
        # HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        time.sleep(2)
        self.assertEqual(url, HelperTestBase.getURL(self))

    def test_clickGoToAboutByuer(self):
        # Test scope Buyer clicks on About icon => About page is opened:
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        url3 = self.base_url + '/about'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        # HelperTestBase.waitURL(self, url2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # Test scope -  buyer clicks on About icon => About page is opened:
        HelperTestBase.reliableClick(self, "[data-test-id='goToAbout']")
        self.assertEqual(url3, HelperTestBase.getURL(self))
        # Click on <  icon => Settings page is opened:
        HelperTestBase.clickBackIcon(self)
        # HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # Click on 'Home' icon => The Shopping list is opened
        SettingsPage.clickHomeIcon(self)
        # HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        time.sleep(2)
        self.assertEqual(url1, HelperTestBase.getURL(self))

    def test_sendFeedbackBuyer(self):
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        text = 'support@BiziBAZA.com'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # Test scope Buyer clicks on Send Feedback icon => Submit form is opened:
        SettingsPage.sendFeedback(self)
        time.sleep(6)
        self.assertIn(text, self.driver.page_source)

    def test_sendFeedbackSeller(self):
        url1 = self.base_url + '/shopping-list'
        url2 = self.base_url + '/settings'
        text = 'support@BiziBAZA.com'
        # Test scope Seller clicks on Send Feedback icon => Submit form is opened:

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        NavigationMenuPage.clickSellerButton(self)
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='settingsLink']")

        self.assertEqual(url2, HelperTestBase.getURL(self))
        SettingsPage.sendFeedback(self)
        time.sleep(6)
        self.assertIn(text, self.driver.page_source)
