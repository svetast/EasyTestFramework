from strgen import StringGenerator

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import RegistrationPage


# Test scope - input an INVALID password in the "Password" field, input a valid data into all fields,
#  click the "Sign up" button => The appropriate error message is displayed
# Requirement: The 'Password' must contains one uppercase letter, one digit and be more than 8 symbols


class TestRegistrationPasswordValidation(RegistrationPage):
    # test data: Ss12345 ( less 8 symbols)
    # @pytest.mark.skip
    def test_registrationUnSuccess1(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'Ss12345'
        password2 = 'Ss12345'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '15'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '11'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))


        # test data: ' '

    #@pytest.mark.skip
    def test_registrationUnSuccess2(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = ''
        password2 = ''
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '20'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '17'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # test data : ss123456
    #@pytest.mark.skip
    def test_registrationUnSuccess3(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'ss123456'
        password2 = 'ss123456'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '12'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '10'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

     # test data : SS123456

    #@pytest.mark.skip

    def test_registrationUnSuccess4(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'SS123456'
        password2 = 'SS123456'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '14'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '18'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

     # test data : Testerss

    #@pytest.mark.skip

    def test_registrationUnSuccess5(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'Testerss'
        password2 = 'Testerss'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '16'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '11'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))

        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # test data : 12345678
        # @pytest.mark.skip

    def test_registrationUnSuccess6(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = '12345678'
        password2 = '12345678'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '12'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '10'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

    # test data :  !@#$%^&*
    #@pytest.mark.skip
    def test_registrationUnSuccess7(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = '!@#$%^&*'
        password2 = '!@#$%^&*'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '10'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '11'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # test data : different valid passwords

    #@pytest.mark.skip
    def test_registrationUnSuccess8(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'Ss123456'
        password2 = 'Ff123456'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '15'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '11'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))

        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # test data : different INvalid passwords

    #@pytest.mark.skip

    def test_registrationUnSuccess9(self):
        url = self.base_url + '/signup'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = 'sveta' + x
        lastName = 'test' + x
        login = 'new' + x
        login2 = login
        password = 'Ss123'
        password2 = 'Fg123'
        ppEmail = x + '@gmail.com'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        phone = '+380' + y
        address = "Nauky Street"
        address2 = "Street"
        city = 'Kharkov'
        state = '5'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '18'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)

        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))