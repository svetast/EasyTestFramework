import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestNavigationMenuSeller(NavigationMenuPage):
    # Test scope -  Seller click on the "+" button  => The navigation menu is displayed => Cart, Messages, Profile, Watchlist,
    # Reviewes, Analytics, Favorites are present:

    # @pytest.mark.skip
    def test_clickNavigationMenuButton(self):
        url = self.base_url + '/login'
        url2 = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        url3 = self.base_url + '/settings'
        driver = self.driver
        driver.get(self.base_url)
        text = 'Logout:'
        text1 = 'Do you want to logout?'
        LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
        time.sleep(2)
        NavigationMenuPage.clickSellerButton(self)
        #NavigationMenuPage.clickNavMenuButton(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")

        time.sleep(3)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='new-item']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profile']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchlist']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favorites']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='reviews']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analytics']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialogs']"), True)
        NavigationMenuPage.clickNavMenuButton(self)
        HelperTestBase.logOutAction(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        self.assertEqual(url3, HelperTestBase.getURL(self))
        HelperTestBase.clicklogOutButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # Test scope - Click on the 'Profile' icon => The 'Your profile' page is opened.
        # @pytest.mark.skip
        def test_clickProfileButton(self):
            url = self.base_url + '/profile'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
            NavigationMenuPage.clickProfile(self)
            time.sleep(3)
            # NavigationMenuPage.clickProfile(self)
            self.assertEqual(url, HelperTestBase.getURL(self))

        # Test scope - Click on the 'Favorites' icon => The 'Your favorite list:' page is opened.
        # @pytest.mark.skip
        def test_clickFavoritesButton(self):
            url = self.base_url + '/favorites'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            time.sleep(2)
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            # HelperTestBase.clickAndWait(self, "[data-test-id='favorites']")
            # time.sleep(3)
            NavigationMenuPage.clickFavoriteList(self)
            self.assertEqual(url, HelperTestBase.getURL(self))

            # Test scope - Click on the 'Watchlist' icon => The 'Watchlist' page is opened:
            # @pytest.mark.skip

        def test_clickWatchlistButton(self):
            url = self.base_url + '/watchlist'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            # HelperTestBase.clickAndWait(self, "[data-test-id='watchlist']")
            # time.sleep(3)
            NavigationMenuPage.clickWatchlist(self)
            self.assertEqual(url, HelperTestBase.getURL(self))

            # Test scope - Click on Messages icon => The Messages page is opened:
            # @pytest.mark.skip

        def test_clickMessagesButton(self):
            url = self.base_url + '/dialogs'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            time.sleep(1)
            HelperTestBase.clickAndWait(self, "[data-test-id='dialogs']")
            # NavigationMenuPage.clickMessages(self)
            time.sleep(5)
            self.assertEqual(url, HelperTestBase.getURL(self))


            # Test scope - Click on Reviews icon => The Reviews page is opened:

        # @pytest.mark.skip
        def test_clickReviewsButton(self):
            url = self.base_url + '/reviews'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='reviews']")
            # NavigationMenuPage.clickReviews(self)
            time.sleep(3)
            self.assertEqual(url, HelperTestBase.getURL(self))

        # Test scope - Click on Analytics icon => The Analytics page is opened:
        # @pytest.mark.skip
        def test_clickAnalyticsButton(self):
            url = self.base_url + '/analytics'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestbiy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
            # HelperTestBase.clickAndWait(self, "[data-test-id='analytics']")
            NavigationMenuPage.clickAnalytics(self)
            time.sleep(3)
            self.assertEqual(url, HelperTestBase.getURL(self))
