from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage


class AdvertismentPage(LoginPage):
    def AdvertismentPage(self):
        driver = self.driver
        driver.get(self.base_url)

    ##### Check an advertisement carousel:

    def clickOnImage0(self):
        wait = WebDriverWait(self.driver, 60)
        image = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//img[@src='https://bizibazapics.s3.amazonaws.com/Ads/2644265007210509201713043.jpeg']")))
        image.click()

    def clickOnImage1(self):
        wait = WebDriverWait(self.driver, 60)
        image = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//img[@src='https://bizibazapics.s3.amazonaws.com/Ads/3756540828060405201712318.jpeg']")))
        image.click()

    def clickOnImage2(self):
        wait = WebDriverWait(self.driver, 60)
        image = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//img[@src ='https://bizibazapics.s3.amazonaws.com/Ads/3756540828060405201712318.jpeg']")))
        image.click()
