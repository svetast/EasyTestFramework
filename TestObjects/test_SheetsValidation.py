import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SheetsPage import SheetsPage


class TestSheetsValidation(SheetsPage, ProductEditorPage):
    def test_checkXSSValidation(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        text = 'alert(&#34;xss-injection!&#34;)'
        text2 = '<script>'
        text1 = '<script>alert("xss-injection!")</script>'
        LoginPage.loginAction(self, 'SellerTestege', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        SheetsPage.openSheets(self)
        time.sleep(2)
        # Checking on XSS injections :
        SheetsPage.editProductItemField(self, '<script>alert("xss-injection!")</script>')
        SheetsPage.editSellerNameField(self, '<script>alert("xss-injection!")</script>')
        SheetsPage.editDescription(self, '<script>alert("xss-injection!")</script>')
        SheetsPage.editProductCode(self, '<script>alert("xss-injection!")</script>')
        SheetsPage.clickSaveButton(self)
        HelperTestBase.clickYesButton(self)
        SheetsPage.closeSheets(self)
        SheetsPage.openSheets(self)
        time.sleep(5)
        self.assertNotIn(text1, self.driver.page_source)
        self.assertIsNot(True, self.driver.switch_to_active_element)

        # return test data:
        SheetsPage.editProductItemField(self, 'Test Item')
        SheetsPage.editSellerNameField(self, 'Test Description')
        SheetsPage.editDescription(self, 'Test Description')
        SheetsPage.editProductCode(self, 'Test Product Code')
        SheetsPage.clickSaveButton(self)
        HelperTestBase.clickYesButton(self)

    # @pytest.mark.skip
    def test_checkValidationFieldsBlocked(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestlhc', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)

        # Check that Record field is blocked:
        SheetsPage.openSheets(self)
        SheetsPage.clickOnRecordField(self)
        self.assertEqual(False, hasattr(SheetsPage.clickOnRecordField(self), 'send_keys'))

        # Check that Category field is blocked:
        SheetsPage.clickOnCategoryField(self)
        self.assertEqual(False, hasattr(SheetsPage.clickOnCategoryField(self), 'send_keys'))

        # Check that SubCategory field is blocker:
        SheetsPage.clickOnSubCategoryField(self)
        self.assertEqual(False, hasattr(SheetsPage.clickOnSubCategoryField(self), 'send_keys'))

        # Check that SubCategoryEntry field is blocked:
        SheetsPage.clickOnSubCategoryEntryField(self)
        self.assertEqual(False, hasattr(SheetsPage.clickOnSubCategoryEntryField(self), 'send_keys'))

        # @pytest.mark.skip

    def test_checkPriceValidation(self):
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            text = 'Error:'
            text1 = 'Item #1 - Unacceptable PRICE value. Must be above zero.'
            text3 = '$123'
            text4 = '$54'
            LoginPage.loginAction(self, 'SellerTestege', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            SheetsPage.openSheets(self)
            time.sleep(2)
            SheetsPage.editPrice(self, '-1')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editPrice(self, '0')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editPrice(self, '123#456Afghj')
            self.assertIn(text3, self.driver.page_source)

            SheetsPage.editPrice(self, '054')
            time.sleep(2)
            self.assertIn(text4, self.driver.page_source)

            SheetsPage.editPrice(self, '')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editPrice(self, '<script>alert("xss-injection!")</script>')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

        # @pytest.mark.skip

    def test_checkSalePriceValidation(self):
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            text = 'Error:'
            text1 = 'Item #1 - Unacceptable SALE PRICE value. Must be above zero.'
            text3 = '$123'
            text4 = '$54'
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            SheetsPage.openSheets(self)
            time.sleep(3)
            SheetsPage.editSalePriceField(self, '-1')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editSalePriceField(self, '0')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editSalePriceField(self, '123asdf')
            self.assertIn(text3, self.driver.page_source)

            SheetsPage.editSalePriceField(self, '054')
            time.sleep(2)
            self.assertIn(text4, self.driver.page_source)

            SheetsPage.editSalePriceField(self, '<script>alert("xss-injection!")</script>')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

        # @pytest.mark.skip

    def test_checkAvailableQuantityValidation(self):
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            text = 'Error:'
            text6 = 'Item #1 - Unacceptable AVAILABLE QUANTITY value. Must be zero or above.'
            text1 = 'Item#1 - Field AVAILABLE QUANTITY is required. Please, fill it in.'
            text5 = 'Incorrect value type for QTYUNITID field.'
            text7 = 'Item#1 - Field AVAILABLE QUANTITY is required. Please, fill it in.'
            text3 = '$123'
            text4 = '543'
            LoginPage.loginAction(self, 'SellerTestege', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            SheetsPage.openSheets(self)
            time.sleep(2)
            SheetsPage.editAvailableQuantity(self, '-1')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text6, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editAvailableQuantity(self, '0')
            SheetsPage.clickSaveButton(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editAvailableQuantity(self, '123#456Afghj')
            SheetsPage.clickSaveButton(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text7, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editAvailableQuantity(self, '054')
            SheetsPage.clickSaveButton(self)
            time.sleep(2)
            self.assertIn(text4, self.driver.page_source)

            SheetsPage.editAvailableQuantity(self, '')
            SheetsPage.clickSaveButton(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            SheetsPage.editAvailableQuantity(self, '<script>alert("xss-injection!")</script>')
            SheetsPage.clickSaveButton(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            ##### Returt test data:
            SheetsPage.editAvailableQuantity(self, '543')
            time.sleep(2)
            self.assertIn(text4, self.driver.page_source)

        # @pytest.mark.skip

    def test_checkCountryValidation(self):
            driver = self.driver
            driver.maximize_window()
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SellerTestege', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            SheetsPage.openSheets(self)
            time.sleep(2)
            SheetsPage.selectCountry(self, text='Canada')
            SheetsPage.clickSaveButton(self)
            HelperTestBase.clickYesButton(self)

            SheetsPage.selectCountry(self, text='Panama')
            SheetsPage.clickSaveButton(self)
            HelperTestBase.clickYesButton(self)

            SheetsPage.selectCountry(self, text='Country')
            SheetsPage.clickSaveButton(self)
            HelperTestBase.clickYesButton(self)
