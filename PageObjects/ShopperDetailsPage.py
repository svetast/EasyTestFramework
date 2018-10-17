import time

from HelperTestBase import HelperTestBase


class ShopperDetailsPage(HelperTestBase):
    def ShopperDetailsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def checkColor(self):
        color = self.driver.find_element_by_css_selector(".navbar__right>img").get_attribute(self)
        return color

    def goToProductDetaisPage(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(1)

    def clickSellerName(self):
        self.goToProductDetaisPage()
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='showSeller']")

    def clickItemsForSaleButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='searchForShopper']")
        time.sleep(3)

    def clickContactSellerButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='goToChat']")
        time.sleep(4)

    def clickBackLink(self):
        HelperTestBase.reliableClick(self, "[data-test-id='searchResultsLink']")
        # HelperTestBase.waitSettingsButton(self)
        time.sleep(5)

    def clickFavoriteButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='toggleFLStatus']")
        time.sleep(6)

    def clickShoperPhone(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='ShopperPhone']")

    def clickShopperWebPage(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='ShopperWebPage']")

    def clickShopperMail(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='ShopperMail']")

    def checkMapPresent(self):
        state = self.driver.find_element_by_css_selector(
            "body > app-root > div > div > shopper-details > div > div.shopper-details > div > div.shopper-details__img > agm-map > div.agm-map-container-inner.sebm-google-map-container-inner > div > div > div:nth-child(1) > div:nth-child(3) > div").is_displayed()
        return state

    def checkImagePresent(self):
        state = self.driver.find_element_by_css_selector(
            "body > app-root > div > div > shopper-details > div > div.shopper-details > div > div.shopper-details__content-user > span").is_displayed()
        return state

    def checkMarketsMapPresent(self):
        state = self.driver.find_element_by_css_selector(
            "bbb").is_displayed()
        return state
