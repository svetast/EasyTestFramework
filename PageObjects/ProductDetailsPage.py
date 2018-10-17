import time

from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class ProductDetailsPage(NavigationMenuPage):
    def ProductPage(self):
        driver = self.driver
        driver.get(self.base_url)



    def goToProductDetailsPageUniversal(self, locatorList=None, locatorProduct=None):
        HelperTestBase.click(self, locatorList)
        HelperTestBase.click(self, locatorProduct)
        time.sleep(3)

    def goToProductDetailsPage(self):
        self.clickItemOnList()
        self.clickProduct()
        time.sleep(5)

    def clickItemOnList(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        time.sleep(2)

    def clickProduct(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(2)





    def clickAddToCart(self):
        HelperTestBase.click(self, "[data-test-id='detailAddToCart']")
        time.sleep(2)

    def addToFavoriteList(self):
        HelperTestBase.click(self, "[data-test-id='addToFL']")
        time.sleep(5)

    def removeFromFavoriteList(self):
        HelperTestBase.click(self, "[data-test-id='removeFromFL']")
        time.sleep(5)

    def addToWatchList(self):
        HelperTestBase.click(self, "[data-test-id='addToWL']")
        time.sleep(5)

    def removeFromWatchList(self):
        HelperTestBase.click(self, "[data-test-id='removeFromWL']")
        time.sleep(5)


    def clickBuyNow(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='detailBuyNow']")
        time.sleep(1)

    def clickBiziPix(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='BiziPix']")
        time.sleep(3)

    #  input the number into 'quantity' field on Product page:
    def addQuantity(self, number=None):
        elem = self.driver.find_element_by_css_selector("[data-test-id='detailPriceQty']")
        elem.clear()
        elem.send_keys(number)

    ##################################

    def click(self, locator=None):
        self.driver.find_element_by_css_selector(locator).click()

    def clickOk(self):
        self.driver.find_element_by_xpath("html/body/app-root/div/modal/div/div/button").click()


    #   'COMMAND a'   doesn't work in Mac OS by Chrome - FF  only :

    def addQuantityCopyPaste(self):
        elem1 = self.driver.find_element_by_css_selector("[data-test-id='detailPriceQty']")
        elem2 = self.driver.find_element_by_css_selector("[data-test-id='detailAlertQty']")
        elem2.clear()
        elem2.send_keys("-2")
        elem2.send_keys(Keys.SHIFT, Keys.UP)
        elem2.send_keys(Keys.COMMAND, 'c')  # copy
        elem1.send_keys(Keys.COMMAND, 'v')  # paste

    ####### The 'Helper' method -  for getting result after added quantity :##############

    def getResultAddQuantity(self):
        result = self.driver.find_element_by_id("qtyInput").text
        return result

    def getMessage(self):
        text = self.driver.find_element_by_css_selector(".modal__msg").text
        return text

    def clickReviewsButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='showReviews']")
        time.sleep(2)



    def clickCloseButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='closeButton']")
        time.sleep(2)

    def addProductToCart(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(1)
        HelperTestBase.wait(self, "[data-test-id='detailAddToCart']")
        HelperTestBase.clickAndWait(self, "[data-test-id='detailAddToCart']")

    def clickBackButton(self):
        HelperTestBase.click(self, "[data-test-id='searchResultsLink']")
        time.sleep(1)

    def clickSellerName(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='showSeller']")

    def addProductToCartWatchlistFavorites(self):
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        time.sleep(1)
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(1)
        HelperTestBase.reliableClick(self, "[data-test-id='addToFL']")
        time.sleep(1)
        HelperTestBase.reliableClick(self, "[data-test-id='addToWL']")
        time.sleep(1)
        HelperTestBase.wait(self, "[data-test-id='detailAddToCart']")
        time.sleep(1)
        HelperTestBase.reliableClick(self, "[data-test-id='detailAddToCart']")
        time.sleep(1)
        HelperTestBase.clickYesButton(self)
        time.sleep(1)
