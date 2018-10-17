import time

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class WatchListPage(NavigationMenuPage):
    def WatchListPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def removeFromWatchList(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='watchListPRemoveItem_0']")
        time.sleep(3)

    def addToWatchList(self):
        HelperTestBase.reliableClick(self, "[data-test-id ='shoppingListProduct_0']")
        HelperTestBase.wait(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id ='abstractListProduct_0']")
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id ='addToWL']")
        time.sleep(3)

    def checkItemPresent(self):
        state = HelperTestBase.checkElementPresent(self, "[data-test-id='watchListPItem_0']")
        return state
