import time

from strgen import StringGenerator

from HelperTestBase import HelperTestBase
from PageObjects.RegistrationPage import RegistrationPage


class TestRegistrationSuccess(RegistrationPage):
    ####### There are positive tests!!!!  ######

    # Test scope - click on the 'Sign up' button on the 'LogIn' form  => 1.The 'Sign up' page is opened,  < Log In' link is displayed.
    # click on the 'Log In' link on the 'SignUp' form  => LogIn page is opened, Login button is present:

    # @pytest.mark.skip
    def test_RegistrationStartClose(self):
        text1 = 'Welcome! Please select account type.'
        url1 = self.base_url + '/login'
        url2 = self.base_url + '/signup'
        driver = self.driver
        driver.get(self.base_url)
        HelperTestBase.clickAndWait(self, "[data-test-id='signupBtn']")
        self.assertIn(text1, driver.page_source)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='loginLink']"), True)
        HelperTestBase.clickAndWait(self, "[data-test-id='loginLink']")
        time.sleep(5)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='loginBtn']"), True)

    # @pytest.mark.skip
    def test_setupPayPal_Acc(self):
        url = self.base_url + '/signup'
        title = 'Sign Up for PayPal: Create a Business or Personal Account Now With PayPal'
        url1 = 'https://www.paypal.com/cgi-bin/webscr?cmd=_account#/intent_email_password'
        driver = self.driver
        driver.get(self.base_url)
        HelperTestBase.clickAndWait(self, "[data-test-id='signupBtn']")
        self.assertEqual(url, HelperTestBase.getURL(self))
        HelperTestBase.clickAndWait(self, "[data-test-id='ppLink']")
        time.sleep(3)
        # self.assertEqual(url1, HelperTestBase.getURL(self))
        self.assertEqual(title, HelperTestBase.getTitle(self))

    # Test scope - input a valid data into Registration form and click on the 'Sign up' button => 'Success! You have almost finished.' is displayed:
    # After that - Click on 'log in' link on  "After you finish, come back and log in" of the 'success screen' =>	The Log In page is displayed
    # @pytest.mark.skip
    def test_RegistrationBuyerSuccess(self):
        url = self.base_url + '/signup'
        url2 = self.base_url + '/login'
        text1 = 'Success!'
        text2 = 'Please, check your email and follow the verification link to complete you registration.'
        text3 = 'After you finish, come back and'

        # Get random string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()

        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        z = StringGenerator('[\d]{5}').render()
        firstName = 'Sveta' + x
        lastName = 'Test' + x
        login = 'Test' + x
        login2 = login
        password = 'Ss123456'
        password2 = 'Ss123456'
        email = 'svetatestbox' + "+" + x + '@gmail.com'
        # email = 'svetatestbox+1968@gmail.com'
        phone = '+380' + y
        address = "New Street 567"
        address2 = address
        city = 'Avilon'
        state = '22'
        code = '8765'
        country = '199'
        ppFirstName = 'Sveta'
        ppLastName = 'Stepanova'
        ppEmail = 'stepanova@dnt-lab.com'

        driver = self.driver
        driver.get(self.base_url)
        HelperTestBase.click(self, "[data-test-id='signupBtn']")
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        time.sleep(5)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        HelperTestBase.click(self, "[data-test-id='loginLink2']")
        HelperTestBase.wait(self, "[data-test-id='loginBtn']")
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # # Test scope - input a valid data into Registration form and click on the 'Sign up' button => 'Success! You have almost finished.' is displayed:
        # After that - Click on 'log in' link on  "After you finish, come back and log in" of the 'success screen' =>	The Log In page is displayed
        # @pytest.mark.skip

    def test_RegistrationSellerSuccess(self):
        url = self.base_url + '/signup'
        url2 = self.base_url + '/login'
        text1 = 'Success!'
        text2 = 'Please, check your email and follow the verification link to complete you registration.'
        text3 = 'After you finish, come back and'

        # Get random string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{3}').render()

        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        z = StringGenerator('[\d]{5}').render()

        firstName = 'Sveta' + x
        lastName = 'Test' + x
        login = 'SellerTest' + x
        login2 = login
        password = 'Ss123456'
        password2 = 'Ss123456'
        email = 'svetatestbox' + "+" + z + '@gmail.com'
        phone = '+380' + y
        address = "New Street 567"
        address2 = address
        city = 'Boston'
        state = '22'
        code = '8765'
        country = '199'
        ppFirstName = 'Sveta'
        ppLastName = 'Stepanova'
        ppEmail = 'stepanovasveta.ua@gmail.com'

        driver = self.driver
        driver.get(self.base_url)
        HelperTestBase.clickAndWait(self, "[data-test-id='signupBtn']")
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.switchShopperSeller(self)
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        time.sleep(7)
        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)
        HelperTestBase.wait(self, "[data-test-id='loginLink2']")
        HelperTestBase.click(self, "[data-test-id='loginLink2']")
        HelperTestBase.wait(self, "[data-test-id='loginBtn']")
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # Test scope - input a valid data (firstName, lastName, login, login2 have min 2 letters) into Registration form and click on the 'Sign up' button => 'Success! You have almost finished.' is displayed:
        # After that - Click on 'log in' link on  "After you finish, come back and log in" of the 'success screen' =>	The Log In page is displayed

    # @pytest.mark.skip
    def test_RegistrationBuyerMinimum_2_Letters(self):
        url = self.base_url + '/signup'
        url2 = self.base_url + '/login'
        text1 = 'Success!'
        text2 = 'Please, check your email and follow the verification link to complete you registration.'
        text3 = 'After you finish, come back and'

        # Get random string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{2}').render()

        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        z = StringGenerator('[\d]{5}').render()
        firstName = x
        lastName = x
        login = x
        login2 = x
        password = 'Ss123456'
        password2 = 'Ss123456'
        email = 'vasilissa' + "+" + z + '@ukr.net'
        # email = 'stepanova' + "+" + z + '@dnt-lab.com'
        phone = '+380' + y
        address = "New Street 567"
        address2 = address
        city = 'Avilon'
        state = '22'
        code = '8765'
        country = '199'
        ppFirstName = 'Sveta'
        ppLastName = 'Stepanova'
        ppEmail = 'stepanova@dnt-lab.com'

        driver = self.driver
        driver.get(self.base_url)
        HelperTestBase.click(self, "[data-test-id='signupBtn']")
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertIn(text1, self.driver.page_source)
        self.assertIn(text2, self.driver.page_source)
        self.assertIn(text3, self.driver.page_source)

        HelperTestBase.click(self, "[data-test-id='loginLink2']")
        HelperTestBase.wait(self, "[data-test-id='loginBtn']")
        self.assertEqual(url2, HelperTestBase.getURL(self))
