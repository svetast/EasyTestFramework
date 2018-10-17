import time

from selenium.webdriver.common.keys import Keys

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage


class TestLogIn(LoginPage):
    # Valid user credentials - svetast / Ss1234567


    ####### Test scope - input a valid login "svetast" and valid password "Ss1234567", click on the 'Log In' button => Home page is opened:

    # @pytest.mark.skip
    def test_loginLogOutSuccess(self):
        url1 = self.base_url + '/shopping-list'
        url = self.base_url + '/login'
        url2 = self.base_url + '/settings'
        text = 'Logout:'
        text1 = 'Do you want to logout?'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(4)
        HelperTestBase.logOutAction(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickCancelButton(self)
        HelperTestBase.clicklogOutButton(self)
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='username']"), True)

    # Test scope - the fields are empty => the 'Login' button isn't active:
    # @pytest.mark.skip

    def test_loginUnSuccess1(self):
        url = self.base_url + '/login'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionEmptyFields(self, '', '')
        self.assertEqual(url, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='loginBtn']"), False)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='username']"), True)


        # Test scope - input an invalid login "Svetast", valid password. Press the "Login" button =>
        # The "User Svetast doesn't exist" message is displayed under the "Login" field:

    #@pytest.mark.skip
    def test_loginUnSuccess2(self):
        url = self.base_url + '/login'
        text = 'Unable to login:'
        text1 = "User Svetast doesn't exist"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionInvalidData(self, 'Svetast', 'Ss1234567')
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='loginBtn']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='username']"), True)



        # Test scope - Input an unregistered login "CD" and password. Press the "Login" button.	The "User CD doesn't exist" message is displayed under the "Login" field,
        #  the'username' field has focus:

        # @pytest.mark.skip

    #@pytest.mark.skip
    def test_loginUnSuccess3(self):
        url = self.base_url + '/login'
        text = "Unable to login:"
        text1 = "User CD doesn't exist"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionInvalidData(self, 'CD', 'Ss1234567')
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        # check - 'username' field is enabled:
        self.assertIs(True, LoginPage.checkUsername_IsEnabled(self))
        # check - 'username' field has focus:

    def is_element_focus(self):
        self.driver.find_element_by_name("username") == self.driver.switch_to.active_element

        #

        # Test scope - Input a valid login "svetast" and invalid password "Ss" . Press the "Login" button => The "Incorrect password" message is displayed under the "Login" field,
        # the'password' field has focus:
        # @pytest.mark.skip

    #@pytest.mark.skip
    def test_loginUnSuccess4(self):
        url = self.base_url + '/login'
        text = "Unable to login:"
        text1 = "Incorrect password"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionInvalidData(self, 'svetast', 'Ss')
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        # check - 'password' field is enabled:
        self.assertIs(True, LoginPage.checkPassword_IsEnabled(self))
        # check - 'password' field has focus:

    def is_element_focus1(self):
        return self.driver.find_element_by_name("password") == self.driver.switch_to.active_element

        # Update the page if "Keep me loged" wasn't selected =>	The Log In page is opened:

        # @pytest.mark.skip
    def test_chekUpdatePageUnSelectedKeepMeLogged(self):
        url = self.base_url + '/shopping-list'
        url1 = self.base_url + '/login'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionWithoutKeepMeLogged(self, 'SA1', 'Bizibaza111')

        self.assertEqual(url, HelperTestBase.getURL(self))
        driver.refresh()
        self.assertEqual(url1, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='username']"), True)



        # Update the page if "Keep me loged" was selected =>	The page updated. User stay logged in, 'Log Out' button os displayed:

    #@pytest.mark.skip
    def test_chekUpdatePageSelectedMeLogged(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', 'Bizibaza111')
        time.sleep(5)

        self.assertEqual(url, HelperTestBase.getURL(self))
        driver.refresh()
        HelperTestBase.waitSettingsButton(self)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='settingsLink']"), True)
        self.assertEqual(url, HelperTestBase.getURL(self))

    #@pytest.mark.skip
    def test_unchekedKeepMeLoggedBrowser(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginActionWithoutKeepMeLogged(self, 'svetast', 'Ss1234567')
        time.sleep(5)
        self.assertEqual(url, HelperTestBase.getURL(self))
        time.sleep(5)
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')
        driver.get(self.base_url)
        time.sleep(5)
        self.assertIs(HelperTestBase.checkElementEnabled(self, "[data-test-id='username']"), True)

        # @pytest.mark.skip
    def test_chekedKeepMeLoggedBrowser(self):
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(5)
        self.assertEqual(url, HelperTestBase.getURL(self))
        time.sleep(5)
        body = self.driver.find_element_by_tag_name("body")
        body.send_keys(Keys.CONTROL + 't')
        driver.get(self.base_url)
        time.sleep(5)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # Test scope: click on 'Show password' => Password is displayed:

        # @pytest.mark.skip
    def test_checkShowPassword(self):
        text = 'Ss1234567'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginShowPassword(self, 'svetast', 'Ss1234567')
        # time.sleep(2)
        self.assertEqual(text, self.driver.find_element_by_name('password').get_attribute('ng-reflect-model'))
