import time

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class FavoritesPage(NavigationMenuPage):
    def FavoritesPage(self):
        driver = self.driver
        driver.get(self.base_url)


        ########     HELPERS    ############

#   get text 'Your favorite list:'
    def getText(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/div/favorite-list/div/h2").text
        return text

    def getMessage(self):
        text= self.driver.find_element_by_class_name("list__ul__empty-list").text
        return text

#   get text 'List of products:'
    def getTextList(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/div/favorite-list/div/ul[1]/h2").text
        return text

#   get text 'Users list: '
    def getTextUserList(self):
        text = self.driver.find_element_by_xpath("//body/app-root/div/div/favorite-list/div/ul[2]/h2").text
        return text

    def removeFromFavList(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='favListPRemoveItem_0']")
        time.sleep(5)

    def addToFavList(self):
        HelperTestBase.reliableClick(self, "[data-test-id ='shoppingListProduct_0']")
        # HelperTestBase.wait(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id ='abstractListProduct_0']")
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id ='addToFL']")
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='searchResultsLink']")


        # self.driver.find_element_by_css_selector("[data-test-id ='shoppingListProduct_0']").click()
        # self.driver.find_element_by_css_selector("[data-test-id ='abstractListProduct_0']").click()
        # self.driver.find_element_by_css_selector("[data-test-id ='addToFL']").click()
        # time.sleep(5)
