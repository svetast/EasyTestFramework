import time

from strgen import StringGenerator

from HelperTestBase import HelperTestBase
from PageObjects.InventoryListPage import InventoryListPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage


class TestProductEditor(ProductEditorPage):
    # Test scope -  Check the elements on Product Editor page =>	The elements are present:
    # @pytest.mark.skip

    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/product-editor'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(5)

        # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
        # ProductEditorPage.goProductEditor(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='inventoryItem-0']")
        time.sleep(5)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cancelLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Product Item']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Seller Name']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='uploadImg']"), True)
        self.assertIs(HelperTestBase.checkElement(self, "description"), True)
        self.assertIs(HelperTestBase.checkElement1(self, "point-container"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='sellingPriceInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='priceUnitsName']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='currentQuantityInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='qtyUnitName']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='productCodeInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='deliveryOfferedSwitch']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='pickUpOfferedSwitch']"), True)
        years = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        self.assertIs(years[0].is_displayed(), True)
        self.assertIs(years[1].is_displayed(), True)
        self.assertIs(years[2].is_displayed(), True)
        self.assertIs(years[3].is_displayed(), True)
        self.assertIs(years[4].is_displayed(), True)
        months = self.driver.find_elements_by_css_selector("[data-test-id='monthSelect']")
        self.assertIs(months[0].is_displayed(), True)
        self.assertIs(months[1].is_displayed(), True)
        self.assertIs(months[2].is_displayed(), True)
        self.assertIs(months[3].is_displayed(), True)
        self.assertIs(months[4].is_displayed(), True)
        days = self.driver.find_elements_by_css_selector("[data-test-id='daySelect']")
        self.assertIs(days[0].is_displayed(), True)
        self.assertIs(days[1].is_displayed(), True)
        self.assertIs(days[2].is_displayed(), True)
        self.assertIs(days[3].is_displayed(), True)
        self.assertIs(days[4].is_displayed(), True)
        hours = self.driver.find_elements_by_css_selector("[data-test-id='hourSelect']")
        self.assertIs(hours[0].is_displayed(), True)
        self.assertIs(hours[1].is_displayed(), True)
        self.assertIs(hours[2].is_displayed(), True)
        self.assertIs(hours[3].is_displayed(), True)
        self.assertIs(hours[4].is_displayed(), True)
        minute = self.driver.find_elements_by_css_selector("[data-test-id='minuteSelect']")
        self.assertIs(minute[0].is_displayed(), True)
        self.assertIs(minute[1].is_displayed(), True)
        self.assertIs(minute[2].is_displayed(), True)
        self.assertIs(minute[3].is_displayed(), True)
        self.assertIs(minute[4].is_displayed(), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='countrySelect']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='organicSwitch']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='salePriceInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='saleUnitName']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='activeSwitch']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='saveBtn']"), True)

        ### Test scope -  Click on 'Save' button =>	The "Success! The item has been successfully updated." is displayed:
        # @pytest.mark.skip

    def test_clickSaveButton(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/product-editor'
        url1 = self.base_url + '/inventory-list'
        text = 'Success:'
        text1 = 'The item has been successfully updated.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        ###### Test scope - check available item after editing:    ###########
        ProductEditorPage.goProductEditor(self)
        ProductEditorPage.clickSaveButton(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

    def test_addProductSuccess(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/product-editor'
        url1 = self.base_url + '/inventory-list'
        text = 'Success:'
        text1 = 'A new item has been successfully created.'
        text3 = 'Remove item?'
        text4 = 'Are you sure you want to remove this item?'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        # LoginPage.loginAction(self, 'SellerTesttze', 'Ss123456')
        time.sleep(5)

        x = StringGenerator('[\c]{5}').render()

        ProductEditorPage.addProductWithoutYear(self,
                                                title='Test Item ' + x,
                                                description='test',
                                                price='1',
                                                sortUnits='Each',
                                                currentQuantityInp='10', sortQTY='Each',
                                                country='Canada', productCodeInp='test',
                                                salePrice='1', sortSalePrice='Each')
        time.sleep(5)

        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.driver.refresh()
        time.sleep(5)
        ##### RETURT to start-
        NavigationMenuPage.clickSellerButton(self)
        InventoryListPage.deleteItem(self)
        self.assertEqual(text3, HelperTestBase.getModalHeader(self))
        self.assertEqual(text4, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)



        # Test scope - Click on Cancel button =>   Cancel editing?  All your changes will be lost!"" is displayed
        # Click on NO button => The Product Editor page is displayed
        # Click on YES button => Inventory list is displayed


        ###  Click on 'Cancel' button => 'Cancel editing? All your changes will be lost!' is displayed:

    # @pytest.mark.skip
    def test_clickCancelButton(self):
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/product-editor'
            url1 = self.base_url + '/inventory-list'
            text = 'Cancel editing?'
            text1 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            NavigationMenuPage.clickSellerButton(self)
            time.sleep(3)
            ProductEditorPage.goProductEditor(self)
            ProductEditorPage.clickCancel(self)

            # HelperTestBase.clickAndWait(self, "[data-test-id='inventoryItem-0']")
            # self.assertEqual(url2, HelperTestBase.getURL(self))
            # self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cancelLink']"), True)
            # HelperTestBase.clickAndWait(self, "[data-test-id='cancelLink']")
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            time.sleep(3)
            self.assertEqual(url1, HelperTestBase.getURL(self))
            # Test scope - check available item after editing:
            ProductEditorPage.goProductEditor(self)
            ProductEditorPage.clickSaveButton(self)
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

            # def test_getMessageIfEmptyInventoryList(self):
            #         #### Test scope - Click on Seller if user hasn't item in Inventory List=> 'Error: Items not found.' is displayed:
            #         url = self.base_url + '/shopping-list'
            #         url2 = self.base_url + '/product-editor'
            #         url1 = self.base_url + '/inventory-list'
            #         text = 'Error:'
            #         text1 = 'Items not found'
            #         driver = self.driver
            #         driver.get(self.base_url)
            #         LoginPage.loginAction(self, 'Bob', 'Ss123456')
            #         time.sleep(5)
            #         self.assertEqual(url, HelperTestBase.getURL(self))
            #         NavigationMenuPage.clickSellerButton(self)
            #         self.assertEqual(text, HelperTestBase.getModalHeader(self))
            #         self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            #         HelperTestBase.clickYesButton(self)
            #         self.assertEqual(url1, HelperTestBase.getURL(self))


















            #  Test scope - checking of requirement fields:
            # @pytest.mark.skip

    def test_EmptyFields(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text0 = 'The field TITLE is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)

            ProductEditorPage.setTitleOnly(self, '')
            time.sleep(3)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text0, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_checkWitoutPrice(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'The field SELLING PRICE is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            ProductEditorPage.setTitleOnly(self, 'Test Item')
            time.sleep(5)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_checkWitoutUnits(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'The field UNITS (after Selling price field) is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            HelperTestBase.waitSettingsButton(self)

            ProductEditorPage.setPrice(self, 'Test Item', '2')
            time.sleep(3)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)


            # @pytest.mark.skip

    def test_checkWithoutQTY(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'The field AVAILABLE QUANTITY is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(2)
            ProductEditorPage.setQTY(self, title='Test Apple', price='2', avaiableQuantityInp='')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_checkWitoutSortQTY(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'The field UNITS (after Available quantity field) is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            self.assertEqual(url, HelperTestBase.getURL(self))
            ProductEditorPage.setQTY(self, 'Test Apple', '2', '3')
            time.sleep(3)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_checkWithCountryWithoutDeliveryMethod(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'You should choose DELIVERY method.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)

            ProductEditorPage.setCountryWithoutDeliveryMethod(self, 'Test Apple', '2', '3', 'Afghanistan')
            time.sleep(3)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_setDeliveryMethodWitoutCountry(self):
            url = self.base_url + '/shopping-list'
            text = 'Success:'
            text1 = 'The field COUNTRY OF ORIGIN is required. Please, fill it in.'
            text2 = 'A new item has been successfully created.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)

            ProductEditorPage.setDeliveryMethodWitoutCountry(self, title='Test Item Apple', price='2',
                                                             avaiableQuantityInp='3')
            time.sleep(3)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text2, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            InventoryListPage.deleteItem(self)
            HelperTestBase.clickYesButton(self)


            # @pytest.mark.skip

    def test_setInvalidPrice(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'Unacceptable PRICE value!'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            ProductEditorPage.setInvPrice(self, title='Test Item', price='Asdf!@#$%')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            # self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_setInvalidQTY(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'Unacceptable QUANTITY value!'
            text5 = 'The field AVAILABLE QUANTITY is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)


            # ProductEditorPage.addProductWithoutYear(self, title='Test Product', price='2',
            #                       description='test', sortUnits='Each',
            #                       currentQuantityInp='asdf', sortQTY='Each',
            #                       country='Canada', productCodeInp='#test',
            #                       salePrice='1', sortSalePrice='Each')
            ProductEditorPage.openProductEditor(self)
            ProductEditorPage.setTitle(self, 'Test Apple')
            ProductEditorPage.setPrice1(self, '2')
            ProductEditorPage.sortUnits(self, 'Each')
            ProductEditorPage.clickSaveButton(self)

            # ProductEditorPage.setQTY(self, title='Test Product', price='2', currentQuantityInp='Asdf')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text5, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            ##### delete the new item from Inventory List:
            InventoryListPage.deleteItem(self)

            # @pytest.mark.skip

    def test_setInvalidSalePrice(self):
            url = self.base_url + '/shopping-list'
            text = 'Error:'
            text1 = 'Unacceptable price value!'
            text4 = 'The field AVAILABLE QUANTITY is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)

            ProductEditorPage.setInvalidSalePrice(self, title='Test Kolobok', price="3", salePrice='@#$%^&asdfg',
                                                  avaiableQuantityInp='1', country='Canada')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))

            # @pytest.mark.skip

    def test_addProductWithoutTitle(self):
            url = self.base_url + '/shopping-list'
            text1 = 'The field TITLE is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            text = 'Error:'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            self.assertEqual(url, HelperTestBase.getURL(self))
            ProductEditorPage.setTitleOnly(self, '')
            time.sleep(5)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_addProductEmptyFields(self):
            url = self.base_url + '/shopping-list'
            text1 = 'The field TITLE is required. Please, fill it in.'
            text11 = 'Cancel editing?'
            text12 = 'All your changes will be lost!'
            text = 'Error:'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(3)
            ProductEditorPage.setTitleOnly(self, '')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ProductEditorPage.clickCancel(self)
            self.assertEqual(text11, HelperTestBase.getModalHeader(self))
            self.assertEqual(text12, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)

            # @pytest.mark.skip

    def test_editProduct(self):
            # Test scope - Edit the product> click Save button => the changes are saved:

            url = self.base_url + '/shopping-list'
            text1 = 'The item has been successfully updated.'
            text = 'Success:'
            text3 = 'New Sveta'
            text4 = 'Test New Item Test'
            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'Bob', 'Ss123456')
            time.sleep(5)
            self.assertEqual(url, HelperTestBase.getURL(self))
            ProductEditorPage.editProduct(self, 'New Sveta')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            self.assertIn(text3, self.driver.page_source)

            ##Test scope - user can re-change after the changes have been saved

            ProductEditorPage.editProduct(self, 'Test New Item Test')
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            self.assertIn(text4, self.driver.page_source)
