import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SheetsPage import SheetsPage


class TestSheetsEdit(SheetsPage, ProductEditorPage):

    # @pytest.mark.skip
    def test_checkChangesSavedSuccess(self):
        # Test scope - Make some changes in Sheets screen, click on Save button, reopen the Sheets screen => Changes are saved

        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        text2 = 'Warning:'
        text3 = 'Success:'
        text1 = 'You have unsaved changes. Discard them?'

        text = "Qwerty"
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(3)
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        ### Checking that changes saved on Following Field:
        SheetsPage.editProductItemField(self, 'Qwerty')
        # SheetsPage.clickSaveButton(self)
        SheetsPage.editSellerNameField(self, 'Test Seller Name')
        SheetsPage.editDescription(self, 'tralalalala')
        SheetsPage.editPrice(self, '155')
        SheetsPage.selectQuantityUnits(self, 'Box')
        SheetsPage.editProductCode(self, 'edit text')
        SheetsPage.selectMarketPickUp(self)
        SheetsPage.selectDeliveryMethod(self)
        SheetsPage.selectSaleIsActive(self)
        # SheetsPage.selectOrganic(self)
        # SheetsPage.selectNonGMO(self)
        SheetsPage.closeSheets(self)

        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        self.assertIsNot(text, self.driver.page_source)
        SheetsPage.editProductItemField(self, 'Qwerty')
        SheetsPage.closeSheets(self)
        self.assertEqual(text2, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        self.assertIs(text, self.driver.page_source)

        # ### Return test data:
        SheetsPage.openSheets(self)
        SheetsPage.editProductItemField(self, 'Test Item Test')
        SheetsPage.editSellerNameField(self, 'Aist')
        SheetsPage.editDescription(self, '123 see')
        SheetsPage.editPrice(self, '10')
        SheetsPage.selectQuantityUnits(self)
        SheetsPage.editProductCode(self, ' new string')
        SheetsPage.selectMarketPickUp(self)
        SheetsPage.selectDeliveryMethod(self)
        SheetsPage.selectSaleIsActive(self)
        # SheetsPage.selectOrganic(self)
        #SheetsPage.selectNonGMO(self)
        SheetsPage.clickSaveButton(self)


    # @pytest.mark.skip
    def test_uploadImageOrganicSertificate(self):
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        text = "Error"
        LoginPage.loginAction(self, 'SellerTestpsq', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)

        SheetsPage.openSheets(self)
        SheetsPage.clickImageOrganicSerttificate(self)
        self.assertIsNot(text, self.driver.page_source)

    # @pytest.mark.skip
    def test_uploadImageNonGMOSertificate(self):
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        text = "Error"
        LoginPage.loginAction(self, 'SellerTestpsq', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)

        SheetsPage.openSheets(self)
        SheetsPage.clickImageNonGMOSerttificate(self)
        self.assertIsNot(text, self.driver.page_source)


        # @pytest.mark.skip

    #@pytest.mark.skip
    def test_checkChangesNotSavedAfterCancelClick(self):
        # Test scope - Make some changes in Sheets screen, click on Cancel button, reopen the Sheets screen => Changes are saved
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        text = "Rubicon"
        LoginPage.loginAction(self, 'SellerTestpsq', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        SheetsPage.editProductItemField(self, 'Rubicon')
        SheetsPage.closeSheets(self)
        HelperTestBase.clickYesButton(self)
        SheetsPage.openSheets(self)
        self.assertNotIn(text, self.driver.page_source)

    # @pytest.mark.skip
    def test_uploadImageProduct(self):
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        text = "Error"
        LoginPage.loginAction(self, 'SellerTestlhc', 'Ss123456')
        time.sleep(3)
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SheetsPage.openSheets(self)
        SheetsPage.clickImageProduct(self)
        time.sleep(3)
        self.assertIsNot(text, self.driver.page_source)
