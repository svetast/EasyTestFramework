import time

from HelperTestBase import HelperTestBase
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ProfilePage import ProfilePage


class TestProfile(NavigationMenuPage):
    # Test scope - check elements on Profile page:

    # @pytest.mark.skip
    def test_checkElements(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        time.sleep(2)

        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='uploadBtn']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='title']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='title']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profileAddress1']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='newAddress']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profileAddressEdit']"), True)





        # Test scope : 1.click on AddNewAdress on  Profile page => Shipping address is opened
        # 2. Click on Done = > error messagre is dispplayed, click on OK button => error message closed
        # 3. Click on Cancel button => Profile page is opened

    # @pytest.mark.skip
    def test_clickAddNewAddressDoneCancel(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        url3 = self.base_url + '/addr-editor'
        text1 = 'Error!'
        text2 = 'Please check all the fields for completeness or typos.'

        driver = self.driver
        driver.get(self.base_url)

        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(3)

        NavigationMenuPage.clickProfile(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # time.sleep(2)
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        HelperTestBase.clickAndWait(self, "[data-test-id='newAddress']")
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='firstNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='lastNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address1Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address2Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cityInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='stateSelect']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='codeInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='phoneInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='countrySelect']"), True)
        # self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='makePrimary']"), True)
        ProfilePage.clickDoneAddress(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        ProfilePage.clickCancelAddress(self)
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # Test scope : 1.click on AddNewAdress on  Profile page => Shipping address is opened
        # 2. Click on Done = > error messagre is dispplayed, click on OK button => error message closed
        # 3. Click on Cancel button => Profile page is opened

    # @pytest.mark.skip
    def test_clickAddressDoneCancel(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        url3 = self.base_url + '/addr-editor'
        text = 'Error!'
        text1 = 'Please check all the fields for completeness or typos.'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')

        NavigationMenuPage.clickProfile(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        # self.assertEqual(url2, HelperTestBase.getURL(self))

        HelperTestBase.clickAndWait(self, "[data-test-id='profileAddress1']")

        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='firstNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='lastNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address1Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address2Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cityInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='stateSelect']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='codeInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='phoneInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='countrySelect']"), True)
        # self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='makePrimary']"), True)
        ProfilePage.clickDoneAddress(self)
        # self.assertEqual(text, HelperTestBase.getModalHeader(self))
        # self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        # HelperTestBase.clickYesButton(self)
        #
        # ProfilePage.clickCancelAddress(self)
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        # HelperTestBase.clickAndWait(self, "[data-test-id='profileAddressEdit']")
        HelperTestBase.clickAndWait(self, "[data-test-id='newAddress']")

        time.sleep(2)
        self.assertEqual(url3, HelperTestBase.getURL(self))
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='firstNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='lastNameInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address1Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='address2Inp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='cityInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='stateSelect']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='codeInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='phoneInp']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='countrySelect']"), True)
        # self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='makePrimary']"), True)
        ProfilePage.clickDoneAddress(self)
        self.assertEqual(text, HelperTestBase.getModalHeader(self))
        self.assertEqual(text1, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        ProfilePage.clickCancelAddress(self)
        time.sleep(9)
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # Test scope - click on < on  Profile page => Shopping list is displayed:

        # @pytest.mark.skip

    def test_clickBackButton(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(3)

        # NavigationMenuPage.clickProfile(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        time.sleep(2)

        self.assertEqual(url2, HelperTestBase.getURL(self))
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # Test scope - user can edit data in Webpage field:

        # @pytest.mark.skip

    def test_editWebFieldValidData(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'www.alf.kh.pp'
        text1 = 'www.alf.kh.ua'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        time.sleep(3)

        # NavigationMenuPage.clickProfile(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        time.sleep(2)

        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertEqual(text, ProfilePage.getWebString(self))
        ProfilePage.editWebField(self, 'www.alf.kh.ua')
        time.sleep(5)
        self.assertEqual(text1, ProfilePage.getWebString(self))

        #### return the test data to start state:
        ProfilePage.editWebField(self, 'www.alf.kh.pp')
        time.sleep(5)
        self.assertEqual(text, ProfilePage.getWebString(self))

        # Test scope - user can edit data in Email field

    # @pytest.mark.skip
    def test_editEmailFieldValidData(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'stepanova@dnt-lab.com'
        text1 = 'stepanova@gmail.com'

        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(3)

        NavigationMenuPage.clickProfile(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        # self.assertEqual(url2, HelperTestBase.getURL(self))

        self.assertEqual(text, ProfilePage.getEmailString(self))
        ProfilePage.editEmailField(self, 'stepanova@gmail.com')
        time.sleep(5)
        self.assertEqual(text1, ProfilePage.getEmailString(self))

        #### return the test data to start state:
        ProfilePage.editEmailField(self, 'stepanova@dnt-lab.com')
        time.sleep(5)
        self.assertEqual(text, ProfilePage.getEmailString(self))

        # Test scope - check that Web field validates inputted data:
        # @pytest.mark.skip

    def test_editWebFieldInvalidData(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'www.alf.kh.ua'
        text1 = 'Error!'
        text2 = "Input doesn't correspond expected pattern."
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(3)

        NavigationMenuPage.clickProfile(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        #
        # self.assertEqual(url2, HelperTestBase.getURL(self))
        # self.assertEqual(text, ProfilePage.getWebString(self))
        ### try to delete data:
        ProfilePage.editWebField(self, '')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ### try to enter invalida data:
        ProfilePage.editWebField(self, 'www.alf.')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, 'alf.kh.ua')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, '#$%^&')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, 'www.alf.   kh')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, 'www. alf.kh')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, 'wwwalfkh')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editWebField(self, 'www.alf@kh')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        #### return the test data to start state:
        ProfilePage.editWebField(self, 'www.alf.kh.ua')
        # time.sleep(3)
        self.assertEqual(text, ProfilePage.getWebString(self))

        # Test scope - check that Email field validates inputted data:
        # @pytest.mark.skip

    def test_editEmailFieldInvalidData(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'stepanova+039@dnt-lab.com'
        text1 = 'Error!'
        text2 = "Input doesn't correspond expected pattern."
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        # time.sleep(3)
        #
        # self.assertEqual(url, HelperTestBase.getURL(self))
        NavigationMenuPage.clickProfile(self)
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        # self.assertEqual(url2, HelperTestBase.getURL(self))
        # self.assertEqual(text, ProfilePage.getEmailString(self))
        ### try to delete data:
        ProfilePage.editEmailField(self, '')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ### try to enter invalida data:
        ProfilePage.editEmailField(self, 'stepanova+039@')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, '@dnt-lab.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, 'stepanova+039dnt-lab.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, 'stepanova+039@dnt-lab.')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, 'stepanova+039@ dnt-lab.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, 'stepanova+039@dnt-lab@com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        ProfilePage.editEmailField(self, 'stepanova+039 @dnt-lab.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        # time.sleep(3)
        #### return the test data to start state:
        ProfilePage.editEmailField(self, 'stepanova@dnt-lab.com')
        # time.sleep(3)
        self.assertEqual(text, ProfilePage.getEmailString(self))

        # Test scope - edit PAYPAL field => Validate windows appears:
        # @pytest.mark.skip

    def test_editPayPalFieldValidDataNotSaved(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'stepanova@dnt-lab.com'
        text1 = "Can't update PayPal email"
        text2 = "Canceled. Do you want to keep former email?"
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(3)
        self.assertEqual(url, HelperTestBase.getURL(self))

        # NavigationMenuPage.clickProfile(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertEqual(text, ProfilePage.getPpString(self))
        ### try to edit data:
        ProfilePage.editPayPalField(self, 'dokoko@dnt-lab.com')
        # Test scope - edit PAYPAL field => Validate windows appears:
        self.assertIs(True, HelperTestBase.checkElementPresent(self, "[data-test-id='modal']"))
        ProfilePage.closeModalWindow(self)
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        # Close warning window and back to Profile screen:
        # HelperTestBase.clickBackButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='shoppingLink']")
        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")

        # NavigationMenuPage.clickProfile(self)
        # checking that changes not saved:
        self.assertEqual(text, ProfilePage.getPpString(self))

        # Test scope - check that PAYPAL field validates inputted data:
        # @pytest.mark.skip

    def test_editPayPalFieldInvalidData(self):
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        text = 'stepanova@dnt-lab.com'
        text1 = 'Error!'
        text2 = "Input doesn't correspond expected pattern."
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', 'Ss1234567')
        time.sleep(3)

        self.assertEqual(url, HelperTestBase.getURL(self))
        # NavigationMenuPage.clickProfile(self)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(2)
        HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        self.assertEqual(text, ProfilePage.getPpString(self))
        ### try to delete data:
        ProfilePage.editPayPalField(self, '')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ### try to enter invalida data:
        ProfilePage.editPayPalField(self, 'stepanova@')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, '@gmail.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova@gmail')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova@ dnt-lab.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova@dnt-lab@com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova.gmail.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova@gmail   com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova @  gmail.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova@gmail. com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)
        ProfilePage.editPayPalField(self, 'stepanova @gmail.com')
        self.assertEqual(text1, HelperTestBase.getModalHeader(self))
        self.assertEqual(text2, HelperTestBase.getModalMessage(self))
        HelperTestBase.clickYesButton(self)
        time.sleep(3)

        #### return the test data to start state:
        ProfilePage.editPayPalField(self, 'stepanova@dnt-lab.com')
        time.sleep(5)
        self.assertEqual(text, ProfilePage.getPpString(self))

    def test_Profile_change_PayPal_email(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'svetast', "Ss1234567")
        time.sleep(3)

        NavigationMenuPage.clickProfile(self)
        time.sleep(3)

        ProfilePage.editPayPalField(self, 'kirtolm@ukr.net')
        time.sleep(3)

        firstNameInp = driver.find_element_by_css_selector("[data-test-id='paypalFirstName']")
        firstNameInp.click()
        firstNameInp.send_keys("Kirill")

        lastNameInp = driver.find_element_by_css_selector("[data-test-id='paypalLastName']")
        lastNameInp.click()
        lastNameInp.send_keys("Tolmachev")

        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        time.sleep(3)

        NavigationMenuPage.clickProfile(self)
        time.sleep(3)

        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(3)

        self.assertIn("kirtolm@ukr.net", driver.page_source)

        """
        Change data back
        """
        ProfilePage.editPayPalField(self, 'kirtolmachev@gmail.com')
        time.sleep(3)

        firstNameInp = driver.find_element_by_css_selector("[data-test-id='paypalFirstName']")
        firstNameInp.click()
        firstNameInp.send_keys("Kirill")

        lastNameInp = driver.find_element_by_css_selector("[data-test-id='paypalLastName']")
        lastNameInp.click()
        lastNameInp.send_keys("Tolmachev")
        time.sleep(3)

        HelperTestBase.clickAndWait(self, "[data-test-id='yesButton']")
        time.sleep(5)

        # @pytest.mark.skip

    def test_uploadPhoto(self):
        # Test scope - click Upload image on  Profile page => Documents folder is  displayed:
        url2 = self.base_url + '/profile'
        url = self.base_url + '/shopping-list'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Testwkmyn', 'Ss123456')
        # time.sleep(3)
        # self.assertEqual(url, HelperTestBase.getURL(self))
        # HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        # HelperTestBase.clickAndWait(self, "[data-test-id='profile']")
        # time.sleep(2)
        NavigationMenuPage.clickProfile(self)
        time.sleep(3)
        self.assertEqual(url2, HelperTestBase.getURL(self))
        ProfilePage.uploadPhoto(self)
        time.sleep(5)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='uploadBtn']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='title']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='shoppingLink']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='title']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profileAddress1']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='newAddress']"), True)
        self.assertIs(HelperTestBase.checkElementPresent(self, "[data-test-id='profileAddressEdit']"), True)
