import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from PageObjects.ShoppingListPage import ShoppingListPage


class TestChoosingProduct(ShoppingListPage, NavigationMenuPage):
    # Valid user credentials - Testeuwqw / Ss123456

    # Test scope - Click on the Chocolate on items list > choosing Bisou Noir 100% Blend #3 Dark Chocolate product,
    #  click on it =>	The 'Buy now' button is displayed


    def test_choosingProduct(self):
        ###Test scope : User selected the item from ShoppingList, added item to Cart:
        text2 = 'Shopping Cart:'
        text3 = 'Item has been successfully added.'
        text4 = 'Your cart is currently empty'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(4)

        ShoppingListPage.selectProduct(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAddToCart']"), True)

        HelperTestBase.clickAndWait(self, "[data-test-id='detailAddToCart']")
        time.sleep(2)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        #### return test data:
        NavigationMenuPage.clickCart(self)
        ShoppingCartPage.deleteItemFromCart(self)
        time.sleep(3)
        self.assertIn(text4, self.driver.page_source)
