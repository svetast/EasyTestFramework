from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestSellerMode(NavigationMenuPage):
    #### Valid user (Seller & Buyer) credentials - Ss / Ss1234567



    # Test scope - Click on the 'Seller' icon => The 'Inventory list'  is opened
    # @pytest.mark.skip
    def test_checkElements(self):
        url1 = self.base_url + '/inventory-list'
        url2 = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        HelperTestBase.waitSettingsButton(self)

        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")
        HelperTestBase.wait(self, "[data-test-id='inventoryItem-0']")
        self.assertEqual(url1, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryItem-0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='sheetEditorLink']"), True)


        #self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='inventoryTransition-0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='settingsLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='biziPixLink']"), True)
        self.assertEqual(url1, HelperTestBase.getURL(self))

        # Test scope - Click on the '+' button => Navigation menu is opened.
        # There are present: Messages,Watchlist, New item, Favorites, Reviews, Anaiytics, Profile :

        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.wait(self, "[data-test-id='new-item']")
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='new-item']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profile']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='watchlist']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='favorites']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='reviews']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='analytics']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialogs']"), True)

        # Test scope - Click on the '+New item' button => Categories menu is opened, there are present:
        # There categories are present : Fruits, Vegetables, Meat, Bakery, Poultry, Dairy, SeaFood, Other:

        HelperTestBase.clickAndWait(self, "[data-test-id='new-item']")
        HelperTestBase.wait(self, "[data-test-id='SeaFood']")
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='SeaFood']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Fruits']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Meat']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Poultry']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Vegetables']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Bakery']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Other']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='Dairy']"), True)

        ## Test scope - Click on 'Buyer' icon => The 'Shopping list'  is opened:
        HelperTestBase.clickAndWait(self, "[data-test-id='buyerBtn']")
        HelperTestBase.waitSettingsButton(self)
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # Test scope - Click on 'LogOut' icon	=> The message is displayed
        # @pytest.mark.skip
        def test_clickLogOut(self):
            url1 = self.base_url + '/inventory-list'
            url2 = self.base_url + '/shopping-list'
            url4 = self.base_url + '/login'
            text = 'Logout:'
            text1 = 'Do you want to logout?'
            driver = self.driver
            driver.get(self.base_url)
            # LoginPage.loginAction(self, 'Ss', 'Ss1234567')
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

            NavigationMenuPage.clickSellerButton(self)
            self.assertEqual(url1, HelperTestBase.getURL(self))
            HelperTestBase.logOutAction(self)
            self.assertEqual(text, HelperTestBase.getModalHeader(self))
            self.assertEqual(text1, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            time.sleep(5)
            self.assertEqual(url4, HelperTestBase.getURL(self))

        # @pytest.mark.skip
        def test_openSheets_Close(self):
            # Test scope - Click on 'sheetEditorLink' icon	=> The sheetEditor is opened:
            url1 = self.base_url + '/inventory-list'
            url2 = self.base_url + '/shopping-list'
            url4 = self.base_url + '/inventory-sheet'

            driver = self.driver
            driver.get(self.base_url)
            LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

            NavigationMenuPage.clickSellerButton(self)
            self.assertEqual(url1, HelperTestBase.getURL(self))
            SheetsPage.openSheets(self)
            self.assertEqual(url4, HelperTestBase.getURL(self))
            SheetsPage.closeSheets(self)
            self.assertEqual(url1, HelperTestBase.getURL(self))
