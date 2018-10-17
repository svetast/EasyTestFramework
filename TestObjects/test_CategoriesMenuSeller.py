import time

from HelperTestBase import HelperTestBase
from PageObjects.CategoriesMenuPage import CategoriesMenuPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestCategoriesMenuSeller(NavigationMenuPage, CategoriesMenuPage):
    #### Valid user (Seller & Buyer) credentials - Ss / Ss1234567


    # Seller clicks on the 'footer category' button => The 'categories menu' is closed
    # @pytest.mark.skip
    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        # Test scope - click on +NewItem  => the 'categories menu' ( Fruits, Vegetables, Meat, Other, Bakery ...... ) is displayed:

        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Fruits']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Vegetables']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Bakery']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Other']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Meat']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='SeaFood']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Dairy']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Poultry']"), True)

        # Test scope - click on NavMenu button  => the 'categories menu' ( Fruits, Vegetables, Meat, Other, Bakery ...... ) is closed:
        NavigationMenuPage.clickNavMenuButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Fruits']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Vegetables']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Bakery']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Other']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Meat']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='SeaFood']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Dairy']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Poultry']"), False)

        # @pytest.mark.skip

    def test_checkCategoriesPresent(self):

        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'

        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        # Test scope -  Seller clicks on the image of the 'Fruits' category => The appropriate subcategories are displayed. :
        CategoriesMenuPage.clickFruitsButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")
        # Test scope -  Seller clicks on the image of the 'Vegetables' category => The appropriate subcategories are displayed. :
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickVegetablesButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")
        # Test scope -  Seller clicks on the image of the 'Bakery' category => The appropriate subcategories are displayed:
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickBakeryButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")

        # Test scope -  Seller clicks on the image of the 'Other' category => The appropriate subcategories are displayed. :
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickOtherButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")

        # Test scope -  Seller clicks on the image of the 'Meat' category => The appropriate subcategories are displayed. :
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickMeatButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")

        # Test scope -  Seller clicks on the image of the 'SeaFood' category => The appropriate subcategories are displayed. :
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickSeaFoodButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")

        # Test scope -  Seller clicks on the image of the 'Dairy' category => The appropriate subcategories are displayed. :
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickDairyButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")

        # Test scope -  Seller clicks on the image of the 'Poultry' category => The appropriate subcategories are displayed. :

        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickPoultryButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryLink']")











        # @pytest.mark.skip

    def test_clickVegetablesIcon(self):
        # Test scope -  Seller clicks on the image of the 'Vegetables' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickVegetablesButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickBakeryImg(self):
        # Test scope -  Seller clicks on the image of the 'Bakery' category => The appropriate subcategories are displayed:
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(2)
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickBakeryButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickOtherIcon(self):
        # Test scope -  Seller clicks on the image of the 'Other' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(2)
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickOtherButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickMeatIcon(self):
        # Test scope -  Seller clicks on the image of the 'Meat' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'

        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickMeatButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)

        # @pytest.mark.skip

    def test_clickSeaFood(self):
        # Test scope -  Seller clicks on the image of the 'SeaFood' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickSeaFoodButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)


        # @pytest.mark.skip

    def test_clickPoultry(self):
        # Test scope -  Seller clicks on the image of the 'Poultry' category => The appropriate subcategories are displayed. :
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickPoultryButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_1']"), True)


        # @pytest.mark.skip

    def test_clickDairy(self):
        # Test scope -  Seller clicks on the image of the 'Dairy' category => The appropriate subcategories are displayed:
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickDairyButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='subcategory_0']"), True)
