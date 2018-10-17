import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.SearchScreenPage import SearchScreenPage


class TestBiziPixViewer(ProductDetailsPage, SearchScreenPage):
    '''If user hasn't BiziPix image: 1.Click on BiziPix veiwer => "User has no BiziPix image" is displayed.
     2.Click on OK button"	 => Previous (Product Details) page is open.'''

    # @pytest.mark.skip
    def test_clickBiziPixOnProductDetails(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'Sorry,'
        text2 = "this seller doesn't provide BiziPix."

        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        time.sleep(3)
        # self.assertEqual(url, HelperTestBase.getURL(self))
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='BiziPix']")
        time.sleep(3)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)

        #     If user has BiziPix image:
        #
        # 1.Click on BiziPix veiwer. => 1.The storage of items is opened.
        # 2.Click on closeButton. => 2.Previous page is open.
        # 3.Click on BiziPix veiwer. => 3.The storage of items is opened.
        # 4.Move cursor  on the product. 4."Click to buy" icon appears.
        # 5.Click on  "Click to buy" icon  = > The appropriate 'Product Details' page is opened:



        # @pytest.mark.skip

    def test_BiziPixSelectProduct(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='BiziPix']")
        ProductDetailsPage.clickCloseButton(self)
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)

    def test_BiziPix_using(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='BiziPix']")

        wait = WebDriverWait(self.driver, 100)
        cursor = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='cursor']")))
        # img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='bizipixImage']")))

        actions = ActionChains(driver)
        actions.move_to_element(cursor)
        actions.click_and_hold(cursor)
        actions.drag_and_drop_by_offset(cursor, 162, -75)
        time.sleep(2)
        actions.drag_and_drop_by_offset(cursor, 60, -80)
        time.sleep(2)
        actions.drag_and_drop_by_offset(cursor, 62, -75)

        actions.perform()
        time.sleep(3)
        HelperTestBase.reliableClick(self, "[data-test-id='bizipixCard']")
        time.sleep(6)
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"))

        # @pytest.mark.skip

    def test_BiziPix_close(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        # self.assertEqual(url, HelperTestBase.getURL(self))
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='abstractListProduct_0']")
        HelperTestBase.reliableClick(self, "[data-test-id='BiziPix']")

        HelperTestBase.reliableClick(self, "[data-test-id='closeButton']")
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)

        # @pytest.mark.skip

    def test_clickBiziPixAndBack(self):
        # Test scope - 1.click on BiziPix => Cursor is displayed.
        # 2.Move cursor to item and click on 'Click to buy' => Appropriate product is opened. Buy button is displayed.
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', 'Ss123456')
        time.sleep(3)

        HelperTestBase.reliableClick(self, "[data-test-id='shoppingListProduct_1']")
        HelperTestBase.reliableClick(self, "[data-test-id='BiziPix']")
        time.sleep(3)
        ProductDetailsPage.clickCloseButton(self)
        time.sleep(2)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)
