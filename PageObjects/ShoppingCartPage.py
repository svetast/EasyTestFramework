import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase
from PageObjects.NavigationMenuPage import NavigationMenuPage


class ShoppingCartPage(NavigationMenuPage):
    def CartPage(self):
        driver = self.driver
        driver.get(self.base_url)

    # checking - is the 'PAY' button  present on Cart page:

    def checkPayPresent(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='payBtn']").is_displayed()
        return state

    def checkCartBadge(self):
        state = self.driver.find_element_by_xpath(
            "/html/body/app-root/div/div/cart/div/cart-header/header/nav/div[2]/div/span").is_displayed()
        return state

    def click(self, locator=None):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        button.click()

    def clickRefreshButton(self):
        HelperTestBase.click(self, "[data-test-id='cartRefreshItem_0']")

    def clickPayButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='payBtn']")

    def deleteItemFromCart(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='cartRemoveItem_0']")
        time.sleep(5)


#   get text for Empty Cart':
    def getText(self):
        text = self.driver.find_element_by_css_selector("body > app-root > div > div > cart > div > div > h3").text
        return text


    def addQuantity(self, number=None):
       elem = self.driver.find_element_by_name("quantity")
       elem.clear()
       elem.send_keys(number)

    def addItemToCart(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.clickAndWait(self, "[data-test-id='detailAddToCart']")
        time.sleep(5)
