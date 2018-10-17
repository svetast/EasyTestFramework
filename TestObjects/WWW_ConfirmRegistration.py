import time

from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase
from PageObjects.RegistrationPage import RegistrationPage


class Test_WWW_ConfirmRegistrationSuccess(RegistrationPage):
    # @pytest.mark.skip
    def test_WWW_ConfirmRegistrationGmail(self):
        text1 = 'Success!'
        text2 = 'User successfully verified!'
        driver = self.driver
        driver.maximize_window()
        driver.get('https://accounts.google.com/signin')
        time.sleep(5)
        self.driver.find_element_by_id("identifierId").send_keys('svetatestbox@gmail.com')
        self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)

        time.sleep(5)
        self.driver.find_element_by_name('password').send_keys('ss@1234567')
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get('https://mail.google.com/mail/u/0/#inbox')
        time.sleep(9)
        self.driver.find_elements_by_xpath("//span/b[contains(text(), 'Account verification')]")[0].click()
        time.sleep(3)
        self.driver.find_element_by_partial_link_text("http://bizibaza.com/api/v1/verification?signup_token=").click()
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])
        self.assertEqual(text1, HelperTestBase.getTitle(self))
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)

    # @pytest.mark.skip
    def test_WWW_ReConfirmRegistrationGmail(self):
        title = 'BiziBAZA™ APP'
        driver = self.driver
        driver.maximize_window()
        driver.get('https://accounts.google.com/signin')
        time.sleep(5)
        self.driver.find_element_by_id("identifierId").send_keys('svetatestbox@gmail.com')
        self.driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)

        time.sleep(5)
        self.driver.find_element_by_name('password').send_keys('ss@1234567')
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get('https://mail.google.com/mail/u/0/#inbox')
        time.sleep(9)
        self.driver.find_elements_by_xpath("//span[contains(text(), 'Account verification')]")[0].click()
        time.sleep(3)
        self.driver.find_element_by_partial_link_text(
            "http://bizibaza.com/api/v1/verification?signup_token=").click()
        time.sleep(5)
        driver.switch_to_window(driver.window_handles[1])
        self.assertEqual(title, HelperTestBase.getTitle(self))
