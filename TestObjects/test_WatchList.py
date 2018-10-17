import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.WatchListPage import WatchListPage


class TestWatchList(WatchListPage):
    # Test scope - check elements on Watchlist page:

    #@pytest.mark.skip
    def test_checkElements(self):
        url2 = self.base_url + '/watchlist'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Testvqlap', 'Ss123456')
        # LoginPage.loginAction(self, 'Testvqlap', 'Ss123456')
        LoginPage.loginAction(self, 'Testdcjkt', 'Ss123456')
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='watchlist']")
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchListPItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchListPRemoveItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)

    # Test scope - Buyer clicks on "<" button in the header =>	The Shopping List page is opened:
    # @pytest.mark.skip
    def test_BuyerClicksBackButton(self):
        url2 = self.base_url + '/watchlist'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Testvqlap', 'Ss123456')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        self.assertEqual(url, HelperTestBase.getURL(self))

        time.sleep(2)
        NavigationMenuPage.goToWatchListPage(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        # HelperTestBase.clickAndWait(self, "[data-test-id='shoppingLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        # HelperTestBase.waitURL(self, url)
        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # Test scope - Buyer clicks on "<" button in the header =>	The Inventory List page is opened:
    #@pytest.mark.skip
    def test_SellerClicksBackButton(self):
        url2 = self.base_url + '/watchlist'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")

        time.sleep(5)
        self.assertEqual(url1, HelperTestBase.getURL(self))

        NavigationMenuPage.clickWatchlist(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url1, HelperTestBase.getURL(self))



    #@pytest.mark.skip
    def test_deleteAddItemToWL(self):
        # Test scope - delete item from Watch List => the item deleted, the Empty text is displayed
        url2 = self.base_url + '/watchlist'
        url = self.base_url + '/shopping-list'
        text='Empty'
        driver = self.driver
        driver.get(self.base_url)

        LoginPage.loginAction(self, 'Testgzcks', 'Ss123456')
        NavigationMenuPage.clickWatchlist(self)
        WatchListPage.removeFromWatchList(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        time.sleep(4)
        self.assertIn(text, self.driver.page_source)

        # Test scope - add to Watch List => the item added
        self.driver.refresh()
        WatchListPage.addToWatchList(self)
        ProductDetailsPage.clickBackButton(self)
        time.sleep(3)
        NavigationMenuPage.clickWatchlist(self)

        time.sleep(2)
        self.assertIs(WatchListPage.checkItemPresent(self), True)

        # def test_add_to_WL_and_remove(self):
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     LoginPage.loginAction(self, 'Test', "Test12345")
        #
        #     HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProductName_0']")
        #     wait = WebDriverWait(self.driver, 60)
        #     element = wait.until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='abstractListProductTitle_0']")))
        #     el_name = element.text
        #     HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        #     HelperTestBase.reliableClick(self, "[data-test-id='addToWL']")
        #     HelperTestBase.reliableClick(self, "[data-test-id='searchResultsLink']")
        #     HelperTestBase.reliableClick(self, "[data-test-id='footerMainBtn']")
        #     HelperTestBase.reliableClick(self, "[data-test-id='watchlist']")
        #
        #     time.sleep(5)
        #     self.assertIn(el_name, driver.page_source)
        #
        #     HelperTestBase.reliableClick(self, "[class='icon-trash-empty']")
        #
        #     time.sleep(3)
        #     self.assertNotIn(el_name, driver.page_source)
