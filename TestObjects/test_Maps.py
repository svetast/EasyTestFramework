import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SearchScreenPage import SearchScreenPage
from PageObjects.ShopperDetailsPage import ShopperDetailsPage
from PageObjects.ShoppingListPage import ShoppingListPage


class TestMaps(ShoppingListPage, SearchScreenPage):
    # @pytest.mark.skip
    def test_checkMapsOnSearchesPage(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/map-search'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='mapBtnTop']"), True)
        HelperTestBase.clickAndWait(self, "[data-test-id='mapBtnTop']")
        time.sleep(9)
        self.assertEqual(url1, HelperTestBase.getURL(self))

        # self.assertIs(ShopperDetailsPage.checkMarketsMapPresent(self), True)

    # @pytest.mark.skip
    def test_checkMapsOnEvent(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTesthtd', 'Ss123456')
        time.sleep(3)

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='inventoryItem-0']")

        ProductEditorPage.clickEventTitle(self)
        time.sleep(6)
        self.assertIs(ProductEditorPage.checkMapPresent(self), True)

        # @pytest.mark.skip
    def test_checkMapsOnShopperDetails(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        HelperTestBase.clickAndWait(self, "[data-test-id='carouselImgUrl']")
        time.sleep(2)
        ProductDetailsPage.clickSellerName(self)
        time.sleep(5)
        self.assertIs(ShopperDetailsPage.checkMapPresent(self), True)

    #@pytest.mark.skip
    def test_checkMapsOnMarketDetails(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        time.sleep(3)
        # HelperTestBase.clickSearch(self)
        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")
        SearchScreenPage.submitSearchMarket(self, 'Mars')
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(5)
        self.assertIs(SearchScreenPage.checkMarketTitlePresent(self), True)
        self.assertIs(SearchScreenPage.checkMapsPresent(self), True)

    # @pytest.mark.skip
    def test_checkMapsOnSearch(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        time.sleep(3)
        # HelperTestBase.clickSearch(self)
        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")
        SearchScreenPage.submitSearchMarket(self, 'Mars')
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='mapBtnTop']")
        time.sleep(3)
        self.assertEqual(url1, HelperTestBase.getURL(self))

    #@pytest.mark.skip
    def test_checkMapsIfItemNotFound(self):
        # Test scope : search results for item 'kolobok' => Map isn't present
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'Search for:'
        text1 = 'Gladiolus'
        text0 = 'Error:'
        text2 = 'Input data error'
        text3 = 'Results: 0'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(5)

        HelperTestBase.clickSearch(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SearchScreenPage.submitSearchItem(self, 'kolobok')
