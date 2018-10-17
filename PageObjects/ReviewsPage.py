import time

from HelperTestBase import HelperTestBase
from PageObjects.AnalyticsPage import AnalyticsPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProductDetailsPage import ProductDetailsPage


class ReviewsPage(ProductDetailsPage):
    def ReviewsPage(self):
        driver = self.driver
        driver.get(self.base_url)

    # #### Click on Filter on 'Add Reviews' page:
    def clickFilter(self):
        self.driver.find_element_by_css_selector("[data-test-id='showFilter']").click()
        time.sleep(3)

    def checkFilterPresent(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='showFilter']").is_displayed()
        return state

    ### Click on Filter on 'Add Reviews' page:
    def clickBackButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='backLink']")
        time.sleep(3)

    ### Select reviews:


    # Click on Add Review
    def clickAddReviewButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='addReview']")
        time.sleep(6)








    #### The elements on 'Add a review' page:

    # def checkSavePresent(self):
    #     state = self.driver.find_element_by_css_selector(
    #         'body > app-root > div > div > reviews > div > div > form > input').is_displayed()
    #     return state




    def checkSavePresent(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='saveReview']").is_displayed()
        return state

    # def checkStarsPresent(self):
    #     state = self.driver.find_element_by_css_selector(
    #         'body > app-root > div > div > reviews > div > div > form > input').is_displayed()
    #     return state
    #

    def checkStarsPresent(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='reviewStars']").is_displayed()
        return state

    # def checkYourReviewPresent(self):
    #     state = self.driver.find_element_by_css_selector(
    #         "body > app-root > div > div > reviews > div > div > form > textarea").is_displayed()
    #     return state
    #

    def checkYourReviewPresent(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='reviewInputCom']").is_displayed()
        return state

    # def setReviewText(self):
    #     self.driver.find_element_by_css_selector(
    #         'body > app-root > div > div > reviews > div > div > form > textarea').send_keys('Test Review')

    def setReviewText(self):
        self.driver.find_element_by_css_selector("[data-test-id='reviewInputCom']").send_keys('Test Review')






    def clickSaveButton(self):
        self.driver.find_element_by_css_selector("[data-test-id='saveReview']").click()
        time.sleep(2)

    # def addStars(self):
    #     self.driver.find_element_by_css_selector(
    #         'body > app-root > div > div > reviews > div > div > form > input').send_keys('5')

    def addStars(self):
        HelperTestBase.setStars(self)
        # self.driver.find_element_by_css_selector("[data-test-id='reviewStars']").send_keys('5')

    ##### Check 'Add a review' text on header: ######

    def checkElemPresent(self):
        elem = HelperTestBase.checkElementPresent(self,
                                                  "body > app-root > div > div > reviews > div > reviews-header > header > button")
        return elem



    def addReviewSuccess(self):
        self.setReviewText()
        self.addStars()
        self.clickSaveButton()
        time.sleep(3)


    def goToAddReviewPage(self):
        NavigationMenuPage.clickAnalytics(self)
        AnalyticsPage.clickHistoryButton(self)
        AnalyticsPage.clickHistoryBuyer(self)
        AnalyticsPage.openProductWitchBought(self)
        ProductDetailsPage.clickReviewsButton(self)



    def addReviewOnBuyer(self):
        NavigationMenuPage.clickAnalytics(self)
        AnalyticsPage.clickHistoryButton(self)
        AnalyticsPage.clickHistoryBuyer(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='review_0']")
        self.addReviewSuccess()

    def setStars(self):
        HelperTestBase.setStars(self)
        # elf.driver.find_element_by_css_selector("reviewStars").send_keys(stars)

    def setTextReview(self):
        self.driver.find_element_by_css_selector("reviewStars").send_keys("5")
        self.driver.find_element_by_css_selector("reviewInputCom").send_keys("Review about svetast")
        self.driver.find_element_by_css_selector("saveReview").click()




        # self.driver.find_element_by_css_selector("reviewStars").send_keys(stars)

    def clickBackFromAddReviewPage(self):
        NavigationMenuPage.clickAnalytics(self)
        AnalyticsPage.clickHistoryButton(self)
        AnalyticsPage.clickHistoryBuyer(self)
        HelperTestBase.reliableClick(self, "[data-test-id='review_0']")
        self.clickBackButton()
        time.sleep(5)
