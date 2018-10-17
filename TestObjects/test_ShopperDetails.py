from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.ShopperDetailsPage import ShopperDetailsPage


class TestShopperDetails(ShopperDetailsPage):
    ###Test scope - check elements on Shopper Details page:
    # @pytest.mark.skip
    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchResultsLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='toggleFLStatus']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperName']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperRate']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailRate']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperPhone']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperAddress']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperWebPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperMail']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToChat']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchForShopper']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shopperImage']"), True)
        # self.assertIs(ShopperDetailsPage.checkImagePresent(self), True)



        ###Test scope - Click on Favorite icon => the color is red, refresh page => the color is red.
        ###             Click on red Favorite icon => the color isn't red.

    # @pytest.mark.skip
    def test_clickFavoriteIcon(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickFavoriteButton(self)
        driver.refresh()
        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickFavoriteButton(self)
        ShopperDetailsPage.clickBackLink(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"))

    #@pytest.mark.skip
    def test_clickBack(self):
        ##Test scope - click on "<" icon => Product Details  page is opened:
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickBackLink(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"))



        ###Test scope - Click on "ItemsForSale" icon (for SA1 product)  => "SA1's items" page is opened:

    #@pytest.mark.skip
    def test_clickItemsForSale(self):
        url = self.base_url + '/shopping-list'
        text = "SA1's items"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickItemsForSaleButton(self)
        self.assertEqual(text, HelperTestBase.getText(self, "[data-test-id='searchKey']"))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_1']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_2']"), True)

        ###Test scope - Click on "Contact Seller" icon   => The text input is opened:
        # @pytest.mark.skip

    def test_clickContactSeller(self):
        url2 = self.base_url + '/shopping-list'
        url = self.base_url + '/chat-room?interlocutor=SA1'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        ###Test scope - Click on "Contact Seller" icon   => Seller page is opened:
        ShopperDetailsPage.clickContactSellerButton(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='sendMessage']"))

        # self.assertIs(True, HelperTestBase.checkElementPresent(self, 'message'))

    #@pytest.mark.skip

    def test_checkPopUp(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text1 = 'Send mail to salemazkoor@gmail.com ?'
        text2 = "Open 'www.bizibaza.com'?"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testnrxei', 'Ss123456')

        ShopperDetailsPage.clickSellerName(self)
        # Test scope - click on shopper Email => 'Send mail to salemazkoor@gmail.com ?' is displayed:
        ShopperDetailsPage.clickShopperMail(self)

        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        # HelperTestBase.clickYesButton(self)

        # Test scope - click on Cancel => Shopper Details is displayed:
        HelperTestBase.clickCancelButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperName']"), True)

        # Test scope - click on shopper web page  => 'Open www.bizibaza.com ?' is displayed:
        ShopperDetailsPage.clickShopperWebPage(self)
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))

        # Test scope - click on Cancel => Shopper Details is displayed:
        HelperTestBase.clickCancelButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='ShopperName']"), True)
