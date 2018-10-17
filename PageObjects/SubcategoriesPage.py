from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.CategoriesMenuPage import CategoriesMenuPage


class SubcategoriesPage(CategoriesMenuPage):
    def SubcategoriesPage(self):
        driver = self.driver
        driver.get(self.base_url)

        #####  Select a product in 'Subcategory product items:':

    # The universal method - click oj Subcategory:
    def clickSubcategory(self, locator=None):
        self.driver.find_element_by_css_selector(locator).click()

    # The universal method - check is product present :

    def checkProductIsPresent(self, locator=None):
        state = self.driver.find_element_by_css_selector(locator).is_displayed()
        return state




######################################################### will remove
    # Click on 'NannyO's Green Tomato Pickles 16oz':

    def clickNannyGreenTomatoPickles(self):
        self.driver.find_element_by_xpath("//app/div/div/home/div/div/home-product-list/div/ul/li[1]/h2").click()

  # Click on subcategory on Ohter category:
    def clickFlowers(self):
        self.driver.find_element_by_xpath("//app-root/div/div/goods-nav/ul/li[1]/p/i").click()

    def clickChocolate(self):
        self.driver.find_element_by_xpath("//app-root/div/div/goods-nav/ul/li[6]/p/i").click()


 # Click on subcategory on Bakery category:

    def clickBread(self):
        self.driver.find_element_by_xpath("html/body/app-root/div/div/goods-nav/ul/li[1]/p/i").click()