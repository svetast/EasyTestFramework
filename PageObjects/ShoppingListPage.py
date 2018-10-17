import time

from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class ShoppingListPage(LoginPage):
    def ShoppingListPage(self):
        driver = self.driver
        driver.get(self.base_url)

##### Select the product in Shopping List:
    def selectProduct(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        time.sleep(3)

    def sortAndSelectProduct(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='detailAddToCart']")
        time.sleep(3)

    def clickOnItem(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        time.sleep(3)



    def clickOnHeader(self):
        self.driver.find_element_by_xpath("//header/shopping-header/div/nav/div[2]/h4").send_keys(Keys.ENTER)



   # This method set text into input field :
    def setTextUseSpace(self, locator=None, stringtext=None):
        self.driver.find_element_by_css_selector(locator).clear()
        self.driver.find_element_by_css_selector(locator).send_keys(stringtext)
        self.driver.find_element_by_xpath(
            "//body/app-root/div/div/shopping-list/div/shopping-header/header/div/nav/div/h4").click()
