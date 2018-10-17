import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from  HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class NavigationMenuPage(LoginPage):
    def NavigationMenuPage(self):
        driver = self.driver
        driver.get(self.base_url)

    ################## NAVIGATION MENU   #########################


    # checking - is a web element present on NavMenu? ( Cart, Profile, Watchlist etc.):

    def checkElementEnabled(self, locator=None):
        state = self.driver.find_element_by_css_selector(locator).is_enabled()
        return state

    ###############

    # click on the web element on NavMenu (on Cart,on Profile, on Watchlist etc.):

    def click(self, locator=None):
        wait = WebDriverWait(self.driver, 50)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        button.click()



    def clickWatchlist(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='watchlist']")
        time.sleep(3)


    def clickFavoriteList(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='favorites']")
        time.sleep(3)

    def clickProfile(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='profile']")
        time.sleep(3)

    def clickMessages(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='dialogs']")
        time.sleep(3)

    def clickAnalytics(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='analytics']")
        time.sleep(2)





    def clickNewItem(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='new-item']")
        time.sleep(2)

    def clickReviews(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='reviews']")
        time.sleep(2)



    def clickCart(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='cart']")
        time.sleep(3)

    def clickNavMenuButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)


    def clickSellerButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")
        time.sleep(5)




    def clickBuyerButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='buyerBtn']")
        time.sleep(3)

    def clickBackButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)

    def goToWatchListPage(self):
        self.clickNavMenuButton()
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='watchlist']")
        time.sleep(2)

    def removeProductFromCartWatchlistFavorites(self):
        HelperTestBase.reliableClick(self, "[data-test-id='cart']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='cartRemoveItem_0']")
        time.sleep(7)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(5)
        self.clickWatchlist()
        #HelperTestBase.reliableClick(self, "[data-test-id='watchlist']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='watchListPRemoveItem_0']")
        time.sleep(7)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.clickFavoriteList()
        #HelperTestBase.reliableClick(self, "[data-test-id='favorites']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='favListPRemoveItem_0']")
        time.sleep(7)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)

    def deleteItemFromCart(self):
        HelperTestBase.reliableClick(self, "[data-test-id='cartRemoveItem_0']")
        time.sleep(5)

    def removeFromWatchList(self):
        HelperTestBase.reliableClick(self, "[data-test-id='watchListPRemoveItem_0']")
        time.sleep(5)

    def removeFromFavList(self):
        HelperTestBase.reliableClick(self, "[data-test-id='favListPRemoveItem_00']")
        time.sleep(5)

    #####

    def clickWatchList_XXX(self):
        self.driver.find_element_by_xpath("//app-footer/footer/div/nav/span[2]").click()
        time.sleep(2)
