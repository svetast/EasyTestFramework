import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from PageObjects.ShoppingListPage import ShoppingListPage


class TestShoppingCart(ShoppingCartPage):
    # @pytest.mark.skip
    def test_111111111111CheckTestData(self):
        # Test scope - Click on "<" button in the header =>	The Shopping List page is opened:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'Your cart is currently empty'
        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testxjerk', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.driver.refresh()
        time.sleep(2)


        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testupcrs', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.driver.refresh()
        time.sleep(2)

        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testffkod', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        self.assertIn(text1, self.driver.page_source)
        self.driver.refresh()
        time.sleep(2)


        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testvhksx', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.driver.refresh()
        time.sleep(2)


        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testsitlh', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.driver.refresh()
        time.sleep(2)


        ###
        LoginPage.loginActionWithoutKeepMeLogged(self, 'Testoxbfn', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_1']"), True)
        self.driver.refresh()
        time.sleep(2)

    # @pytest.mark.skip
    def test_clickBackIcon(self):
        # Test scope - Click on "<" button in the header =>	The Shopping List page is opened:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testvrjec', 'Ss123456')

        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='cart']")
        time.sleep(3)
        # NavigationMenuPage.clickCart(self)
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text1 = 'Sub total:'
        text2 = 'Item expires:'
        text3 = 'Quantity'
        text4 = 'Total cost'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testxjerk', 'Ss123456')
        time.sleep(5)
        NavigationMenuPage.clickCart(self)
        HelperTestBase.waitElement(self, "[data-test-id='cartItemImage_0']")
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemTitle_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemImage_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemExpiresIn_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemQnt_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRemoveItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='payBtn']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartRefreshItem_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartTotal']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemTotalCost_0']"), True)
        self.assertIs(ShoppingCartPage.checkCartBadge(self), True)
        self.assertIn(text1, driver.page_source)
        self.assertIn(text2, driver.page_source)
        self.assertIn(text3, driver.page_source)
        self.assertIn(text4, driver.page_source)

    # @pytest.mark.skip
    def test_deleteItemAddItem(self):
        # Test scope - click on delete button - the product deleted from Cart:

        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text1 = 'Your cart is currently empty'
        text2 = 'Shopping Cart:'
        text3 = 'Item has been successfully added.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testupcrs', 'Ss123456')
        time.sleep(4)
        NavigationMenuPage.clickCart(self)
        time.sleep(2)
        ShoppingCartPage.deleteItemFromCart(self)
        time.sleep(2)
        self.assertIn(text1, self.driver.page_source)
        time.sleep(2)
        ####### return test to start position:
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        ShoppingCartPage.addItemToCart(self)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        driver.refresh()
        time.sleep(5)
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='cartRemoveItem_0']"), True)

    #@pytest.mark.skip
    def test_checkPayFunction(self):
        # Test scope - click on delete button - check PAY on Cart page:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        title = 'Choose a way to pay - PayPal'
        text2 = 'Your cart is currently empty'
        text1 = 'Shopping Cart:'
        text3 = 'Item has been successfully added.'
        urlPP = 'https://www.paypal.com'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testffkod', 'Ss123456')
        time.sleep(4)
        HelperTestBase.waitSettingsButton(self)

        #### prepeare test data:
        ShoppingListPage.sortAndSelectProduct(self)
        time.sleep(5)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        NavigationMenuPage.clickCart(self)
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        time.sleep(5)
        ShoppingCartPage.clickPayButton(self)
        time.sleep(15)
        self.assertEqual(title, HelperTestBase.getTitle(self))

        ####### return the test to start position: ###############
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(10)
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cartItemTitle_0']"), True)
        ShoppingCartPage.deleteItemFromCart(self)
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

    #@pytest.mark.skip
    def test_checkPayButtonAfterRefresh(self):
        # Test scope - check PAY button after clicked on Refresh item button:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        title = 'Choose a way to pay - PayPal'
        text1 = 'Your cart is currently empty'
        text2 = 'Shopping Cart:'
        text3 = 'Item has been successfully added.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testlbhhl', 'Ss123456')
        NavigationMenuPage.clickCart(self)
        time.sleep(2)

        ShoppingCartPage.clickRefreshButton(self)
        time.sleep(5)
        ShoppingCartPage.clickPayButton(self)
        time.sleep(10)
        self.assertEqual(title, HelperTestBase.getTitle(self))

    #@pytest.mark.skip
    def test_checkValidQuantity(self):
        # Test scope - add valid quantity :
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text1 = '$8.00'
        text2 = '$4.00'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testfkvec', 'Ss123456')
        time.sleep(3)
        NavigationMenuPage.clickCart(self)
        HelperTestBase.setQuantity(self, "[data-test-id='cartItemQnt_0']", '2')
        time.sleep(2)
        self.assertEqual(text2, HelperTestBase.getText(self, "[data-test-id='cartTotal']"))
        self.assertEqual(text2, HelperTestBase.getText(self, "[data-test-id='cartItemTotalCost_0']"))
        driver.refresh()
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.wait(self, "[data-test-id='cart']")
        HelperTestBase.clickAndWait(self, "[data-test-id='cart']")
        time.sleep(2)
        HelperTestBase.setQuantity(self, "[data-test-id='cartItemQnt_0']", '1')
        time.sleep(2)
        self.assertEqual(text2, HelperTestBase.getText(self, "[data-test-id='cartTotal']"))
        self.assertEqual(text2, HelperTestBase.getText(self, "[data-test-id='cartItemTotalCost_0']"))

    #@pytest.mark.skip
    def test_checkZeroQuantity(self):
        # Test scope - add the Zero quantity = > the error message is displayed:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text1 = 'Error:'
        text2 = 'Some of the items have their booking expired! Please, refresh their status and try again.'
        text3 = '$12.00'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testyzccc', 'Ss123456')
        time.sleep(4)

        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='dialogs']")
        time.sleep(3)

        # NavigationMenuPage.clickCart(self)
        time.sleep(5)
        HelperTestBase.setQuantity(self, "[data-test-id='cartItemQnt_0']", '3')
        self.assertEqual(text3, HelperTestBase.getText(self, "[data-test-id='cartTotal']"))

        HelperTestBase.setQuantity(self, "[data-test-id='cartItemQnt_0']", '0')
        time.sleep(2)
        ShoppingCartPage.clickPayButton(self)
        time.sleep(1)
        self.assertEqual(url2, HelperTestBase.getURL(self))

    #@pytest.mark.skip

    def test_checkPayStatusAfterProductDeleted(self):
        #### Test scope - Click on the 'Remove from cart' button and check PAY link	=> The PAY link isn't active
        title = 'Pay with a PayPal account - PayPal'
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text1 = 'Your cart is currently empty'
        text2 = 'Shopping Cart:'
        text3 = 'Item has been successfully added.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testvhksx', 'Ss123456')
        time.sleep(3)
        NavigationMenuPage.clickCart(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='cartRemoveItem_0']")
        time.sleep(5)
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickAndWait(self, "[data-test-id='payBtn']")
        self.assertIsNot(title, HelperTestBase.getTitle(self))
        ###returt the test data:
        self.driver.refresh()
        ShoppingCartPage.addItemToCart(self)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

    # @pytest.mark.skip

    def test_addQantity(self):
        ### Test scope - Test the 'Quantity' on Cart page:
        url = self.base_url + '/shopping-list'
        text = 'Error:'
        text2 = 'Your demand exceeds proposal.'
        text3 = '$9.00'
        text4 = '$6.00'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testsitlh', 'Ss123456')
        time.sleep(4)
        self.assertEqual(url, HelperTestBase.getURL(self))
        NavigationMenuPage.clickCart(self)

        ### Test scope - Type the "6" into 'Quantity' field (if available 5) =>	"Error! Your demand exceeds proposal." is displayed


        ShoppingCartPage.addQuantity(self, '10')
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ### Test scope - Type the "3" into 'Quantity' field.	The 'Sub total' increased 3 times, the 'Total cost' increased 3 times:

        ShoppingCartPage.addQuantity(self, '3')
        self.assertEqual(text3, HelperTestBase.getText(self, "[data-test-id='cartItemSubtotal_0']"))

        ##### Type the "-2" into 'Quantity' field	=> The "2" is displayed in 'Quantity' field
        ShoppingCartPage.addQuantity(self, '-2')
        self.assertEqual(text4, HelperTestBase.getText(self, "[data-test-id='cartItemSubtotal_0']"))

        #  @pytest.mark.skip
    def test_add_to_SC_and_remove(self):
        driver = self.driver
        driver.get(self.base_url)
        text2 = 'Your cart is currently empty'
        text3 = "Item has been successfully added."
        text4 = 'Shopping Cart:'

        LoginPage.loginAction(self, 'Test', "Test12345")
        time.sleep(4)
        ShoppingCartPage.addItemToCart(self)
        self.assertEqual(text4, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        NavigationMenuPage.clickCart(self)
        HelperTestBase.reliableClick(self, "[data-test-id='cartRemoveItem_0']")
        time.sleep(5)
        self.assertIn(text2, self.driver.page_source)

    #@pytest.mark.skip
    def test_ShoppingCart_count(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Test', "Test12345")
        time.sleep(4)

        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        time.sleep(3)

        qtyInp = driver.find_element_by_css_selector("[data-test-id='abstractListProductQty_0']")
        qtyInp.click()
        qtyInp.send_keys("1")
        time.sleep(3)

        openBtn = driver.find_elements_by_class_name("abstract-list__product__open")[0]
        openBtn.click()
        time.sleep(3)

        qtyInpDetails = driver.find_element_by_css_selector("[data-test-id='detailPriceQty']")
        qtyInpDetailsValue = qtyInpDetails.get_attribute("value")
        self.assertEqual("1", qtyInpDetailsValue)
