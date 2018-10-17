from strgen import StringGenerator

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import RegistrationPage


class TestRegistrationEmpty_InvalidFields(RegistrationPage):


    # Test scope - there are empty all fields, click the "Sign up" button => The appropriate error message is displayed
    # @pytest.mark.skip
    def test_registrationEmptyFields(self):
        pageTitle = 'BiziBAZA'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        RegistrationPage.registrationEmptyFields(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))

    # test data: !@#$%^&*(){}
    # @pytest.mark.skip
    def test_registrationInvalidFields(self):
        pageTitle = 'BiziBAZA'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        y = StringGenerator('[\d]{9}').render()
        firstName = '!@#$%^&*(){}'
        lastName = '!@#$%^&*(){}'
        login = '!@#$%^&*(){}'
        login2 = login
        password = '!@#$%^&*(){}'
        password2 = '!@#$%^&*(){}'
        ppEmail = '!@#$%^&*(){}@gmail.com'
        ppFirstName = '!@#$%^&*(){}'
        ppLastName = '!@#$%^&*(){}'
        phone = '+380' + y
        address = "!@#$%^&*(){}"
        address2 = "!@#$%^&*(){}"
        city = '!@#$%^&*(){}'
        state = '15'
        code = '8765'
        email = '!@#$%^&*(){}@example.com'
        country = '11'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))

    # test data: '      curubo'
    #@pytest.mark.skip
    def test_registrationInvalidFields2(self):
        pageTitle = 'BiziBAZA'
        text1 = 'Error:'
        text2 = 'Please, check all the fields for completeness or typos.'
        # Get random letters string ( \c: lowercase,  \l: - letters, {5} - number of leters)
        x = StringGenerator('[\c]{5}').render()
        # Get random numbers string ( \d: digits, {9} - number of leters)
        z = StringGenerator('[\d]{3}').render()
        y = StringGenerator('[\d]{9}').render()
        firstName = '      curubo'
        lastName = '      curubo'
        login = '      curubo'
        login2 = login
        password = 'Ss123456'
        password2 = password
        email = 'stepanova+' + z + '@dnt-lab.com'
        ppEmail = '     curubo@gmail.com'
        ppFirstName = '      curubo'
        ppLastName = '      curubo'
        phone = '+380' + y
        address = '      curubo'
        address2 = address
        city = '      curubo'
        state = '15'
        code = '8765'
        country = '11'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        RegistrationPage.registration(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))


        # Input the valid data into all fielda, dont select 'State' option, click the "Sign up" button = >   The appropriate error message is displayed:

        # @pytest.mark.skip

    def test_registrationWithoutState(self):
        pageTitle = 'BiziBAZA'
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
        password = 'Ss1234567'
        password2 = 'Ss1234567'
        phone = '+380' + y
        address = "Street 1"
        address2 = "apppartment 23"
        city = 'Boston'
        state = '0'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '11'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        ppEmail = 'stepanovasveta.ua@gmail.com'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        RegistrationPage.registrationWitoutState(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))


        # Input the valid data into all fielda, dont select 'Country' option, click the "Sign up" button = >   The appropriate error message is displayed:

    #@pytest.mark.skip
    def test_registrationWithoutCountry(self):
        pageTitle = 'BiziBAZA'
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
        password = 'Ss1234567'
        password2 = 'Ss1234567'
        phone = '+380' + y
        address = "Street 1"
        address2 = "apppartment 23"
        city = 'Boston'
        state = '15'
        code = '8765'
        email = 'test' + x + '@example.com'
        country = '0'
        ppFirstName = 'Svitlana'
        ppLastName = 'Stepanova'
        ppEmail = 'stepanovasveta.ua@gmail.com'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.clickSignUpButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        RegistrationPage.registrationWitoutCountry(self, firstName, lastName, login, login2, password, password2,
                                      ppFirstName, ppLastName, ppEmail, email, phone,
                                      address, address2, city, state, code, country)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        self.assertEqual(pageTitle, RegistrationPage.getTitle(self))
