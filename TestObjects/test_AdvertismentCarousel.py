import time

from HelperTestBase import HelperTestBase
from PageObjects.AdvertismentPage import AdvertismentPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestAdvertismentCarousel(AdvertismentPage):
    def test_checkAdvertisment(self):
        # Test scope - Click on an advertisement carousel => the Product Details page is opened:
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        self.assertEqual(url, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='carouselImgUrl']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='carouselImgUrl']")
        time.sleep(2)
        # Test scope - The 'Add To Cart' and 'Buy' buttons are present:
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailAddToCart']"), True)
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailBuyNow']"), True)
        # Test scope - click on < button => the Shopping List page is opened:
        HelperTestBase.clickAndWait(self, "[data-test-id='searchResultsLink']")
        # Test scope - Check that NavMenu button is present:
        HelperTestBase.checkElementPresent(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        # Test scope - Click on NavMenu button => The NavMenu is opened:
        NavigationMenuPage.clickNavMenuButton(self)
        HelperTestBase.waitElement(self, "[data-test-id='cart']")
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cart']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profile']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchlist']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favorites']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='reviews']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analytics']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialogs']"), True)

        # @pytest.mark.skip

    def test_checkAdvertisment0(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            self.assertEqual(url, HelperTestBase.getURL(self))
            # Test scope - Click on 1th advertisement carousel => the Product Details page is opened:
            AdvertismentPage.clickOnImage0(self)
            time.sleep(2)
            # Test scope - The 'Add To Cart' and 'Buy' buttons are present:
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailAddToCart']"), True)
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailBuyNow']"), True)

        # @pytest.mark.skip

    def test_checkAdvertisment1(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            self.assertEqual(url, HelperTestBase.getURL(self))
            # Test scope - Click on 2th advertisement carousel => the Product Details page is opened:


            AdvertismentPage.clickOnImage1(self)
            time.sleep(2)
            # Test scope - The 'Add To Cart' and 'Buy' buttons are present:
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailAddToCart']"), True)
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailBuyNow']"), True)

        # @pytest.mark.skip

    def test_checkAdvertisment2(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            self.assertEqual(url, HelperTestBase.getURL(self))
            # Test scope - Click on 3th advertisement carousel => the Product Details page is opened:
            AdvertismentPage.clickOnImage2(self)
            time.sleep(2)
            # Test scope - The 'Add To Cart' and 'Buy' buttons are present:
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailAddToCart']"), True)
            self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='detailBuyNow']"), True)
