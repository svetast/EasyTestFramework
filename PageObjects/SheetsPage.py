import timefrom selenium.webdriver import ActionChainsfrom selenium.webdriver.common.keys import Keysfrom HelperTestBase import HelperTestBaseclass SheetsPage(HelperTestBase):    def SubcategoriesPage(self):        driver = self.driver        driver.get(self.base_url)    # Open Sheets:    def openSheets(self):        HelperTestBase.reliableClick(self, "[data-test-id='sheetEditorLink']")        time.sleep(5)        # Close Sheets:    def closeSheets(self):        HelperTestBase.reliableClick(self, "[data-test-id='cancelLink']")        time.sleep(5)    def deleteItem(self):        elements = self.driver.find_elements_by_css_selector("[data-test-id='remove']")        actionChains = ActionChains(self.driver)        actionChains.click(elements[0])        actionChains.perform()    def getPageNumber(self):        pageCounter = HelperTestBase.getText(self, "[data-test-id='pageCounter']")        return pageCounter    def typeTextOnProductItemField(self, text=None):        field = self.driver.find_element_by_xpath("//div[3]/div/div/div/table/tbody/tr[1]/td[1]/div").click()        actionChains = ActionChains(self.driver)        field.send_keys(Keys.NULL)        actionChains.double_click(field).perform()        time.sleep(2)    def typeTextOnRecordField(self, text):        field = self.driver.find_element_by_xpath("//div[3]/div/div/div/table/tbody/tr[1]/th").click()        actionChains = ActionChains(self.driver)        actionChains.double_click(field).perform()        time.sleep(2)    def clickOnRecordField(self):        field = self.driver.find_element_by_xpath("//div[3]/div/div/div/table/tbody/tr[1]/th").click()        time.sleep(1)        return field    def clickOnCategoryField(self):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[3]").click()        time.sleep(1)        return field    def clickOnSubCategoryField(self):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[4]").click()        time.sleep(1)        return field    def clickOnSubCategoryEntryField(self):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[5]").click()        time.sleep(1)        return field    def clickOnCurrentQTYField(self):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[17]").click()        time.sleep(1)        return field    def clickImageProduct(self):        image = self.driver.find_elements_by_css_selector("[data-test-id ='photoURL']")        image[0].click()    def editProductItemField(self, text=None):        field = self.driver.find_element_by_xpath("//div[3]/div/div/div/table/tbody/tr[1]/td[1]/div")        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def clickSaveButton(self):        HelperTestBase.reliableClick(self, "[data-test-id='saveBtn']")    def editSellerNameField(self, text):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[7]")        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def editDescription(self, text):        field = self.driver.find_elements_by_xpath('//div[@class="cell__description"]')        actionChains = ActionChains(self.driver)        actionChains.double_click(field[0])        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def editPrice(self, price):        field = self.driver.find_element_by_xpath('//div[1]/div/div/div/table/tbody/tr[1]/td[9]')        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(price)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def selectUnits(self, text=None):        units = self.driver.find_elements_by_xpath("//div[@class='htAutocompleteArrow']")        actionChains = ActionChains(self.driver)        actionChains.double_click(units[0])        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def selectQuantityUnits(self, text=None):        units = self.driver.find_elements_by_xpath("//div[@class='htAutocompleteArrow']")        actionChains = ActionChains(self.driver)        actionChains.double_click(units[3])        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)        # units = self.driver.find_elements_by_xpath("//div[@class='htAutocompleteArrow']")        # units[3].click()        # box = self.driver.find_element_by_xpath("//td[contains(text(),'Each')]")        # box.click()    def selectCountry(self, text=None):        country = self.driver.find_elements_by_xpath("//td[@class='htAutocomplete']")        actionChains = ActionChains(self.driver)        actionChains.double_click(country[5])        actionChains.send_keys(text)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def selectSaleUnits(self, saleUnits=None):        units = self.driver.find_elements_by_xpath("//div[@class='htAutocompleteArrow']")        units[6].click()        box = self.driver.find_element_by_xpath("//td[contains(text(),'Each')]")        box.click()    def checkedCheckbox(self):        self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr/td[19]/input").click()        # checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        # checkbox[0].click()        # for checkbox in checkbox:        #     if not checkbox.is_selected():        #         checkbox.click()    def editProductCode(self, description):        # field = self.driver.find_element_by_xpath("//td[@class='current highlight']")        field = self.driver.find_element_by_xpath('//div[1]/div/div/div/table/tbody/tr/td[18]')        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(description)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def clickImageOrganicSerttificate(self):        HelperTestBase.reliableClick(self, "[data-test-id='organic_certificate_image']")    def clickImageNonGMOSerttificate(self):        HelperTestBase.reliableClick(self, "[data-test-id='nonGMO_certificate_image']")    def editQTY(self, QTY):        field = self.driver.find_element_by_xpath('//div[1]/div/div/div/table/tbody/tr[1]/td[9]')        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(QTY)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def editAvailableQuantity(self, param):        field = self.driver.find_element_by_xpath('//div[1]/div/div/div/table/tbody/tr[1]/td[15]')        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(param)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def clickCreateButton(self):        HelperTestBase.reliableClick(self, "[data-test-id='createBtn']")    def selectDeliveryMethod(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[0])        actionChains.perform()        time.sleep(2)    def selectMarketPickUp(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[1])        actionChains.perform()        time.sleep(2)    def selectOrganic(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[2])        actionChains.perform()        time.sleep(2)    def selectNonGMO(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[3])        actionChains.perform()        time.sleep(2)    def selectSaleIsOn(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[4])        actionChains.perform()        time.sleep(2)    def selectSaleIsActive(self):        checkbox = self.driver.find_elements_by_xpath("//input[@class='htCheckboxRendererInput']")        actionChains = ActionChains(self.driver)        actionChains.double_click(checkbox[5])        actionChains.perform()        time.sleep(2)    def editSalePriceField(self, param):        field = self.driver.find_element_by_xpath("//div[1]/div/div/div/table/tbody/tr[1]/td[29]")        actionChains = ActionChains(self.driver)        actionChains.double_click(field)        actionChains.send_keys(param)        actionChains.send_keys(Keys.ENTER)        actionChains.perform()        time.sleep(2)    def clickDuplicate(self):        button = self.driver.find_element_by_xpath("//div[3]/div/div/div/table/tbody/tr[1]/td[2]/div/button[1]/span[2]")        button.click()