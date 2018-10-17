import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchScreenPage import SearchScreenPage


class TestSearchFunction(SearchScreenPage):
    # @pytest.mark.skip
    def test_searchFunctionAscending(self):
        # Test scope -  If product is present in DB:
        # Type the 'wipes' into search field, click on Enter => The Results are  displayed:


        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'wipes'
        text3 = 'gladiolus'

        text1 = "Test cookies DONT BUY"
        text2 = "TEST COOKIES DONT BUY"
        text3 = 'TEST COOKIES DONT BUY $4'
        text = 'cookies'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.wait(self, "[data-test-id='searchLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")
        time.sleep(2)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        HelperTestBase.setText(self, "[data-test-id='searchInp']", 'cookies')
        time.sleep(4)
        self.assertIn(text, self.driver.page_source)

        # Test scope - sorting by ascending:
        SearchScreenPage.sortItems(self, 'ascending')
        self.assertEqual(text1, HelperTestBase.getText(self, "[data-test-id='abstractListProductTitle_0']"))

    # @pytest.mark.skip
    def test_searchFunctionDescending(self):
        # Test scope - sorting by descending:

        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text1 = "Cookies -3 Test Item Don't Buy 4$"
        text3 = 'TEST COOKIES DONT BUY $4'
        text2 = "TEST COOKIES DONT BUY"
        text3 = "Test Cookies Don't buy2!"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")

        self.assertEqual(url1, HelperTestBase.getURL(self))
        HelperTestBase.setText(self, "[data-test-id='searchInp']", 'cookies')
        time.sleep(5)
        self.assertIn(text3, self.driver.page_source)
        SearchScreenPage.sortItems(self, 'descending')
        self.assertEqual(text3, HelperTestBase.getText(self, "[data-test-id='abstractListProductTitle_0']"))

        # @pytest.mark.skip
    def test_searchFunctionRate(self):
        # Test scope - sorting by rate:
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'cookies'
        text1 = "Cookies -3 Test Item Don't Buy 4$"
        text2 = "Test Cookies Don't buy2!"
        text4 = 'Test cookies DONT BUY'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        # HelperTestBase.clickSearch(self)
        HelperTestBase.reliableClick(self, "[data-test-id='searchLink']")
        # HelperTestBase.wait(self, "[data-test-id='searchLink']")
        # HelperTestBase.click(self, "[data-test-id='searchLink']")
        time.sleep(5)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        HelperTestBase.setText(self, "[data-test-id='searchInp']", 'cookies')
        time.sleep(5)
        SearchScreenPage.sortItems(self, 'rate')
        self.assertEqual(text2, HelperTestBase.getText(self, "[data-test-id='abstractListProductTitle_0']"))

    #@pytest.mark.skip
    def test_searchFunctionFilterSeller(self):
        # Test scope1 : search results for Seller 'Bob' ==  search results for 'bob' == '     Bob':
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'Search for:'
        text1 = 'Bob'
        text0 = 'Error:'
        text2 = 'Input data error'
        text3 = 'Results: 0'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.clickSearch(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SearchScreenPage.submitSearchSeller(self, 'Bob')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)

        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchSeller(self, 'bob')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)

        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchSeller(self, '    Bob')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)

        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchSeller(self, '    karabas')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        HelperTestBase.clickBack(self)

        # Test scope2 - type invalid data into search seller => Error message is displayed:
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchSeller(self, '@#$%')
        self.assertEqual(text0, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"))

    # @pytest.mark.skip
    def test_searchFunctionFilterItem(self):
        # Test scope1 : search results for item 'Cookies' ==  search results for 'cookies' == '     cookies':
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'Search for:'
        text1 = 'Gladiolus'
        text0 = 'Error:'
        text2 = 'Input data error'
        text3 = 'Results: 0'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.clickSearch(self)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        SearchScreenPage.submitSearchItem(self, 'gladiolus')
        self.assertIn(text1, self.driver.page_source)

        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchItem(self, '            gladiolus')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)

        SearchScreenPage.submitSearchItem(self, 'Gladiolus')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchItem(self, '    kolobok')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        # Test scope2 - type invalid data into search seller => Error message is displayed:
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchItem(self, '@#$%')
        time.sleep(2)
        self.assertEqual(text0, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        # Test scope - click on Close button => Error message is closed, search input is displayed:
        HelperTestBase.clickYesButton(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"))

    # @pytest.mark.skip
    def test_searchFunctionFilterMarket(self):
        # Test scope1 : search results for item 'MARC' ==  search results for 'marc' == '     Marc':
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        text = 'Search for:'
        text1 = 'Mars'
        text0 = 'Error:'
        text2 = 'Input data error'
        text3 = 'Results: 0'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.clickSearch(self)

        self.assertEqual(url1, HelperTestBase.getURL(self))
        SearchScreenPage.submitSearchMarket(self, 'Mars')

        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchMarket(self, 'MARS')
        self.assertIn(text1, self.driver.page_source)
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)
        SearchScreenPage.submitSearchMarket(self, '    mars')
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)

        SearchScreenPage.submitSearchSeller(self, '        cucurubo')
        time.sleep(2)
        self.assertIn(text3, self.driver.page_source)
        HelperTestBase.clickBack(self)
        HelperTestBase.clickSearch(self)

        time.sleep(1)
        # Test scope2 - type invalid data into search seller => Error message is displayed:
        SearchScreenPage.submitSearchMarket(self, '@#$%')
        time.sleep(1)
        self.assertEqual(text0, HelperTestBase.getModalHeader(self))
        # self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='searchInp']"))

    # @pytest.mark.skip
    def test_searchFunctionEmptyField(self):
        # Test scope - empty field in search input => there aren't search results:
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/search'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testmzmye', 'Ss123456')

        HelperTestBase.clickSearch(self)
        time.sleep(1)
        self.assertEqual(url1, HelperTestBase.getURL(self))
        HelperTestBase.setText(self, "[data-test-id='searchInp']", '')
        time.sleep(3)
        self.assertEqual(url1, HelperTestBase.getURL(self))
