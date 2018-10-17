import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.ShoppingListPage import ShoppingListPage


class TestShoppingList(ShoppingListPage):
    ## Test scope -  Check the web elements => Log Out button, Search button, Add new item field,
    ### Delete item button, Status item button, Edit item button, NavigationMenu button, CategoriesMenu button are present:

    #@pytest.mark.skip
    def test_chekElementsPresent(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'testhdzzr', 'Ss123456')
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='searchLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='settingsLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='addNewInput']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='removeBtn_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='statusBtn_0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='footerMainBtn']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='showCategoriesBtn']"), True)









        ### Test scope -  Click on Search icon on the Shopping List page =>	The 'Search' form is displayed
        # Input Search, Filter, LigIn link are displayed
        # Click on < button => Shopping List is opened ########

    # @pytest.mark.skip
    def test_clickSearchButton(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/search'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'testlvqvj', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")
        time.sleep(2)
        HelperTestBase.wait(self, "[data-test-id='filterBtn']")
        HelperTestBase.wait(self, "[data-test-id='searchInp']")
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))



        ### Test scope -  Type "test item" into '+New item title' field	The 'test tiem' added to shopping list

    #@pytest.mark.skip
    def test_AddRemoveItemTitle(self):
        url = self.base_url + '/shopping-list'
        text1 = 'Test Item1'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testohbms', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        HelperTestBase.setText(self, "[data-test-id='addNewInput']", "Test Item1")
        time.sleep(2)
        # HelperTestBase.checkState(self, "[data-test-id='shoppingListProduct']")
        self.assertIn(text1, driver.page_source)
        # self.assertEqual(text1, HelperTestBase.getText(self, "[data-test-id='shoppingListItemTitle']"))
        # driver.refresh()
        HelperTestBase.waitSettingsButton(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='removeBtn_0']")
        self.driver.refresh()
        self.assertNotIn(text1, driver.page_source)



    ###### Test scope - Click on shopping list item =>	The title of item is opened to edit,
    # edit the item, click on the  Enter => The change saved

    #@pytest.mark.skip
    def test_EditCustomListItemTitle(self):
        url = self.base_url + '/shopping-list'
        text1 = 'Kolobok'
        text2 = 'Test item'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testijewb', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        time.sleep(2)
        HelperTestBase.setText(self, "[data-test-id='shoppingListItemTitle_0']", "Test item")
        #driver.refresh()
        time.sleep(10)
        self.assertIn(text2, driver.page_source)
        # return the test data to start position:

        HelperTestBase.click(self, "[data-test-id='removeBtn_0']")
        HelperTestBase.setText(self, "[data-test-id='addNewInput']", "Kolobok")
        driver.refresh()
        time.sleep(3)
        self.assertIn(text1, driver.page_source)
        # HelperTestBase.waitElement(self, "[data-test-id='shoppingListProduct']")
        # self.assertEqual(text1, HelperTestBase.getText(self, "[data-test-id='shoppingListItemTitle']"))



        ###### Test scope - Click on shopping list item =>	The title of item is opened to edit,
        # edit the item, click on the  space => The change saved

    #@pytest.mark.skip
    def test_EditCustomListItemTitleUseSpace(self):
        url = self.base_url + '/shopping-list'
        text1 = 'Kolobok'
        text2 = 'Test item'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testzezyt', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        HelperTestBase.setText(self, "[data-test-id='shoppingListItemTitle_0']", "Test item")
        #driver.refresh()
        time.sleep(10)
        self.assertIn(text2, self.driver.page_source)
        # return the test data to start position:

        HelperTestBase.click(self, "[data-test-id='removeBtn_0']")
        ShoppingListPage.setTextUseSpace(self, "[data-test-id='addNewInput']", "Kolobok")
        #driver.refresh()
        time.sleep(10)
        self.assertIn(text1, self.driver.page_source)
        # HelperTestBase.waitElement(self, "[data-test-id='shoppingListProduct']")
        # self.assertEqual(text1, HelperTestBase.getText(self, "[data-test-id='shoppingListItemTitle']"))

        # @pytest.mark.skip

    def test_MoveToDraftCustomItemTitle(self):
        url = self.base_url + '/shopping-list'
        text1 = 'Kolobok'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testvvica', 'Ss123456')
        HelperTestBase.waitSettingsButton(self)

        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))
        HelperTestBase.clickAndWait(self, "[data-test-id='statusBtn_0']")
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='statusBtn_0']")
        time.sleep(5)
 ####### add Assert !!!!!!!!!!!!#################

    @pytest.mark.skip
    def test_add_to_SL_and_remove(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Test', "Test12345")

        HelperTestBase.reliableClick(self, "[data-test-id='showCategoriesBtn']")
        HelperTestBase.reliableClick(self, "[data-id='55e447694d9b31be099f7502']")
        HelperTestBase.reliableClick(self, "[data-test-id='subcategory_0']")

        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='entry_0']")))
        el_name = element.text
        self.driver.execute_script("arguments[0].click()", element)

        wait = WebDriverWait(self.driver, 60)
        element = driver.find_element_by_class_name("ok")
        self.assertEqual(element.text, el_name + "\n" + el_name)

        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='removeBtn_1']")

        driver.refresh()
        self.assertNotIn(el_name, driver.page_source)