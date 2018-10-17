import time

from HelperTestBase import HelperTestBase
from PageObjects.AnalyticsPage import AnalyticsPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestAnalyticsHistory(NavigationMenuPage):
    ### Test scope -  Seller: Click on Duties =>	The 'Duties' page is opened:

    # @pytest.mark.skip
    def test_clickOnDutiesSeller(self):
        url = self.base_url + '/duties'
        url2 = self.base_url + '/analytics'
        url1 = self.base_url + '/inventory-list'
        url3 = self.base_url + '/shopping-list'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        NavigationMenuPage.clickSellerButton(self)
        NavigationMenuPage.clickAnalytics(self)
        # ### Test scope -  click on 'Duties' page:
        AnalyticsPage.clickDutiesButton(self)
        time.sleep(2)
        self.assertEqual(url, HelperTestBase.getURL(self))

        ### Test scope -  check the elements on 'Duties' page:

        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dutyItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analyticLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='duties']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='rightDirItem_0']"), True)

        ### Test scope -  click on  < button on 'Duties list' page => Analytics page is opened:
        AnalyticsPage.reliableClick(self, "[data-test-id='analyticLink']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
        ### Test scope -  click on  < button on 'Analytics' page => Inventory list page is opened:
        AnalyticsPage.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url1, HelperTestBase.getURL(self))

        ### Test scope - Buyer:  Check the elements on Analytics page =>	The are present:  < button, History

    # @pytest.mark.skip
    def test_checkElementsBuyer(self):
            url = self.base_url + '/login'
            url2 = self.base_url + '/analytics'
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
            # LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            NavigationMenuPage.clickAnalytics(self)

            # NavigationMenuPage.clickAnalytics(self)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='history']"), True)

        ### Test scope - Seller:  Check the elements on Analytics page =>	The are present:  < button, History, Duties

    # @pytest.mark.skip
    def test_checkElementsSeller(self):
            url2 = self.base_url + '/analytics'
            url = self.base_url + '/shopping-list'
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

            NavigationMenuPage.clickSellerButton(self)
            time.sleep(5)
            # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            # time.sleep(1)
            # HelperTestBase.clickAndWait(self, "[data-test-id='analytics']")
            # time.sleep(2)
            NavigationMenuPage.clickAnalytics(self)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='history']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='duties']"), True)

        ### Test scope -  Seller: Click on Back button =>	The Inventory list is displayed:

    # @pytest.mark.skip
    def test_clickBackSeller(self):
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/analytics'
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
            # LoginPage.loginAction(self, 'Bob', 'Ss123456')

            NavigationMenuPage.clickSellerButton(self)
            time.sleep(4)
            NavigationMenuPage.clickAnalytics(self)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
            self.assertEqual(url1, HelperTestBase.getURL(self))

        ### Test scope -  Buyer: Click on Back button => The The Shopping list is opened:

    # @pytest.mark.skip
    def test_clickBackBuyer(self):
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/analytics'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(4)
            NavigationMenuPage.clickAnalytics(self)
            time.sleep(2)
            self.assertEqual(url2, HelperTestBase.getURL(self))

        # Test scope-  Buyer: Click on History =>	The Buyer History page is opened:

    # @pytest.mark.skip
    def test_clickOnHistoryBuyer(self):
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/analytics'
            url3 = self.base_url + '/history'
            driver = self.driver
            driver.get(self.base_url)
            # LoginPage.loginAction(self, 'Bob', 'Ss123456')
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
            NavigationMenuPage.clickAnalytics(self)
            AnalyticsPage.clickHistoryButton(self)
            time.sleep(2)
            self.assertEqual(url3, HelperTestBase.getURL(self))

        ### Test scope -  Seller: Click on History =>	The 'Seller History' page is opened:

    # @pytest.mark.skip
    def test_clickOnHistorySeller(self):
            url = self.base_url + '/history'
            url1 = self.base_url + '/inventory-list'
            url2 = self.base_url + '/analytics'
            url3 = self.base_url + '/shopping-list'

            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
            time.sleep(5)
            # LoginPage.loginAction(self, 'Bob', 'Ss123456')
            self.assertEqual(url3, HelperTestBase.getURL(self))
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            NavigationMenuPage.clickAnalytics(self)
            time.sleep(2)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
            AnalyticsPage.clickHistoryButton(self)
            self.assertEqual(url, HelperTestBase.getURL(self))

            ### Test scope -  check the elements on 'Seller History' page:

            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='historyItem_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analyticLink']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='sellerHistory']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='rightDirItem_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='qntItems']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='total']"), True)

            ### Test scope -  click on  < button on 'Seller History' page => 'Analytics' page is opened:
            HelperTestBase.reliableClick(self, "[data-test-id='analyticLink']")
            # AnalyticsPage.clickBackFromHistoryAndDuties(self)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            ### Test scope -  click on  < button on 'Analytics' page => Inventory list page is opened:
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
            # AnalyticsPage.clickBackFromAnalytics(self)
            self.assertEqual(url1, HelperTestBase.getURL(self))
