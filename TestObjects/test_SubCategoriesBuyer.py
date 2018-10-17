import time

import pytest

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.SubcategoriesPage import SubcategoriesPage


class TestSubCategories(SubcategoriesPage):
    # Valid user credentials - SA1 / Bizibaza111


    # test scope -click on Flowers => Daisy Mums, Gerbera, Gladiolus, Rose  are displayed:
    @pytest.mark.skip
    def test_subcategoryOtherFlowers(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='Other']")
        HelperTestBase.clickAndWait(self, "[data-test-id=subcategory_3]")
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))







        # test scope - click on Chocolate => 'Dark' is displayed:

    # @pytest.mark.skip
    def test_subcategoryOtherChocolate(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(4)

        HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
        HelperTestBase.clickOnElement(self, "[data-test-id='Other']")
        HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
        HelperTestBase.clickAndWait(self, "[data-test-id=subcategory_1]")
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))


    # test scope - click on Bread => 'Sourdough'  is displayed:
    # @pytest.mark.skip
    def test_subcategoryBakeryBread(self):
        url = self.base_url + '/shopping-list'
        text1 = 'White'
        text0 = "Sourdough"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
        HelperTestBase.clickOnElement(self, "[data-test-id='Bakery']")
        HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
        HelperTestBase.clickAndWait(self, "[data-test-id=subcategory_0]")
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))

        # test scope - click on Arugula => 'Arugula'  is displayed:
        # @pytest.mark.skip
        def test_subcategoryVegetablesCarrot(self):
            url = self.base_url + '/shopping-list'
            text0 = 'Carrot'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.waitSettingsButton(self)

            HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='Vegetables']")
            HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))



            # test scope - click on Apple => 'Apple'  is displayed:

        # @pytest.mark.skip
        def test_subcategoryFruitsApple(self):
            url = self.base_url + '/shopping-list'
            text0 = 'Apple'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.waitSettingsButton(self)

            HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='Fruits']")
            HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))




            # test scope - click on Apple => 'Apple'  is displayed:
            # @pytest.mark.skip

        def test_subcategoryVegetablesCucumber(self):
            url = self.base_url + '/shopping-list'
            text0 = 'Cucumber'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.waitSettingsButton(self)

            HelperTestBase.clickAndWait(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='Vegetables']")
            HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_1']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))

        # test scope - click on 'Back' button on subcategory => Shopping List page is opened, Log out link is displayed:
        # @pytest.mark.skip
        def test_BackToShoppingList(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')

            HelperTestBase.waitSettingsButton(self)

            HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.reliableClick(self, "[data-test-id='Vegetables']")
            HelperTestBase.wait(self, "[data-test-id='shoppingLink']")
            time.sleep(3)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
            HelperTestBase.waitSettingsButton(self)
            self.assertEqual(url, HelperTestBase.getURL(self))



            # Test scope -  click on the Chicken subcategory  subcategory of the 'Poultry' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickPoultryChicken(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='Poultry']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))

        # Test scope -  click on Butter subcategory of the 'Dairy' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickDairyButter(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickOnElement(self, "[data-test-id='Dairy']")
            HelperTestBase.clickOnElement(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))


            # Test scope -  click on the Crab subcategory of the 'SeaFood' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickSeaFoodCrab(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickOnElement(self, "[data-test-id='SeaFood']")
            HelperTestBase.clickOnElement(self, "[data-test-id='subcategory_1']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))

        # Test scope -  click on the Bacon subcategory of the 'Meat' category => The appropriate products are displayed. :

        # @pytest.mark.skip

        def test_clickMeatBacon(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
            HelperTestBase.clickAndWait(self, "[data-test-id='Meat']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
