from HelperTestBase import HelperTestBase
from PageObjects.InventoryListPage import InventoryListPage
from PageObjects.LoginPage import LoginPage
from PageObjects.MessagesPage import MessagesPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.ShopperDetailsPage import ShopperDetailsPage


class TestInventoryList(NavigationMenuPage, MessagesPage, ShopperDetailsPage, ProductEditorPage):
    ## 1. Test scope -  Click on 'delete' button =>	The 'Are your sure you want to remove this item?' message is displayed.
    # click on No button  = > Inventory list is displayed
    #### 2. Click the delete button =>	The 'Are your sure you want to remove this item?' message is displayed.
    # click on Yes button = > the item is deleted from Inventory list
    # @pytest.mark.skip
    def test_deleteAdd_Item_InventoryList(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/inventory-list'
        text = 'Success:'
        text1 = 'A new item has been successfully created.'
        text2 = 'Remove item?'
        text3 = 'Are you sure you want to remove this item?'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        ## Click on 'delete' button
        InventoryListPage.deleteItem(self)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        # click on No button  = > Inventory list is displayed
        InventoryListPage.deleteItem(self)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ########## Test scope Seller create item => the item added to Inventory List:
        ProductEditorPage.returtTestData(self, title='Test Apple', price='2',
                                         description='test', sortUnits='Each',
                                         currentQuantityInp='100', sortQTY='Each',
                                         country='Canada', productCodeInp='test product')

        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        # @pytest.mark.skip
        # def test_prepearingTestDataInventoryList(self):
        #     url = self.base_url + '/shopping-list'
        #     text = 'Success:'
        #     text1 = 'A new item has been successfully created.'
        #     driver = self.driver
        #     driver.get(self.base_url)
        #     #LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        #     # LoginPage.loginAction(self, 'SellerTestlhc', 'Ss123456')
        #     LoginPage.loginAction(self, 'Bob', 'Ss123456')
        #
        #
        #
        #     self.assertEqual(url, HelperTestBase.getURL(self))
        #     NavigationMenuPage.clickSellerButton(self)
        #     x = StringGenerator('[\c]{5}').render()
        #
        #     i = 1
        #     while (i <= 20):
        #         y = StringGenerator('[\d]{2}').render()
        #         ProductEditorPage.addProductWithoutYear(self,
        #                                                 title='Test Item ' + x,
        #                                                 description='test',
        #                                                 price=y,
        #                                                 sortUnits='Each',
        #                                                 currentQuantityInp='10', sortQTY='Each',
        #                                                 country='Canada', productCodeInp='test',
        #                                                 salePrice='1', sortSalePrice='Each')
        #
        #         self.assertEqual(text, HelperTestBase.getModalHeader(self))
        #         self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        #         HelperTestBase.clickYesButton(self)
        #     i += 1
