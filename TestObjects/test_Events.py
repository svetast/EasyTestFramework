import time

from HelperTestBase import HelperTestBase
from PageObjects.AddEventPage import AddEventPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductEditorPage import ProductEditorPage
from PageObjects.SearchScreenPage import SearchScreenPage


class TestEvents(AddEventPage):
    ### Test scope - Type the 'Mars' into Search input, click Enter =>	The list of 'Mars' items are displayed.
    # @pytest.mark.skip
    def test_Add_Remove_EventAction(self):
        url2 = self.base_url + '/event'
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/product-editor'
        text1 = 'Success:'
        text2 = 'The item has been successfully updated.'
        text7 = 'The event has been successfully processed!'
        text3 = 'Remove event?'
        text4 = 'Are you sure you want to remove this event?'
        text5 = 'Warning:'
        text6 = 'This item has already been presented on this market!'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        ### add new Event :
        ProductEditorPage.goProductEditor(self)
        ProductEditorPage.addEventAction(self)
        SearchScreenPage.submitSearchMarketEvent(self, 'mars')
        time.sleep(3)
        #### Test scope - Search the Mars market => the elements are present in the list:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_1']"), True)
        AddEventPage.selectMarket(self)
        # Click on Save button => the appropriate message is displayed:
        ProductEditorPage.clickSaveButton(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text7, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # Click on delete button on Event => the appropriate message is displayed:
        HelperTestBase.clickAndWait(self, "[data-test-id='removeEvent']")
        self.assertEqual(text3, HelperTestBase.getModalHeader(self))
        self.assertEqual(text4, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(2)
        ProductEditorPage.clickSaveButton(self)

    def test_checkEventDuplicate(self):
        url2 = self.base_url + '/event'
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/product-editor'
        text1 = 'Success:'
        text2 = 'The item has been successfully updated.'
        text7 = 'The event has been successfully processed!'
        text3 = 'Remove event?'
        text4 = 'Are you sure you want to remove this event?'
        text5 = 'Warning:'
        text6 = 'This item has already been presented on this market!'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        ### add new Event :
        ProductEditorPage.goProductEditor(self)
        ProductEditorPage.addEventAction(self)
        SearchScreenPage.submitSearchMarketEvent(self, 'mars')
        time.sleep(3)
        #### Test scope - Search the Mars market => the elements are present in the list:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_1']"), True)
        AddEventPage.selectMarket(self)
        # Click on Save button => the appropriate message is displayed:
        ProductEditorPage.clickSaveButton(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text7, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)

        ProductEditorPage.addEventAction(self)
        SearchScreenPage.submitSearchMarketEvent(self, 'mars')
        AddEventPage.selectMarket(self)
        # Add duplicate event and click on Save button => the appropriate Warning message is displayed:
        self.assertEqual(text5, HelperTestBase.getModalHeader(self))
        self.assertEqual(text6, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        HelperTestBase.clickBack(self)

        # Click on delete button on Event => the appropriate message is displayed:
        HelperTestBase.clickAndWait(self, "[data-test-id='removeEvent']")
        self.assertEqual(text3, HelperTestBase.getModalHeader(self))
        self.assertEqual(text4, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(2)
        ProductEditorPage.clickSaveButton(self)



























    def test_Events_edit(self):
        """
        Assume, we have to check editing event's setting (sales)
        Fails because of bug with Market
        """

        """
        Login
        """
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', "Ss123456")

        """
        Switch to seller mode, choose first item and click market

        """
        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='inventoryItem-0']")
        HelperTestBase.reliableClick(self, "[data-test-id='eventTitle']")
        time.sleep(5)

        """
        Click Sale is on switch and check changes
        """
        organicSwitch = driver.find_element_by_css_selector("[data-test-id='organicSwitch']")
        organicSwitchState = organicSwitch.get_attribute("ng-reflect-state")
        organicSwitch.click()
        time.sleep(2)

        new_organicSwitchState = organicSwitch.get_attribute("ng-reflect-state")
        self.assertNotEqual(organicSwitchState, new_organicSwitchState)  # if it was changed
        time.sleep(2)

        """
        Set price 100 and unit Box
        """
        salePriceInp = driver.find_element_by_css_selector("[data-test-id='salePriceInp']")
        salePriceInp.click()
        salePriceInp.send_keys("100")
        time.sleep(2)

        el = driver.find_element_by_name('saleUnitName')
        for option in el.find_elements_by_tag_name('option'):
            if option.get_attribute("data-test-id") == 'Box':
                option.click()  # select() in earlier versions of webdriver
                break

        time.sleep(2)

        """
        Save changes
        """
        HelperTestBase.reliableClick(self, "[data-test-id='saveBtn']")
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        time.sleep(1)

        HelperTestBase.reliableClick(self, "[data-test-id='eventTitle']")
        time.sleep(5)

        """
        Check changes after save
        """
        organicSwitch = driver.find_element_by_css_selector("[data-test-id='organicSwitch']")
        organicSwitchState = organicSwitch.get_attribute("ng-reflect-state")
        self.assertEqual(organicSwitchState, new_organicSwitchState)
        time.sleep(2)

        salePriceInp = driver.find_element_by_css_selector("[data-test-id='salePriceInp']")
        salePriceInpValue = salePriceInp.get_attribute("value")
        self.assertEqual("100", salePriceInpValue)
        time.sleep(5)

        saleUnit = driver.find_element_by_css_selector("[ng-reflect-name='saleUnit']")
        saleUnitValue = salePriceInp.get_attribute("ng-reflect-value")
        self.assertEqual("Box", saleUnitValue)
        time.sleep(5)

        ### Test scope - Seller clicks on Add Events => 'Search market' page is opened:
        # @pytest.mark.skip

    def test_clickAddEventButton(self):
        url2 = self.base_url + '/event'
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/product-editor'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        ProductEditorPage.goProductEditor(self)
        ProductEditorPage.addEventAction(self)
        #### Test scope - the elements are present:

        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"), True)

        ### Test scope - Click on < button  => 'ProductEditor page' page is opened:

        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(2)
        self.assertEqual(url1, HelperTestBase.getURL(self))


        # @pytest.mark.skip

    def test_checkEventRedirectToMarketPage(self):
        url2 = 'http://www.moontwp.com/'
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/product-editor'
        urlMarket = 'http://www.lemarsiowa.com/'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        ProductEditorPage.goProductEditor(self)
        ProductEditorPage.addEventAction(self)
        SearchScreenPage.submitSearchMarketEvent(self, 'mars')
        time.sleep(3)
        #### Test scope - Search the Mars market => the elements are present in the list:
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='abstractListProduct_1']"), True)
        AddEventPage.selectMarket(self)
        ProductEditorPage.clickSaveButton(self)
        HelperTestBase.clickYesButton(self)
        time.sleep(3)

        # Test scope - click on event title => the market title is present, Cancel button is present:

        ProductEditorPage.clickEventTitle(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='marketTitle']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cancelLink']"), True)
        # Test scope - click on Cancel icon => Product editor is opened:
        HelperTestBase.clickAndWait(self, "[data-test-id='cancelLink']")
        self.assertEqual(url1, HelperTestBase.getURL(self))

        ProductEditorPage.clickEventTitle(self)
        # Test scope - click on market title => market page is opened:
        HelperTestBase.reliableClick(self, "[data-test-id='marketWebPage']")
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])
        HelperTestBase.waitURL(self, urlMarket)
        self.assertEqual(urlMarket, HelperTestBase.getURL(self))

        driver.switch_to_window(driver.window_handles[0])
        HelperTestBase.clickAndWait(self, "[data-test-id='cancelLink']")
        time.sleep(4)

        # Click on delete button on Event => the appropriate message is displayed:
        HelperTestBase.clickAndWait(self, "[data-test-id='removeEvent']")
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProductEditorPage.clickSaveButton(self)
