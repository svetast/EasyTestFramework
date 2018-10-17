import time

from HelperTestBase import HelperTestBase
from PageObjects.AnalyticsPage import AnalyticsPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage
from PageObjects.ReviewsPage import ReviewsPage


class TestReviews(ReviewsPage):
    # ### click on Reviews button on Product Details page => Add Review page is opened:
    # @pytest.mark.skip
    def test_clickReviewsOnProductDetails(self):
        url = self.base_url + '/shopping-list'
        url2 = 'reviews-item'
        text1 = 'Add Review'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Ss', 'Ss1234567')

        ProductDetailsPage.goToProductDetailsPage(self)
        ProductDetailsPage.clickReviewsButton(self)
        self.assertIn(text1, self.driver.page_source)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='backLink']"), True)
        self.assertIs(ReviewsPage.checkFilterPresent(self), True)

        ### click on Fiter button  => The filters dropdown are opened:

        ReviewsPage.clickFilter(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='0']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='1']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='2']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='3']"), True)

        ### "Click on: -Positive reviews, -All reviews, -Negative reviews, -Neutral reviews => 	Appropriate reviews are displayed
        # ReviewsPage.selectReviews(self)


        ### Click on Filter button	=> The filters are closed:
        ReviewsPage.clickFilter(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='0']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='1']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='2']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='3']"), False)

        ### Click on "<" button =>	Previous page is opened:
        # ReviewsPage.clickBackButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")

        # #### Test scope - check  'Reviews' on Nav Menu for Buyer:

        # 2. Check the elements on ReviewsPage and redirect back to Shopping list:

    # @pytest.mark.skip
    def test_checkElementsOnReviewsPage(self):
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/reviews'
            driver = self.driver
            driver.get(self.base_url)
            text1 = 'Positive reviews'
            text2 = 'All reviews'
            text3 = 'Neutral reviews'
            text4 = 'Negative reviews'
            LoginPage.loginAction(self, 'SellerTesttxw', 'Ss123456')

            ###Test scope - Buyer clicks on Reviews button on Nav Menu => Add Review page is opened:
            NavigationMenuPage.clickReviews(self)
            self.assertEqual(url2, HelperTestBase.getURL(self))
            # Check - the Back button, Filter button elements are present:
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='backLink']"), True)
            self.assertIs(ReviewsPage.checkFilterPresent(self), True)

            ### Test scope - click on Fiter button  => The filter dropdown is opened:

            ReviewsPage.clickFilter(self)
            ### Test scope - check  the options Positive reviews, All reviews, Negative reviews, Neutral reviews are present:
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='0']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='1']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='2']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='3']"), True)

            self.assertIn(text1, self.driver.page_source)
            self.assertIn(text2, self.driver.page_source)
            self.assertIn(text3, self.driver.page_source)
            self.assertIn(text4, self.driver.page_source)

            ### Click on Filter button	=> The filter dropdown is closed:
            ReviewsPage.clickFilter(self)
            ### Test scope - check  the options Positive reviews, All reviews, Negative reviews, Neutral reviews aren't present:
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='0']"), False)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='1']"), False)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='2']"), False)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='3']"), False)

            ### Click on "<" button =>	ShoppingList page is opened:
            # ReviewsPage.clickBackButton(self)
            HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
            self.assertEqual(url, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_addReviews_If_BuyerNotBoughtProduct(self):
            ### Click on "Add Review" on Reviews page if Buyer hasn't bought product => 'You haven't bought this item yet' is displayed:
            url = self.base_url + '/shopping-list'
            url2 = self.base_url + '/reviews'
            driver = self.driver
            driver.get(self.base_url)
            text1 = 'You cannot send review:'
            text2 = "You haven't bought this item yet"
            LoginPage.loginAction(self, 'Testkaeda', 'Ss123456')

            ProductDetailsPage.goToProductDetailsPage(self)
            ProductDetailsPage.clickReviewsButton(self)
            ReviewsPage.clickAddReviewButton(self)
            self.assertEqual(text1, HelperTestBase.getModalHeader(self))
            self.assertEqual(text2, HelperTestBase.getModalMessage(self))
            HelperTestBase.clickYesButton(self)
            ### Click on "Back" button => Product details page is opened, 'BuyNow' button is displayed:
            # ReviewsPage.clickBackButton(self)
            HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailAddToCart']"), True)
            self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='detailBuyNow']"), True)

    #@pytest.mark.skip
    def test_checkSeller_AddReviewAboutBuyer(self):
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/reviews'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'You cannot send review:'
        text2 = "You haven't bought this item yet"
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')

        time.sleep(3)
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(9)
        ReviewsPage.addReviewOnBuyer(self)



        # # Go to 'Add Review' page from Product Details:
        # ReviewsPage.goToAddReviewPage(self)
        # ReviewsPage.clickBackButton(self)
        # ProductDetailsPage.clickReviewsButton(self)
        # ReviewsPage.clickAddReviewButton(self)
        # self.assertIs(ReviewsPage.checkStarsPresent(self), True)
        # self.assertIs(ReviewsPage.checkYourReviewPresent(self), True)
        # ReviewsPage.addReviewSuccess(self)

    # @pytest.mark.skip

    def test_clickBackFromAddReviewPage(self):
        # Test scope - Seller goes to AddReview Page, click on <, click on < = > Inventory Page is opened
        url = self.base_url + '/shopping-list'
        url2 = self.base_url + '/reviews'
        url1 = self.base_url + '/inventory-list'
        driver = self.driver
        driver.get(self.base_url)
        text1 = 'You cannot send review:'
        text2 = "You haven't bought this item yet"
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        NavigationMenuPage.clickSellerButton(self)
        time.sleep(5)
        ReviewsPage.clickBackFromAddReviewPage(self)
        time.sleep(3)
        AnalyticsPage.clickBackFromHistoryAndDuties(self)
        # AnalyticsPage.clickBackButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        HelperTestBase.waitURL(self, url1)
        self.assertEqual(url1, HelperTestBase.getURL(self))

    # @pytest.mark.skip
    def test_Reviews_positive_filter(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', "Bizibaza111")

        NavigationMenuPage.clickSellerButton(self)
        # HelperTestBase.reliableClick(self, "[data-test-id='sellerBtn']")
        HelperTestBase.reliableClick(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.reliableClick(self, "[data-test-id='reviews']")

        positive_reviews = driver.find_elements_by_css_selector("[attr.data-test-id='like-review_0']")

        HelperTestBase.reliableClick(self, "[data-test-id='showFilter']")
        HelperTestBase.reliableClick(self, "[data-test-id='0']")
        time.sleep(3)

        reviews = self.driver.find_elements_by_class_name("review-list__item")
        self.assertEqual(len(positive_reviews), len(reviews))

    #@pytest.mark.skip
    def test_Reviews_negative_filter(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', "Bizibaza111")

        HelperTestBase.reliableClick(self, "[data-test-id='sellerBtn']")
        HelperTestBase.reliableClick(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.reliableClick(self, "[data-test-id='reviews']")

        negative_reviews = driver.find_elements_by_css_selector("[attr.data-test-id='dislike-review_0']")

        HelperTestBase.reliableClick(self, "[data-test-id='showFilter']")
        HelperTestBase.reliableClick(self, "[data-test-id='3']")
        time.sleep(3)

        reviews = self.driver.find_elements_by_class_name("review-list__item")
        self.assertEqual(len(negative_reviews), len(reviews))
