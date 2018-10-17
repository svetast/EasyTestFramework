import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase
from PageObjects.FavoritesPage import FavoritesPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestFavoritesList(FavoritesPage):
    # Test scope - check elements on Favorites List page:

    # @pytest.mark.skip
    def test_checkElements(self):
        url2 = self.base_url + '/favorites'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testodznv', 'Ss123456')
        time.sleep(3)

        self.assertEqual(url, HelperTestBase.getURL(self))
        NavigationMenuPage.clickFavoriteList(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPRemoveItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPRate_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPTitle_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListDescription_0']"), True)

    # Test scope - Buyer clicks on "<" button in the header of Favorites list =>	The Shopping List page is opened:
    # @pytest.mark.skip
    def test_BuyerClicksBackButton(self):
        url2 = self.base_url + '/favorites'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnqqfl', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        NavigationMenuPage.clickFavoriteList(self)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        #HelperTestBase.waitElement1(self, "[data-test-id='shoppingLink']")
        time.sleep(1)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        self.assertEqual(url, HelperTestBase.getURL(self))

    # Test scope - Seller clicks on "<" button in the header of Favorites list =>	The Inventory List page is opened:
    # @pytest.mark.skip
    def test_SellerClicksBackButton(self):
        url2 = self.base_url + '/favorites'
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
        time.sleep(3)

        NavigationMenuPage.clickSellerButton(self)
        time.sleep(3)
        NavigationMenuPage.clickFavoriteList(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url1, HelperTestBase.getURL(self))

    # Test scope - delete item from Favorites List => the item deleted
    @pytest.mark.skip
    def test_deleteItem(self):
        url2 = self.base_url + '/favorites'
        url = self.base_url + '/shopping-list'
        text='Empty'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testgzcks', 'Ss123456')
        NavigationMenuPage.clickFavoriteList(self)
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPRemoveItem_0']"), True)
        HelperTestBase.clickAndWait(self, "[data-test-id='favListPRemoveItem_0']")
        time.sleep(5)
        self.assertIn(text, self.driver.page_source)
        # self.assertEqual(text, HelperTestBase.getText1(self, "list__ul__empty-list"))

        ####returm the test data to start state:
        self.driver.refresh()
        # Test scope - add item to Favorites List => the item added
        FavoritesPage.addToFavList(self)
        self.driver.refresh()
        time.sleep(10)
        NavigationMenuPage.clickFavoriteList(self)
        time.sleep(3)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favListPRemoveItem_0']"), True)

    # @pytest.mark.skip
    def test_add_to_FL_and_remove(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Test', "Test12345")

        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='abstractListProductTitle_0']")))
        el_name = element.text
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")

        HelperTestBase.reliableClick(self, "[data-test-id='addToFL']")
        HelperTestBase.reliableClick(self, "[data-test-id='searchResultsLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.reliableClick(self, "[data-test-id='favorites']")

        time.sleep(2)
        self.assertIn(el_name, driver.page_source)

        HelperTestBase.reliableClick(self, "[data-test-id='favListPRemoveItem_0']")

        time.sleep(3)
        self.assertNotIn(el_name, driver.page_source)
