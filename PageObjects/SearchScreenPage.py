import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class SearchScreenPage(NavigationMenuPage):
    def SearchWindowPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def sortItems(self, sortOption):
        self.driver.find_element_by_name("sortBy").click()
        select1 = Select(self.driver.find_element_by_name("sortBy"))
        select1.select_by_value(sortOption)

    def submitSearchItem(self, item):
        self.clickFilterSearchIcon()
        self.clickItemSearchButton()
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(item)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(2)

    def submitSearchItem1(self, item):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(item)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)

    def submitSearchSeller(self, seller):
        self.clickFilterSearchIcon()
        self.clickSellerSearchButton()
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(seller)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(2)

    def submitSearchSeller1(self, seller):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(seller)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(3)

    def submitSearchMarket(self, market):
        self.clickFilterSearchIcon()
        self.clickMarketSearchButton()
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(market)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(3)

    def submitSearchMarket1(self, market):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(market)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(3)



    def submitSearchMarketEvent(self, market):
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(market)
        self.driver.find_element_by_css_selector("[data-test-id='searchInp']").send_keys(Keys.ENTER)
        time.sleep(3)



    # the method return the Error during search function:
    def getModalWindow(self):
        title = self.driver.find_element_by_xpath("//html/body/app-root/div/modal/div/div/h3").text
        return title

    def clickItemSearchButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        time.sleep(2)

    def clickSellerSearchButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='noButton']")
        time.sleep(2)



    def clickMarketSearchButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='lastButton']")
        time.sleep(2)

    def clickFilterSearchIcon(self):
        HelperTestBase.reliableClick(self, "[data-test-id='filterBtn']" )
        time.sleep(3)

    def clickMapsTopIcon(self):
        HelperTestBase.reliableClick(self, "[data-test-id='mapBtnTop']")
        time.sleep(2)


    def clickMapsIcon(self):
        HelperTestBase.reliableClick(self, "[data-test-id='mapBtn']")
        time.sleep(2)


    def checkMapsPresent(self):
        maps = self.driver.find_element_by_css_selector(
            "body > app-root > div > div > market > div > div > div > div.shopper-details__img > agm-map > div.agm-map-container-inner.sebm-google-map-container-inner > div > div > div:nth-child(1) > div:nth-child(3) > div").is_displayed()
        return maps

    def checkMarketTitlePresent(self):
        marketTitle = self.driver.find_element_by_css_selector("[data-test-id='marketTitle']").is_displayed()
        return marketTitle






        # def clickOk(self):
    #    self.driver.find_element_by_xpath("html/body/app-root/div/modal/div/div").click()




# the method return the Error during search function:
    def getSearchErrorMessage(self, locator =None):
        message = self.driver.find_element_by_xpath(locator).text
        return message

# the method return the search results:
    def getSearchResult(self):
        searchResult = self.driver.find_element_by_xpath("//search-results/search-list/div/h1").text
        return searchResult