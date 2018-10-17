import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage


class TestNavigationMenuBuyer(NavigationMenuPage):
    # Test scope - Buyer clicks on the "+" button  => The navigation menu is displayed => Cart, Messages, Profile, Watchlist,
    # Reviewes, Analytics, Favorites are present:

    # @pytest.mark.skip
    def test_clickNavigationMenuButton(self):
        url = self.base_url + '/login'
        url2 = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
        #NavigationMenuPage.clickNavMenuButton(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")

        time.sleep(3)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profile']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchlist']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favorites']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='reviews']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analytics']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialogs']"), True)
        NavigationMenuPage.clickNavMenuButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profile']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchlist']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favorites']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='reviews']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analytics']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialogs']"), False)

    # @pytest.mark.skip
    def test_checkCountersOnNavigationMenu(self):
        # Test scope - Buyer clicks on the "+" button  => The navigation menu is displayed => The counters are displayed on [Cart, Messages, Favlist, Watchlist] icon:
        url2 = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Testrnqfo', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")

        # NavigationMenuPage.clickNavMenuButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='messageCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchListCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListCounter']"), True)

    # @pytest.mark.skip
    def test_checkCountersAddDelete(self):
        # Test scope - if [Cart,Favlist, Watchlist] hasn't item => The counters aren't displayed on [Cart, Favlist, Watchlist] icon:
        url2 = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'Your cart is currently empty'

        LoginPage.loginAction(self, 'Testvudca', 'Ss123456')
        NavigationMenuPage.clickNavMenuButton(self)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='cartItemCounter']")), 0)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='watchListCounter']")), 0)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='favListCounter']")), 0)
        NavigationMenuPage.clickNavMenuButton(self)
        # Test scope - Buyer added item to [Cart,Favlist, Watchlist] => The counters are displayed on [Cart, Favlist, Watchlist] icon:

        ProductDetailsPage.addProductToCartWatchlistFavorites(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        NavigationMenuPage.clickNavMenuButton(self)
        time.sleep(3)

        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchListCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListCounter']"), True)
        # Test scope - Buyer deleted item from [Cart,Favlist, Watchlist] => The counters aren't displayed on [Cart, Favlist, Watchlist] icon:
        NavigationMenuPage.removeProductFromCartWatchlistFavorites(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        NavigationMenuPage.clickNavMenuButton(self)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='cartItemCounter']")), 0)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='watchListCounter']")), 0)
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='favListCounter']")), 0)

    # @pytest.mark.skip
    def test_checkSwitchSellerModeBuyerMode(self):
        # Test scope: For Seller user => Inventory list page is opened, for Shopper user => Shopping List page is opened:
        url = self.base_url + '/cart'
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')

        # Check the Buyer mode:
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(1)
        HelperTestBase.clickAndWait(self, "[data-test-id='cart']")
        time.sleep(2)
        #NavigationMenuPage.clickCart(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        # Check the Seller mode:
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(2)
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        #
        # @pytest.mark.skip
        #
        # def test_checkSellerModeForBuyer(self):
        #     #  Test scope: Buyer can't open Seller mode:
        #     url = self.base_url + '/cart'
        #     url1 = self.base_url + '/inventory-list'
        #     url2 = self.base_url + '/shopping-list'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Testhwqla', 'Ss123456')
        #     # LoginPage.loginAction(self, 'Testeuwqw', 'Ss123456')
        #     # Check the Seller mode:
        #     NavigationMenuPage.clickSellerButton(self)
        #     time.sleep(2)
        #     self.assertEqual(url2, HelperTestBase.getURL(self))
        #
        #     # Test scope - Buyer clicks on the 'Profile' icon => The 'Your profile' page is opened.
        #
        # @pytest.mark.skip
        # def test_clickProfileButton(self):
        #     url = self.base_url + '/profile'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        #     NavigationMenuPage.clickProfile(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #     # Test scope - Click < button on 'Profile' page => The 'Shopping List' page is opened.
        #
        #     # Test scope - Buyer clicks on the 'Favorites' icon => The 'Your favorite list:' page is opened.
        #
        # @pytest.mark.skip
        # def test_clickFavoritesButton(self):
        #     url = self.base_url + '/favorites'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        #     NavigationMenuPage.clickFavoriteList(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #
        #     # Test scope - Buyer clicks on the 'Watchlist' icon => The 'Watchlist' page is opened:
        #
        # @pytest.mark.skip
        # def test_clickWatchlistButton(self):
        #     url = self.base_url + '/watchlist'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Testhwqla', 'Ss123456')
        #     # LoginPage.loginAction(self, 'Testvvndj', 'Ss123456')
        #     NavigationMenuPage.clickWatchlist(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #
        #     # Test scope -Buyer clicks on Messages icon => The Messages page is opened:
        #
        # @pytest.mark.skip
        # def test_clickMessagesButton(self):
        #     url = self.base_url + '/dialogs'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Testhwqla', 'Ss123456')
        #     # LoginPage.loginAction(self, 'Testvvndj', 'Ss123456')
        #     NavigationMenuPage.clickMessages(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #
        #
        #     # Test scope - Click on Reviews icon => The Reviews page is opened:
        #
        # @pytest.mark.skip
        # def test_clickReviewsButton(self):
        #     url = self.base_url + '/reviews'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Testhwqla', 'Ss123456')
        #     # LoginPage.loginAction(self, 'Testvvndj', 'Ss123456')
        #     NavigationMenuPage.clickReviews(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #
        # # Test scope - Click on Analytics icon => The Analytics page is opened:
        # @pytest.mark.skip
        # def test_clickAnalyticsButton(self):
        #     url = self.base_url + '/analytics'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Testhwqla', 'Ss123456')
        #     NavigationMenuPage.clickAnalytics(self)
        #     time.sleep(2)
        #     self.assertEqual(url, HelperTestBase.getURL(self))
