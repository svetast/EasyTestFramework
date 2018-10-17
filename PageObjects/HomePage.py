from telnetlib import EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage


class HomePage(LoginPage):# == Shopping List##
    def HomePage(self):
        driver = self.driver
        driver.get(self.base_url)


### LogOut action:   ####

    def clickBackButton(self):
         self.driver.find_element_by_css_selector("[data-test-id='logOutLink']").click()

######## click on Search button:   ###########

    def clickSearchButton(self):
       self.driver.find_element_by_css_selector("[data-test-id='searchLink']").click()

    # def clickButton(self, locator=None):
    #     self.driver.find_element_by_css_selector(locator).click()


 # Click on 'Shopping List' in header ( without data-test-id):
    def clickOnHeader(self):
        self.driver.find_element_by_xpath("//h4").click()



#######   Helpers  ########

    def getBackgroundColor(self, locator=None):
        color = self.driver.find_element_by_css_selector(locator).get_attribute('background')
        return color





######### Choosing item      will re-done!!!!!!!!!        ###########

######  временные методы - будут удалены после добавления data-test-id   #######

    def clickSearchItem(self):
        self.driver.find_element_by_xpath(
            "//html/body/app-root/div/div/shopping-list/div/sub-list[1]/ul/li[7]/div/span[3]/i").click()

    def getTextPepper(self):
        text = self.driver.find_element_by_xpath(
            "//body/app-root/div/div/search-results/search-list/div/ul/li/div[2]/h4").text()
        return text

    def clickSearchPepper(self):
        self.driver.find_element_by_xpath(
            "//body/app-root/div/div/search-results/search-list/div/ul/li/div[3]/i").click()

    def checkBuyNowButton(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='detailBuyNow']").is_displayed()
        return state

