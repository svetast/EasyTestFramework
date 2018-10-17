from selenium.webdriver.support.ui import Select

from PageObjects.LoginPage import LoginPage


class RegistrationPage(LoginPage):
    def RegistrationPage(self):
        driver = self.driver
        driver.get(self.base_url)

    # Registration:


    def registration(self, firstName=None, lastName=None, login=None, login2 =None, password=None, password2=None,
                     ppFirstName=None, ppLastName=None, ppEmail=None, email=None, phone=None,
                     address1=None, address2=None, city=None, state=None, code=None, country=None):
        self.driver.find_element_by_name("firstName").send_keys(firstName)
        self.driver.find_element_by_name("lastName").send_keys(lastName)
        self.driver.find_element_by_name("login").send_keys(login)
        self.driver.find_element_by_name("login2").send_keys(login2)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password2").send_keys(password2)
        self.driver.find_element_by_name("ppFirstName").send_keys(ppFirstName)
        self.driver.find_element_by_name("ppLastName").send_keys(ppLastName)
        self.driver.find_element_by_name("ppEmail").send_keys(ppEmail)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("phone").send_keys(phone)
        self.driver.find_element_by_name("address1").send_keys(address1)
        self.driver.find_element_by_name("address2").send_keys(address2)
        self.driver.find_element_by_name("city").send_keys(city)
        self.driver.find_element_by_name("state").click()
        select1 = Select(self.driver.find_element_by_name("state"))
        select1.select_by_index(state)
        self.driver.find_element_by_name("postCode").send_keys(code)
        self.driver.find_element_by_name("country").click()
        select = Select(self.driver.find_element_by_name("country"))
        select.select_by_index(country)
        self.driver.find_element_by_css_selector("[data-test-id='signupBtn']").click()

    def registrationWitoutCountry(self, firstName=None, lastName=None, login=None, login2=None, password=None, password2=None,
                     ppFirstName=None, ppLastName=None, ppEmail=None, email=None, phone=None,
                     address1=None, address2=None, city=None, state=None, code=None, country=None):
        self.driver.find_element_by_name("firstName").send_keys(firstName)
        self.driver.find_element_by_name("lastName").send_keys(lastName)
        self.driver.find_element_by_name("login").send_keys(login)
        self.driver.find_element_by_name("login2").send_keys(login2)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password2").send_keys(password2)
        self.driver.find_element_by_name("ppFirstName").send_keys(ppFirstName)
        self.driver.find_element_by_name("ppLastName").send_keys(ppLastName)
        self.driver.find_element_by_name("ppEmail").send_keys(ppEmail)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("phone").send_keys(phone)
        self.driver.find_element_by_name("address1").send_keys(address1)
        self.driver.find_element_by_name("address2").send_keys(address2)
        self.driver.find_element_by_name("city").send_keys(city)
        self.driver.find_element_by_name("state").click()
        select1 = Select(self.driver.find_element_by_name("state"))
        select1.select_by_index(state)
        self.driver.find_element_by_name("postCode").send_keys(code)
        self.driver.find_element_by_css_selector("[data-test-id='signupBtn']").click()

    def registrationWitoutState(self, firstName=None, lastName=None, login=None, login2=None, password=None, password2=None,
                     ppFirstName=None, ppLastName=None, ppEmail=None, email=None, phone=None,
                     address1=None, address2=None, city=None, state=None, code=None, country=None):
        self.driver.find_element_by_name("firstName").send_keys(firstName)
        self.driver.find_element_by_name("lastName").send_keys(lastName)
        self.driver.find_element_by_name("login").send_keys(login)
        self.driver.find_element_by_name("login2").send_keys(login2)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("password2").send_keys(password2)
        self.driver.find_element_by_name("ppFirstName").send_keys(ppFirstName)
        self.driver.find_element_by_name("ppLastName").send_keys(ppLastName)
        self.driver.find_element_by_name("ppEmail").send_keys(ppEmail)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("phone").send_keys(phone)
        self.driver.find_element_by_name("address1").send_keys(address1)
        self.driver.find_element_by_name("address2").send_keys(address2)
        self.driver.find_element_by_name("city").send_keys(city)
        self.driver.find_element_by_name("postCode").send_keys(code)
        self.driver.find_element_by_name("country").click()
        select = Select(self.driver.find_element_by_name("country"))
        select.select_by_index(country)
        self.driver.find_element_by_css_selector("[data-test-id='signupBtn']").click()

    # click on 'Log In' link on the header of 'Sign In' form:
    def clickLogInLink(self):
        self.driver.find_element_by_xpath("//a/span").click()
        self.driver.find_element_by_css_selector("[data-test-id='loginLink2']")

    # click on '<'  icon  on the header of 'Sign In' form:
    def clickLogInIcon(self):
        #self.driver.find_element_by_xpath("//a/img").click()
        self.driver.find_element_by_css_selector("[data-test-id='loginLink']")

    # Subit the 'Registration form' with empty fields:
    def registrationEmptyFields(self):
        self.driver.find_element_by_css_selector("[data-test-id='signupBtn']").click()

    ### Select "Seller" option on RegPage:
    def switchShopperSeller(self):
            self.driver.find_element_by_css_selector("[data-test-id='SwitchShopperSeller']").click()


    ###################### HELPER for REGISTRATION ##########################


 ### get the 'Log in' text:
    def getSignUpText(self):
       text = self.driver.find_element_by_xpath("//body/app-root/div/div/signup/div/div[1]/div/div/h4").text
       return text



    ### get the 'Log In' text:

    def getLogInText(self):
        text = self.driver.find_element_by_xpath("//app-root/div/div/signup/div/div[1]/div/a/span").text
        return text                   #/app-root/div/app-header/header/signup-header/nav/div[1]/a/span

    ###   get the 'Welcome! Please select account type.' text:

    def getWelcomeMessage(self):
        message = self.driver.find_element_by_css_selector("[data-test-id='welcome']").text
        #message = self.driver.find_element_by_xpath("//body/app-root/div/div/signup/div/div[2]/p").text
        return message



        ### The messages if registration was successfull:
#  get text  'Success! You have almost finished.'
    def getSuccessMessage1(self):
        message1 = self.driver.find_element_by_css_selector("[data-test-id='successSignup']")
        return message1


# get text 'Please, check your email and follow the verification link to complete you registration. After you finish, come back and log in.'
    def getSuccessMessage2(self):
        message2 = self.driver.find_element_by_xpath("//div/p").text
        return message2

    # The messages if registration was Un_Successfull ( "Please check all the fields for completeness or typos.") :

    def getUnSuccessMessage(self):
        errorMessage = self.driver.find_element_by_xpath("//signup/div/form/div/div[2]/div/span").text
        return errorMessage

    def getErrorMessage(self):
        errorMessage = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/p").text
        return errorMessage

    def getErrorAlertTitle(self):
        alertTitle = self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/h3").text
        return alertTitle

    def clickOkButton(self):
        self.driver.find_element_by_xpath("//body/app-root/div/modal/div/div/button").click()











            #        ActionChains(self.driver).move_to_element(self.driver.find_element_by_name("login")).send_keys(login).perform()