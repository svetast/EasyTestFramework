import time

from HelperTestBase import HelperTestBase


class LoginPage(HelperTestBase):
    def LoginPage(self):
        driver = self.driver
        driver.get(self.base_url)  ### Login action:

    def loginAction(self, username, password):
        self.driver.find_element_by_css_selector("[data-test-id='username']").send_keys(username)
        self.driver.find_element_by_css_selector("[data-test-id='password']").send_keys(password)
        HelperTestBase.reliableClick(self, "[data-test-id='passInvisible']")
        self.driver.find_element_by_css_selector("[data-test-id='keepLogged']").click()
        self.driver.find_element_by_css_selector("[data-test-id='loginBtn']").click()
        time.sleep(6)

    def loginActionInvalidData(self, username, password):
        self.driver.find_element_by_css_selector("[data-test-id='username']").send_keys(username)
        self.driver.find_element_by_css_selector("[data-test-id='password']").send_keys(password)
        HelperTestBase.reliableClick(self, "[data-test-id='passInvisible']")
        self.driver.find_element_by_css_selector("[data-test-id='loginBtn']").click()

    def loginActionEmptyFields(self, username, password):
        self.driver.find_element_by_css_selector("[data-test-id='username']").send_keys(username)
        self.driver.find_element_by_css_selector("[data-test-id='password']").send_keys(password)
        HelperTestBase.reliableClick(self, "[data-test-id='passInvisible']")

    ###### login action wthout  'Keep me logged' checkbox:

    def loginActionWithoutKeepMeLogged(self, username, password):
        self.driver.find_element_by_css_selector("[data-test-id='username']").send_keys(username)
        self.driver.find_element_by_css_selector("[data-test-id='password']").send_keys(password)
        HelperTestBase.reliableClick(self, "[data-test-id='passInvisible']")
        self.driver.find_element_by_css_selector("[data-test-id='loginBtn']").click()
        # HelperTestBase.waitElement(self, "[data-test-id='settingsLink']")
        time.sleep(3)


    def loginShowPassword(self, username, password):
        self.driver.find_element_by_css_selector("[data-test-id='username']").send_keys(username)
        self.driver.find_element_by_css_selector("[data-test-id='password']").send_keys(password)
        self.driver.find_element_by_css_selector("[data-test-id='keepLogged']").click()
        HelperTestBase.reliableClick(self, "[data-test-id='passInvisible']")

    ###### Start 'Sign In' action:

    def clickSignUpButton(self):
        self.driver.find_element_by_css_selector("[data-test-id='signupBtn']").click()

    ###### Start 'Forgot password?' action:

    def clickForgotPasswordButton(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='forgotBtn']")
        time.sleep(2)






    # check - is 'Login' button enabled?
    def checkLoginButton_IsEnabled(self):
        state = self.driver.find_element_by_css_selector("[data-test-id='loginBtn']").is_enabled()
        return state

    # check - is 'username' field enabled?
    def checkUsername_IsEnabled(self):
       state = (self.driver.find_element_by_name("username")).is_enabled()
       return state

    # check - is 'Password' field enabled?
    def checkPassword_IsEnabled(self):
        state = (self.driver.find_element_by_name("password")).is_enabled()
        return state

    def clickReSendVerification(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='resendBtn']")
        time.sleep(2)
