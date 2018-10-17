import time

from HelperTestBase import HelperTestBase
from PageObjects.CategoriesMenuPage import CategoriesMenuPage
from PageObjects.LoginPage import LoginPage


class TestCategoriesMenu(CategoriesMenuPage):
    # @pytest.mark.skip
    def test_checkElements(self):
        # Test scope - Buyer clicks on Categories Menu  => the 'categories menu' ( Fruits, Vegetables, Meat, Other, Bakery) is displayed:
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'asdfgh', 'Ss123456')
        CategoriesMenuPage.clickCategoriesMenuButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Fruits']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Vegetables']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Bakery']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Other']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Meat']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='SeaFood']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Dairy']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Poultry']"), True)

        # Click on the 'footer category' button => The 'categories menu' is closed:
        CategoriesMenuPage.clickCategoriesMenuButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Fruits']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Vegetables']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Bakery']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Other']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Meat']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='SeaFood']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Dairy']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Poultry']"), False)

    # @pytest.mark.skip
    def test_clickFruitsIcon(self):
        # Test scope -  Buyer clicks on the image of the 'Fruits' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'asdfgh', 'Ss123456')

        CategoriesMenuPage.clickCategoriesMenuButton(self)
        CategoriesMenuPage.clickFruitsButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickVegetablesIcon(self):
            # Test scope - Buyer  clicks on the image of the 'Vegetables' category => The appropriate subcategories are displayed. :
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'asdfgh', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickVegetablesButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickBakeryImg(self):
            # Test scope - Buyer clicks on the image of the 'Bakery' category => The appropriate subcategories are displayed:
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'asdfgh', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickBakeryButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickOtherIcon(self):
            # Test scope - Buyer clicks on the image of the 'Other' category => The appropriate subcategories are displayed. :
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'asdfgh', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickOtherButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickMeatIcon(self):
            # Test scope - Buyer clicks on the image of the 'Meat' category => The appropriate subcategories are displayed. :
            url = self.base_url + '/shopping-list'
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'asdfgh', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickMeatButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickSeaFood(self):
            # Test scope -  Buyer clicks on the image of the 'SeaFood' category => The appropriate subcategories are displayed. :
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'svetast', 'Ss1234567')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickSeaFoodButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)


            # @pytest.mark.skip

    def test_clickPoultry(self):
            # Test scope -  Buyer clicks on the image of the 'Poultry' category => The appropriate subcategories are displayed. :
            url = self.base_url + '/shopping-list'
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.get(self.base_url)
            # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
            LoginPage.loginAction(self, 'Bob', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickPoultryButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)


            # @pytest.mark.skip

    def test_clickDairy(self):
            # Test scope -  Buyer clicks on the image of the 'Dairy' category => The appropriate subcategories are displayed:
            url = self.base_url + '/shopping-list'
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.get(self.base_url)
            # LoginPage.loginAction(self, '', 'Ss1234567')
            LoginPage.loginAction(self, 'Bob', 'Ss123456')

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickDairyButton(self)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)

    def test_checkCategotyVisible(self):
            # Test scope -  Buyer clicks on the image of the some category => The appropriate subcategories are displayed:
            url = self.base_url + '/shopping-list'
            url1 = self.base_url + '/inventory-list'
            text0 = 'Carrot'
            text1 = 'Cucumber'
            text2 = 'Bread'
            text3 = 'Brownies'
            text4 = "Chocolate"
            text5 = 'Flowers'
            text6 = 'Bacon'
            text7 = 'Crab'
            text8 = 'Apple'
            text9 = 'Chicken'
            text11 = 'Ice Cream'

            driver = self.driver
            driver.get(self.base_url)
            # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
            LoginPage.loginAction(self, 'svetast', 'Ss1234567')
            time.sleep(4)

            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickVegetablesButton(self)
            self.assertIn(text0, self.driver.page_source)
            self.assertIn(text1, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickBakeryButton(self)
            self.assertIn(text2, self.driver.page_source)
            self.assertIn(text3, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickOtherButton(self)
            self.assertIn(text4, self.driver.page_source)
            self.assertIn(text5, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickMeatButton(self)
            self.assertIn(text6, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickSeaFoodButton(self)
            self.assertIn(text7, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickFruitsButton(self)
            self.assertIn(text8, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickPoultryButton(self)
            self.assertIn(text9, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")

            ##
            CategoriesMenuPage.clickCategoriesMenuButton(self)
            CategoriesMenuPage.clickDairyButton(self)
            self.assertIn(text11, self.driver.page_source)
            HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")



            ######
