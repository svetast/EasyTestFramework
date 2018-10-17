import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.ReviewsPage import ReviewsPage


class TestProductDetails(ProductDetailsPage):
    # Valid user credentials - Testeuwqw / Ss123456 =>   Don't add new item  !!!!!!

    #  Test scope - the buttons are present:  BizPix, AddToWatchList,  AddToFavList, Report, Price, Alert, BuyNow, IconRightOopen.
    # the texts are present:  See Reviews, Price Alert, Quantity, Non GMO, Organic, Delivery is offered, Market pickup is offered,
    # Country of Origin, Production date, Product description


    # @pytest.mark.skip
    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        text1 = 'See Reviews'
        text2 = 'Price Alert'
        text3 = 'Quantity'
        text4 = 'Non GMO'
        text5 = 'Organic'
        text6 = 'Delivery is offered'
        text7 = 'Market pickup is offered'
        text8 = 'Country of Origin'
        text9 = 'Production date'
        text10 = 'Product description'
        text11 = "Test apple"
        # Seller name:
        text12 = 'SA1'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Teststdpp', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='addToWL']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='addToFL']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAlertQty']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailTitle']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAddToCart']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchResultsLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='BiziPix']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailRateStars']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailRate']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='showReviews']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailPriceQty']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAlertQty']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)
        self.assertIn(text1, driver.page_source)
        self.assertIn(text2, driver.page_source)
        self.assertIn(text3, driver.page_source)
        self.assertIn(text4, driver.page_source)
        self.assertIn(text5, driver.page_source)
        self.assertIn(text6, driver.page_source)
        self.assertIn(text7, driver.page_source)
        self.assertIn(text8, driver.page_source)
        self.assertIn(text9, driver.page_source)
        self.assertIn(text10, driver.page_source)
        # self.assertIn(text11, driver.page_source)
        self.assertIn(text12, driver.page_source)
        # click on "< " button => search results page is opened:
        ProductDetailsPage.clickBackButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='resultsCount']"), True)
        time.sleep(2)
        # click on "< " button => Shopping List page is opened:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(2)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_addQuantitySuccess(self):
        # "If a product is available: >=2 Each: type "2" into quantity field=> The 'Cost' increased 2 times:
        url = self.base_url + '/shopping-list'
        text1 = '$8.00'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testeuwqw', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.addQuantity(self, '2')
        time.sleep(3)
        self.assertIn(text1, driver.page_source)

    #    @pytest.mark.skip
    def test_addQuantityNotAvailable(self):
        # "If a product is available: =5 Each: type "6" into quantity field=> "Sorry, your demand exceeds available quantity of 5 Each:"
        # message is displayed:
        url = self.base_url + '/shopping-list'
        text1 = 'Sorry, your demand exceeds available quantity'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testeuwqw', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.addQuantity(self, '98')
        time.sleep(6)
        self.assertIn(text1, self.driver.page_source)

        #  @pytest.mark.skip

    def test_addQuantityZero(self):
        # Test scope - type "0" into quantity field => Cost '$0.00' is displayed:
        # message is displayed:
        url = self.base_url + '/shopping-list'
        text1 = 'Quantity cannot be negative!'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testeuwqw', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.addQuantity(self, '0')
        self.assertIn(text1, driver.page_source)

        #   @pytest.mark.skip

    def test_addQuantityInvalidData(self):
        # Test scope - type an invalid data "@#$%" into quantity field => the field validates inputted data =>the quantity field is empty

        url = self.base_url + '/shopping-list'
        text1 = ''
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testeuwqw', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.addQuantity(self, '@#$%asdfg')
        self.assertEqual(text1, ProductDetailsPage.getResultAddQuantity(self))

        #  @pytest.mark.skip

    def test_addRemoveProductFromCart(self):
        # Test scope - click on AddToCart => The Iten has added to cart. RemoveFromCart is displayed => The Iten has added to cart.  Click on RemoveFromCart =>
        # AddToCart  is displayed, the cart is empty:

        url = self.base_url + '/shopping-list'
        url3 = self.base_url + '/cart'
        text1 = 'Item has been successfully added.'
        text2 = 'Item has been successfully removed.'
        text3 = 'Your cart is currently empty'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testkwayl', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        # Test scope - click on AddToCart => 'The Iten has added to cart' message is displayed, 'RemoveFromCart' button is displayed :
        # ProductDetailsPage.clickAddToCart(self)
        HelperTestBase.reliableClick(self, "[data-test-id='detailAddToCart']")
        self.assertEqual(text1, ProductDetailsPage.getMessage(self))
        HelperTestBase.clickYesButton(self)
        # ProductDetailsPage.clickOk(self)
        self.driver.refresh()
        time.sleep(5)

        NavigationMenuPage.clickCart(self)
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.driver.refresh()
        # Test scope - click on RemoveFromCart => 'Item has been successfully removed.' message is displayed, 'AddToCart' button is displayed :

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.clickAddToCart(self)
        self.assertEqual(text2, ProductDetailsPage.getMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(2)
        NavigationMenuPage.clickCart(self)
        time.sleep(3)
        self.assertIn(text3, self.driver.page_source)

    # @pytest.mark.skip
    def test_checkAddToCartBuyNowFromYourself(self):
        ### Test scope - click on AddToCart / BuyNow  => 'You cannot buy from yourself!' is displayed:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/cart'
        text = 'Error:'
        text1 = 'You cannot buy from yourself!'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTesthfr', 'Ss123456')

        # click on AddToCart = > 'You cannot buy from yourself!' is displayed:

        ProductDetailsPage.addProductToCart(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ### Test scope - click on BuyNow  => 'You cannot buy from yourself!' is displayed:
        ProductDetailsPage.clickBuyNow(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAddToCart']"), True)

        # @pytest.mark.skip
    def test_clickReviews(self):
        ### click on Reviews button => Add Review page is opened:
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/reviews'
        text = 'Add Review'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testvcpak', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.clickReviewsButton(self)
        self.assertIs(True, ReviewsPage.checkElemPresent(self))
        # self.assertIn(text, self.driver.page_source)

        # @pytest.mark.skip

    def test_checkFavListIcon(self):
        ### Test scope - click on AddFavList => RemoveFavList is displayed, refresh page => RemoveFavList is displayed:
        url = self.base_url + '/shopping-list'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testviuug', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        time.sleep(2)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='addToFL']"))

        # ProductDetailsPage.addToFavoriteList(self)
        HelperTestBase.reliableClick(self, "[data-test-id='addToFL']")
        time.sleep(2)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='removeFromFL']"))
        self.driver.refresh()
        time.sleep(10)
        ProductDetailsPage.goToProductDetailsPage(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='removeFromFL']"))
        # ProductDetailsPage.removeFromFavoriteList(self)
        HelperTestBase.reliableClick(self, "[data-test-id='removeFromFL']")
        time.sleep(2)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='addToFL']"))

    # @pytest.mark.skip
    def test_checkWatchListIcon(self):
        ### ### Test scope - click on AddWatchList => RemoveWatchList is displayed, refresh page => RemoveWatchList is displayed:
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testviuug', 'Ss123456')

        ProductDetailsPage.goToProductDetailsPage(self)
        time.sleep(2)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='addToWL']"))
        HelperTestBase.reliableClick(self, "[data-test-id='addToWL']")
        time.sleep(2)
        # ProductDetailsPage.addToWatchList(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='removeFromWL']"))
        self.driver.refresh()
        time.sleep(10)
        ProductDetailsPage.goToProductDetailsPage(self)
        time.sleep(2)
        # ProductDetailsPage.removeFromWatchList(self)
        HelperTestBase.reliableClick(self, "[data-test-id='removeFromWL']")
        time.sleep(2)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='addToWL']"))
