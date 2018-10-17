import time

from HelperTestBase import HelperTestBase
from PageObjects.CategoriesMenuPage import CategoriesMenuPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SheetsPage import SheetsPage


class TestSheetsCreate(SheetsPage, ProductEditorPage):
    # @pytest.mark.skip
    def test_checkCreateItemSuccessAndRemove(self):

        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        text = 'Error:'
        text1 = 'Item#1 - You should choose DELIVERY method.'
        text2 = 'Item#1 - Field TITLE is required. Please, fill it in.'
        text3 = 'Item#1 - Field SELLING PRICE is required. Please, fill it in.'
        text4 = 'Item#1 - Field UNITS is required. Please, fill it in.'
        text5 = 'Item#1 - Field AVAILABLE QUANTITY is required. Please, fill it in.'
        text6 = 'Item#1 - Field QUANTITY UNITS is required. Please, fill it in.'


        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        SheetsPage.clickCreateButton(self)
        CategoriesMenuPage.clickVegetablesButton(self)
        ProductEditorPage.selectCategory(self)
        ##Don't fill out of requarement field, click on Save button=> Error is displayed:
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        ##Fill out only 'Product Item' field, click on Save button=> Error is displayed:
        SheetsPage.editProductItemField(self, 'Test Item Test')
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text3, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ### Fill out not requarement fields Seller Name and Description:
        SheetsPage.editSellerNameField(self, 'Aist')
        SheetsPage.editDescription(self, '123 see')
        ##Don't fill out other requarement fields, click on Save button => Error is displayed:

        SheetsPage.editPrice(self, '10')
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text4, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        ##Don't fill out other requarement fields, click on Save button => Error is displayed:

        SheetsPage.selectUnits(self, 'Carton')
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text5, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        ##Don't fill out other requarement fields, click on Save button => Error is displayed:

        SheetsPage.editAvailableQuantity(self, '65')
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text6, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        SheetsPage.selectQuantityUnits(self, 'Each')
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ### Select the not requarement fields Product Code, Sale is Active, Organic, Non GMO :
        SheetsPage.editProductCode(self, 'New Test String')
        SheetsPage.selectSaleIsActive(self)
        SheetsPage.selectOrganic(self)
        SheetsPage.selectNonGMO(self)
        SheetsPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        SheetsPage.selectDeliveryMethod(self)
        SheetsPage.selectMarketPickUp(self)
        SheetsPage.clickSaveButton(self)
        HelperTestBase.clickYesButton(self)
        SheetsPage.closeSheets(self)

        ######Return test data:
        SheetsPage.openSheets(self)
        SheetsPage.deleteItem(self)
        HelperTestBase.clickYesButton(self)

        # @pytest.mark.skip

    def test_checkOpenSheetsAndClose(self):
            url1 = self.base_url + '/inventory-list'
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            text = 'Warning:'
            text1 = 'You have unsaved changes. Discard them?'
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            SheetsPage.openSheets(self)
            SheetsPage.clickCreateButton(self)
            CategoriesMenuPage.clickVegetablesButton(self)
            ProductEditorPage.selectCategory(self)
            SheetsPage.closeSheets(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickCancelButton(self)

            SheetsPage.closeSheets(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            time.sleep(3)
            self.assertEqual(url1, HelperTestBase.getURL(self))
