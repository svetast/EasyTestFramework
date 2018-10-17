import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.MessagesPage import MessagesPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ShopperDetailsPage import ShopperDetailsPage


class TestMessages(NavigationMenuPage, MessagesPage, ShopperDetailsPage):
    # ## Test scope -  Check the elements on Messaging page =>	The are present:  < button, Search field, Messages list, Date
    # @pytest.mark.skip
    def test_checkElements(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/dialogs'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        # NavigationMenuPage.clickMessages(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='dialogs']")
        time.sleep(3)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchCancel']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialog_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='removeItem']"), True)

    ## Test scope -  For Seller: Check the elements on Messaging page =>	The are present: < button, Search field, Messages list, Date
    # @pytest.mark.skip
    def test_checkElementsForSeller(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/dialogs'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        NavigationMenuPage.clickSellerButton(self)
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='dialogs']")
        time.sleep(3)
        # NavigationMenuPage.clickMessages(self)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchCancel']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='dialog_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='removeItem']"), True)



        ### Test scope Buyer clicks on "<" button => The Shopping list  is opened

    #@pytest.mark.skip
    def test_clickBackBuyer(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/dialogs'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        NavigationMenuPage.clickMessages(self)
        # time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        HelperTestBase.clickBackButton(self)
        # time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))

    ### Test scope Seller clicks on "<" button	=> The Inventory list  is opened
        # @pytest.mark.skip
    def test_clickBackSeller(self):
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/inventory-list'
        url2 = self.base_url + '/dialogs'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        NavigationMenuPage.clickSellerButton(self)
        # time.sleep(5)
        NavigationMenuPage.clickMessages(self)
        #time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        HelperTestBase.clickBackButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # @pytest.mark.skip

    # def test_checkData(self):
    #     url1 = self.base_url + '/shopping-list'
    #     url = self.base_url + '/inventory-list'
    #     url2 = self.base_url + '/dialogs'
    #     text1 = 'Remove dialog?'
    #     text2 = 'Test message'
    #
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     LoginPage.loginAction(self, 'SellerTestsvy', 'Ss123456')
    #     time.sleep(3)
    #
    #     NavigationMenuPage.clickMessages(self)
    #     time.sleep(2)
    #     elem = self.driver.find_elements_by_css_selector("[data-test-id='removeItem']")
    #     if (elem[0] == False):
    #         HelperTestBase.clickAndWait(self, "[data-test-id='shoppingLink']")
    #         ShopperDetailsPage.clickSellerName(self)
    #         ShopperDetailsPage.clickContactSellerButton(self)
    #         MessagesPage.sendMessage(self, 'Test message')
    #         # time.sleep(2)
    #         self.assertIn(text2, self.driver.page_source)
    #
    #         # else:
    #         #     HelperTestBase.clickAndWait(self, "[data-test-id='shoppingLink']")
    #         #     #     ShopperDetailsPage.clickSellerName(self)
    #         #     #     ShopperDetailsPage.clickContactSellerButton(self)
    #         #     #     MessagesPage.sendMessage(self, 'Test message')
    #         #     # # time.sleep(2)
    #         #     #     self.assertIn(text2, self.driver.page_source)
    #


    ### Test scope : Buyer clicks on "delete" button	=> The message is deleted.
    # @pytest.mark.skip
    def test_removeMessageBuyer(self):
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/inventory-list'
        url2 = self.base_url + '/dialogs'
        text1 = 'Remove dialog?'
        text2 = 'Test message'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(3)

        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickContactSellerButton(self)
        time.sleep(5)
        MessagesPage.sendMessage(self, 'Test message')
        self.assertIn(text2, self.driver.page_source)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(5)
        NavigationMenuPage.clickMessages(self)
        time.sleep(2)
        MessagesPage.removeMessage(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickCancelButton(self)
        MessagesPage.removeMessage(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickYesButton(self)


    ### Test scope Seller clicks on "delete" button	=> The message is deleted.
    #@pytest.mark.skip
    def test_removeMessageSeller(self):
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/inventory-list'
        url2 = self.base_url + '/dialogs'
        text1 = 'Remove dialog?'
        text2 = 'Test message'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        time.sleep(5)
        ShopperDetailsPage.clickSellerName(self)
        ShopperDetailsPage.clickContactSellerButton(self)
        MessagesPage.sendMessage(self, 'Test message')
        self.assertIn(text2, self.driver.page_source)
        self.driver.refresh()
        time.sleep(5)
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(5)
        NavigationMenuPage.clickMessages(self)
        time.sleep(2)
        MessagesPage.removeMessage(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickCancelButton(self)
        MessagesPage.removeMessage(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        HelperTestBase.clickYesButton(self)


    # @pytest.mark.skip
    def test_createMessage(self):
        # Test scope: Buyer is creating message	=> The message is created"
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/inventory-list'
        url2 = self.base_url + '/dialogs'
        text1 = 'Test message'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')

        ShopperDetailsPage.clickSellerName(self)
        # time.sleep(2)
        ShopperDetailsPage.clickContactSellerButton(self)
        #  time.sleep(2)
        MessagesPage.sendMessage(self, 'Test message')
        self.assertIn(text1, self.driver.page_source)

    #@pytest.mark.skip

    def test_checkFilterMessage(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/dialogs'
        driver = self.driver
        driver.get(self.base_url)
        text = 'svetast'
        text1 = 'Bob'
        text3 = 'Empty'
        text4 = 'shopper'

        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        self.assertEqual(url, HelperTestBase.getURL(self))
        NavigationMenuPage.clickMessages(self)

        ### Test scope User SA1 /Bizibaza111 types 'sv' into search field =>	'svetast' is displayed in search results.
        MessagesPage.searchMessage(self, 'sv')
        self.assertEqual(text, HelperTestBase.getText(self, "[data-test-id='dialog-name_']"))

        #### Click on 'cancel'	The search field is clear
        MessagesPage.clickCancel(self)
        ### Test scope User SA1 /Bizibaza111 types 'sh' into search field =>	'shooper' is displayed in search results.
        MessagesPage.searchMessage(self, 'sh')
        self.assertEqual(text4, HelperTestBase.getText(self, "[data-test-id='dialog-name_']"))
        MessagesPage.clickCancel(self)
        ### Test scope User SA1 /Bizibaza111 types 'b' into search field =>	'Buyer' is displayed in search results.
        MessagesPage.searchMessage(self, 'b')
        self.assertEqual(text1, HelperTestBase.getText(self, "[data-test-id='dialog-name_']"))
        #### Test scope - Click on 'cancel'	The search field is clear
        MessagesPage.clickCancel(self)
        ### Test scope User SA1 /Bizibaza111 types 'q' into search field =>	'Empty' is displayed
        MessagesPage.searchMessage(self, 'q')
        self.assertIn(text3, self.driver.page_source)

