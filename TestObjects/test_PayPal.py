import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.PayPalPage import PayPalPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from PageObjects.ShoppingListPage import ShoppingListPage


class TestPayPal(ShoppingListPage, NavigationMenuPage):
    '''"1.Click on 'PayPal' link => Choose a way to pay - PayPal"" screen is opened
2.Check the "Log in to your PayPal account" button => The"Log in to your PayPal account" button is present
3.Click on "Log in to your PayPal account" button => The "Pay with a PayPal account" page is opened.
4.Check the elements =>  There are present: Email address field, Password field, LogIn button


    '''

    # @pytest.mark.skip
    def test_PayPalFunction_FromCart(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        text = 'Choose a way to pay - PayPal'
        text3 = 'Pay with a PayPal account'
        text4 = 'Security Challenge - PayPal'
        text1 = 'Shopping Cart:'
        text2 = "In few seconds you'll be redirected to Paypal page to complete your payment."

        LoginPage.loginAction(self, 'Testnrozn', 'Ss123456')

        # prepeare to start:
        NavigationMenuPage.clickCart(self)
        ShoppingCartPage.deleteItemFromCart(self)
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        ShoppingListPage.sortAndSelectProduct(self)
        HelperTestBase.clickYesButton(self)
        NavigationMenuPage.clickCart(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='payBtn']"), True)
        ShoppingCartPage.clickPayButton(self)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))

        time.sleep(3)
        self.assertEqual(text, HelperTestBase.getTitle(self))
        time.sleep(10)
        self.assertIs(True, PayPalPage.checkLogInToYourPayPalAccountButton(self))
        time.sleep(5)
        PayPalPage.clickLogInPayPalButton(self)
        time.sleep(3)
        self.assertIs(True, PayPalPage.checkEmailFieldPresent(self))
        self.assertIs(True, PayPalPage.checkPasswordFieldPresent(self))
        self.assertIs(True, PayPalPage.checkLogInButtonPresent(self))

    # @pytest.mark.skip
    def test_PayPalFunction_FromProductDetails(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        text = 'Choose a way to pay - PayPal'
        text3 = 'Pay with a PayPal account'
        text4 = 'Security Challenge - PayPal'
        text1 = 'Shopping Cart:'
        text2 = "In few seconds you'll be redirected to Paypal page to complete your payment."

        LoginPage.loginAction(self, 'SellerTestcfz', 'Ss123456')

        # prepeare to start:
        NavigationMenuPage.clickCart(self)
        ShoppingCartPage.deleteItemFromCart(self)
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        # HelperTestBase.clickBackButton(self)
        ShoppingListPage.selectProduct(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"))
        HelperTestBase.clickAndWait(self, "[data-test-id='detailBuyNow']")

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        time.sleep(3)
        self.assertEqual(text, HelperTestBase.getTitle(self))
        time.sleep(10)
        self.assertIs(True, PayPalPage.checkLogInToYourPayPalAccountButton(self))
        # time.sleep(5)
        # PayPalPage.clickLogInPayPalButton(self)
        # time.sleep(10)
        # self.assertIs(True, PayPalPage.checkEmailFieldPresent(self))
        # self.assertIs(True, PayPalPage.checkPasswordFieldPresent(self))
        # self.assertIs(True, PayPalPage.checkLogInButtonPresent(self))
