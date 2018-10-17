import time

from strgen import StringGenerator

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SheetsPage import SheetsPage


class TestSheetsPangination(SheetsPage, ProductEditorPage):
    # @pytest.mark.skip
    def test_checkElements(self):
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        url4 = self.base_url + '/inventory-sheet'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestavm', 'Ss123456')
        time.sleep(3)

        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SheetsPage.openSheets(self)
        time.sleep(4)
        self.assertEqual(url4, HelperTestBase.getURL(self))
        ###Check Remove button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='remove']"), True)
        # Check the pangination elements:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToFirstPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToPreviousPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='pageCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToNextPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToLastPage']"), True)
        # Check the Save & Exit button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='saveBtn']"), True)
        # Check the Cancel button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cancelLink']"), True)

        # @pytest.mark.skip
    def test_checkPangination(self):
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        url4 = self.base_url + '/inventory-sheet'
        text = '1 / 5'
        text1 = '2 / 5'
        text2 = '3 / 5'
        text3 = '4 / 5'
        text4 = '5 / 5'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SheetsPage.openSheets(self)
        time.sleep(4)
        self.assertEqual(url4, HelperTestBase.getURL(self))


        ###Check page counter:
        self.assertEqual(text, SheetsPage.getPageNumber(self))
        ###Check Remove button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='remove']"), True)
        # Check the pangination elements:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToFirstPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToPreviousPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='pageCounter']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToNextPage']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='goToLastPage']"), True)
        # Check the Save & Exit button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='saveBtn']"), True)
        # Check the Cancel button:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cancelLink']"), True)

        # Check the 20 items on the page:
        # elements = self.driver.find_elements_by_css_selector("[data-test-id='remove']")
        elements = self.driver.find_elements_by_xpath("//button[@data-test-id='remove']")
        self.assertIs(True, elements[0].is_displayed())
        self.assertIs(True, elements[19].is_displayed())

        # Go to Next page:
        HelperTestBase.reliableClick(self, "[data-test-id='goToNextPage']")
        time.sleep(2)
        self.assertEqual(text1, SheetsPage.getPageNumber(self))

        # Go to Next page:
        HelperTestBase.reliableClick(self, "[data-test-id='goToNextPage']")
        time.sleep(2)
        self.assertEqual(text2, SheetsPage.getPageNumber(self))

        # Go to Previous page:
        HelperTestBase.reliableClick(self, "[data-test-id='goToPreviousPage']")
        time.sleep(2)
        self.assertEqual(text1, SheetsPage.getPageNumber(self))



        # Go to Last page:
        HelperTestBase.reliableClick(self, "[data-test-id='goToLastPage']")
        time.sleep(2)
        self.assertEqual(text4, SheetsPage.getPageNumber(self))

        # Go to First page:
        HelperTestBase.reliableClick(self, "[data-test-id='goToFirstPage']")
        time.sleep(2)
        self.assertEqual(text, SheetsPage.getPageNumber(self))

        # Check the 20 items on the next page:

        elements1 = self.driver.find_elements_by_css_selector("[data-test-id='remove']")
        self.assertIs(True, elements1[0].is_displayed())
        self.assertIs(True, elements1[20].is_displayed())

    # @pytest.mark.skip
    def test_checkRemoveItem_3FromInventoryList(self):
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        url4 = self.base_url + '/inventory-sheet'
        text = 'Remove item?'
        text1 = 'Are you sure you want to remove this item?'
        x = StringGenerator('[\c]{5}').render()

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestavm', 'Ss123456')

        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-0"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-1"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-2"))

        SheetsPage.openSheets(self)
        time.sleep(5)
        self.assertEqual(url4, HelperTestBase.getURL(self))
        elements = self.driver.find_elements_by_css_selector("[data-test-id='remove']")
        self.assertIs(True, elements[0].is_displayed())
        self.assertIs(True, elements[1].is_displayed())
        self.assertIs(True, elements[2].is_displayed())

        SheetsPage.deleteItem(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        elements = self.driver.find_elements_by_css_selector("[data-test-id='remove']")
        self.assertIs(True, elements[0].is_displayed())
        self.assertIs(True, elements[1].is_displayed())
        self.assertIs(True, elements[2].is_displayed())

        SheetsPage.closeSheets(self)
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-0"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-1"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-2"))
        SheetsPage.openSheets(self)
        SheetsPage.deleteItem(self)
        HelperTestBase.clickYesButton(self)
        HelperTestBase.clickYesButton(self)

        SheetsPage.closeSheets(self)
        HelperTestBase.waitElement(self, "[data-test-id='inventoryItem-0")
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-0"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-1"))
        self.assertEqual(len(HelperTestBase.checkElementExist(self, "[data-test-id='inventoryItem-2']")), 0)
        # Returne test data:
        self.driver.refresh()
        time.sleep(4)

        ProductEditorPage.addProductWithoutYear(self,
                                                title='Test Item' + x,
                                                description='test' + x,
                                                price='1',
                                                sortUnits='Each',
                                                currentQuantityInp='10', sortQTY='Each',
                                                country='Canada', productCodeInp='test',
                                                salePrice='1', sortSalePrice='Each')
        time.sleep(5)
        HelperTestBase.clickYesButton(self)

    #@pytest.mark.skip
    def test_checkRemoveItemCheck20Items(self):
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        url4 = self.base_url + '/inventory-sheet'
        text = 'Remove item?'
        text1 = 'Are you sure you want to remove this item?'
        x = StringGenerator('[\c]{5}').render()

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')

        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-0"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-1"))
        self.assertEqual(True, HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-30"))

        SheetsPage.openSheets(self)

        elements = self.driver.find_elements_by_css_selector("[data-test-id='remove']")
        self.assertIs(True, elements[0].is_displayed())
        self.assertIs(True, elements[19].is_displayed())

        SheetsPage.deleteItem(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        self.assertEqual(len(self.driver.find_elements_by_css_selector("[data-test-id='remove']")), 38)
        SheetsPage.closeSheets(self)
        SheetsPage.openSheets(self)
        self.assertEqual(len(self.driver.find_elements_by_css_selector("[data-test-id='remove']")), 40)
        SheetsPage.closeSheets(self)

        ProductEditorPage.addProductWithoutYear(self,
                                                title='Test Item' + x,
                                                description='test' + x,
                                                price='1',
                                                sortUnits='Each',
                                                currentQuantityInp='10', sortQTY='Each',
                                                country='Canada', productCodeInp='test',
                                                salePrice='1', sortSalePrice='Each')
        time.sleep(1)
        HelperTestBase.clickYesButton(self)
