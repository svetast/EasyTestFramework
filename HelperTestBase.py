import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HelperTestBase(unittest.TestCase):
    # class HelperTestBase: This class use for all tests  'Set Up' method


    def setUp(self):

        ### for using Headless Browser:
        # chrome_options = Options()
        # chrome_options.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # ###############

        ### for using Web Browser :

        self.driver = webdriver.Chrome('chromedriver')
        self.driver.set_window_size(360, 640)
        self.driver.implicitly_wait(100)
        self.base_url = "https://bizibaza.com"

    def waitForPageToLoad(self):
        self.driver.set_page_load_timeout(100)

    def waitElement(self, locator=None):
        element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
        WebDriverWait(self.driver, 100).until(element_present)

    def waitSettingsButton(self):
        element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='settingsLink']"))
        WebDriverWait(self.driver, 100).until(element_present)

    def wait(self, locator=None):
        element_present = EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
        WebDriverWait(self.driver, 120).until(element_present)

    def waitTitle(self, title=None):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.title_is(title))

    def waitElement1(self, locator=None):
        element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
        WebDriverWait(self.driver, 100).until(element_present)


        ##### the universal metod  using on web pages: ##########
        #  click if presence of element located:

    def clickAndWait(self, locator=None):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        element.click()
        time.sleep(2)


    def clickOnElement(self, locator=None):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        element.click()

    def click(self, locator=None):
        self.driver.find_element_by_css_selector(locator).click()
        time.sleep(3)

    def clickBackButton(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='shoppingLink']")))
        element.click()
        time.sleep(3)

    def clickBack(self):
        self.reliableClick("[data-test-id='shoppingLink']")
        time.sleep(1)

    def clickHomeIcon(self):
        self.reliableClick("[data-test-id='backLink']")
        time.sleep(1)





    def clickBackIcon(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='backLink']")))
        element.click()
        time.sleep(2)

    def logOutAction(self):
        self.reliableClick("[data-test-id='settingsLink']")
        self.reliableClick("[data-test-id='logout']")
        time.sleep(3)

    def logOutAllDevices(self):
        self.reliableClick("[data-test-id='settingsLink']")
        self.reliableClick("[data-test-id='logoutFromAll']")
        time.sleep(3)

    def clickSettingsButton(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='settingsLink']")))
        element.click()
        time.sleep(2)

    def clicklogOutButton(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='logout']")))
        element.click()
        time.sleep(2)

        # self.driver.find_element_by_css_selector("[data-test-id='logout']").click()
        # time.sleep(3)

    def closeBiziEditor(self):
        self.driver.find_element_by_css_selector("[data-test-id='closeButton']").click()

    def clickSearch(self):
        self.reliableClick("[data-test-id='searchLink']")
        time.sleep(4)

    def clickOn(self, locator=None):
        self.driver.find_element_by_class_name(locator).click()
        time.sleep(3)

    def clickYesButton(self):
        self.driver.find_element_by_css_selector("[data-test-id='yesButton']").click()
        time.sleep(2)

    def clickCancelButton(self):
        self.driver.find_element_by_css_selector("[data-test-id='noButton']").click()
        time.sleep(3)

    def clickByXPath(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        time.sleep(3)

    # This method set text into input field :
    def setText(self, locator=None, stringtext=None):
        self.driver.find_element_by_css_selector(locator).clear()
        self.driver.find_element_by_css_selector(locator).send_keys(stringtext)
        self.driver.find_element_by_css_selector(locator).send_keys(Keys.ENTER)

    def typeText(self, locator=None, stringtext=None):
        self.driver.find_element_by_css_selector(locator).send_keys(stringtext)
        self.driver.find_element_by_css_selector(locator).send_keys(Keys.ENTER)

    def setStars(self):
        # self.driver.find_element_by_css_selector("reviewStars").send_keys("5")
        self.driver.find_element_by_css_selector("[data-test-id='detailRateStars4']").click()

    def setQuantity(self, locator=None, stringtext=None):
        self.driver.find_element_by_css_selector(locator).clear()
        self.driver.find_element_by_css_selector(locator).send_keys(stringtext)
        self.driver.find_element_by_css_selector(locator).send_keys(Keys.ENTER)

    # This method set text into input field :
    def editText(self, locator=None, stringtext=None):
        element = self.driver.find_element_by_css_selector(locator)
        # element.click()
        element.send_keys(stringtext)
        time.sleep(2)

    def inputText(self, locator=None, description=None):
        self.driver.find_element_by_name(locator).send_keys(description)

    def clearField(self, locator=None, stringItem=None):
        self.driver.find_element_by_css_selector(locator).clear()
        self.driver.find_element_by_css_selector(locator).send_keys(stringItem)

    def clearField1(self, locator=None):
        self.driver.find_element_by_css_selector(locator).clear()

    ########## The universal methods for get text of the modal window     #######

    def getModalHeader(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalHeader']").text
        return text

    def getModalMessage(self):
        text = self.driver.find_element_by_css_selector("[data-test-id='modalMessage']").text
        return text

    # checking - is a web element present on NavMenu? ( Cart, Profile, Watchlist etc.):

    def checkElementEnabled(self, locator=None):
        state = self.driver.find_element_by_css_selector(locator).is_enabled()
        return state

    def checkElementExist(self, locator=None):
        state = self.driver.find_elements_by_css_selector(locator)
        return state


    def checkElementPresent(self, locator=None):
        state = self.driver.find_element_by_css_selector(locator).is_displayed()
        return state

    def checkElement(self, locator=None):
        state = self.driver.find_element_by_name(locator).is_displayed()
        return state

    def checkElement1(self, locator=None):
        state = self.driver.find_element_by_class_name(locator).is_displayed()
        return state

    def checkPasswordFieldEnabled(self, locator=None):
        state = self.driver.find_element_by_id(locator).is_enabled()
        return state

    def getText(self, locator=None):
        text = self.driver.find_element_by_css_selector(locator).text
        return text

    def getText1(self, locator=None):
        text = self.driver.find_element_by_class_name(locator).text
        return text

    # the method returns the current title of the web page (use for 'asserts'):
    def getTitle(self):
        currentTitle = self.driver.title
        return currentTitle

    def getURL(self):
        currentURL = self.driver.current_url
        return currentURL

    def checkContainsURL(self):
        currentURL = __contains__('https://www.paypal.com')
        return currentURL

    def reliableClick(self, element):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def waitURL(self, url):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.url_to_be(url))







        ######## delete after   #########

    def clickBackButton111(self):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                               "body > app-root > div > div > watch-list > div > watch-list-header > header > nav > div.navbar__left > a")))
        element.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





############# Don't REMOVE !!!!!!!!!!!!!!!!!    #####################





# Set the mobile device:


# # Select which device you want to emulate by uncommenting it:
# mobile_emulation = {"deviceName": "Nexus 5"}
#
# # Define a variable to hold all the configurations we want:
# chrome_options = webdriver.ChromeOptions()
#
# # Add the mobile emulation to the chrome options variable:
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#
# # Create driver, pass it the path to the chromedriver file and the special configurations you want to run:
# self.driver = webdriver.Chrome(
#     executable_path='chromedriver', chrome_options=chrome_options)


##### or set device:


# mobile_emulation = {
#     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
#     "userAgent": "Mozilla/5.0 (Linux; Android 7.0; PRA-LA1 Build/HUAWEIPRA-LA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"}
# chrome_options = Options()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# self.driver = webdriver.Chrome(chrome_options=chrome_options)





##### the universal metod  using on web pages: ##########
