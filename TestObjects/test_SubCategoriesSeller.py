from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestSubCategorieSeller(NavigationMenuPage):
    # Test scope -  click on the Apple subcategory of the 'Fruits' category => The appropriate products  are displayed. :

    #@pytest.mark.skip
    def test_clickFruitsApple(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        NavigationMenuPage.clickNewItem(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='Fruits']")
        HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))



    # Test scope -  click on the Arugula subcategory of the 'Vegetables' category => The appropriate products  are displayed. :

    #@pytest.mark.skip
    def test_clickVegetablesArugula(self):
        url = self.base_url + '/shopping-list'
        text0 = 'Arugula'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        NavigationMenuPage.clickNewItem(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='Vegetables']")
        HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_2']")
        self.assertEqual(text0, HelperTestBase.getText(self, "[data-test-id='entry_0']"))

        # Test scope -  click on the Bread subcategory of the 'Bakery' category => The appropriate products  are displayed:

        # @pytest.mark.skip
        def test_clickBakeryBread(self):
            url = self.base_url + '/shopping-list'

            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickAndWait(self, "[data-test-id='Bakery']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))

        # Test scope -  click on the Flowers subcategory of the 'Other' category => The appropriate products  are displayed. :

        # @pytest.mark.skip
        def test_clickOtherFlowersIcon(self):
            url = self.base_url + '/shopping-list'
            text0 = 'Acacia'
            text1 = 'Achillea'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickAndWait(self, "[data-test-id='Other']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))

        # Test scope -  click on the Bacon subcategory of the 'Meat' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickMeatBacon(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickAndWait(self, "[data-test-id='Meat']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))

        # Test scope -  click on the Crab subcategory of the 'SeaFood' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickSeaFoodCrab(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickOnElement(self, "[data-test-id='SeaFood']")
            HelperTestBase.clickOnElement(self, "[data-test-id='subcategory_1']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))




            # Test scope -  click on the Chicken subcategory  subcategory of the 'Poultry' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickPoultryChicken(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickAndWait(self, "[data-test-id='Poultry']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))





            # Test scope -  click on Butter subcategory of the 'Dairy' category => The appropriate products are displayed. :

        # @pytest.mark.skip
        def test_clickDairyButter(self):
            url = self.base_url + '/shopping-list'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            NavigationMenuPage.clickNewItem(self)
            HelperTestBase.clickAndWait(self, "[data-test-id='Dairy']")
            HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_0']"))
            self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='entry_1']"))
