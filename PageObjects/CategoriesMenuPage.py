import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class CategoriesMenuPage(LoginPage):
    def CategoriesMenuPage(self):
        driver = self.driver
        driver.get(self.base_url)

    #####################################  Click on  'Categories'    ##############################




    def clickCategoriesMenuButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
        time.sleep(3)


    def clickFruitsButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Fruits']")
        time.sleep(2)

    def clickVegetablesButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Vegetables']")
        time.sleep(2)

    def clickOtherButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Other']")
        time.sleep(2)

    def clickBakeryButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Bakery']")
        time.sleep(2)

    def clickMeatButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Meat']")
        time.sleep(2)

    def clickDairyButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Dairy']")
        time.sleep(2)

    def clickPoultryButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='Poultry']")
        time.sleep(2)

    def clickSeaFoodButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='SeaFood']")
        time.sleep(2)





    # Click on category - Universal method:

    def click(self, locator):
        wait = WebDriverWait(self.driver, 15)
        clickCategory = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        clickCategory.click()



