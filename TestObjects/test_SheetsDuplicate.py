import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SheetsPage import SheetsPage


class TestSheetsDuplicate(SheetsPage, ProductEditorPage):
    # @pytest.mark.skip
    def test_checkDuplicateItemSuccessAndRemove(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        text = 'Remove item?'
        text1 = 'Are you sure you want to remove this item?'
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        SheetsPage.clickDuplicate(self)
        SheetsPage.closeSheets(self)
        SheetsPage.openSheets(self)
        SheetsPage.deleteItem(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.clickYesButton(self)

    # @pytest.mark.skip
    def test_checkDuplicate21Item(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        text = 'Remove item?'
        text1 = 'Are you sure you want to remove this item?'
        LoginPage.loginAction(self, 'SellerTestpsq', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        SheetsPage.clickDuplicate(self)
        time.sleep(3)
        self.assertEqual(len(self.driver.find_elements_by_css_selector("[data-test-id='remove']")), 42)
        SheetsPage.closeSheets(self)
        SheetsPage.openSheets(self)
        self.assertEqual(len(self.driver.find_elements_by_css_selector("[data-test-id='remove']")), 40)
        SheetsPage.deleteItem(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.clickYesButton(self)
