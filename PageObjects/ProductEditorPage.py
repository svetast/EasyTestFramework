import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from HelperTestBase import HelperTestBase
from PageObjects.CategoriesMenuPage import CategoriesMenuPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class ProductEditorPage(LoginPage):
    def ProductEditorPage(self):
        driver = self.driver
        driver.get(self.base_url)

    def addProductWithoutYear(self, title=None, price=None,
                    description=None, sortUnits=None,
                    currentQuantityInp=None, sortQTY=None,
                    country=None, productCodeInp=None,
                    salePrice=None, sortSalePrice=None):
        self.openProductEditor()
        time.sleep(4)
        self.setTitle(title)
        self.setDescription(description)
        self.setPrice1(price)
        self.sortUnits(sortUnits)
        self.setQTY1(currentQuantityInp)
        self.sortQuantity(sortQTY)
        self.setProductCode(productCodeInp)
        self.sortCountry(country)
        self.clickSwitch()
        self.setSalePrice1(salePrice)
        self.sortSalePrice(sortSalePrice)
        self.clickSaveButton()

    def returtTestData(self, title=None, price=None,
                       description=None, sortUnits=None,
                       currentQuantityInp=None, sortQTY=None,
                       country=None, productCodeInp=None):

        NavigationMenuPage.clickNewItem(self)
        CategoriesMenuPage.clickFruitsButton(self)
        self.selectCategory()
        self.setTitle(title)
        self.setDescription(description)
        self.setPrice1(price)
        self.sortUnits(sortUnits)
        self.setQTY1(currentQuantityInp)
        self.sortQuantity(sortQTY)
        self.setProductCode(productCodeInp)
        self.sortCountry(country)
        self.clickSwitch()
        self.clickSaveButton()

    def selectCategory(self):
         HelperTestBase.clickAndWait(self, "[data-test-id='subcategory_0']")
         HelperTestBase.clickAndWait(self, "[data-test-id='entry_0']")
         HelperTestBase.clickAndWait(self, "[data-test-id='nextLink']")

    def editProduct(self, title):
        self.goProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").send_keys(title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)

        self.clickSaveButton()



    def addProduct(self, title=None, price=None,
                    description=None, sortUnits=None, yearFrom=None,
                    dayTill=None, monthTill=None, yearTill=None,
                    currentQuantityInp=None, sortQTY=None,
                    country=None, productCodeInp=None,
                    salePrice=None, sortSalePrice=None):
        self.openProductEditor()
        time.sleep(3)
        self.setTitle(title)
        self.setDescription(description)
        self.setPrice1(price)
        self.sortUnits(sortUnits)
        self.selectPriceValidYearFrom(yearFrom)
        #self.selectPriceValidDayTill(dayTill)
        #self.selectPriceValidMonthTill(monthTill)
        self.selectPriceValidYearTill(yearTill)
        self.setQTY1(currentQuantityInp)
        self.sortQuantity(sortQTY)
        self.setProductCode(productCodeInp)
        self.sortCountry(country)
        self.clickSwitch()
        self.setSalePrice1(salePrice)
        self.sortSalePrice(sortSalePrice)
        self.clickSaveButton()

    def addItemSuccess(self, title=None,
                       description=None,
                       price=None,
                       currentQuantityInp=None,
                       productCodeInp=None):
        self.openProductEditor()
        HelperTestBase.setText(self, "[data-test-id='Product Item']", title)
        HelperTestBase.inputText(self, "description", description)
        HelperTestBase.setText(self, "[data-test-id='sellingPriceInp']", price)
        HelperTestBase.setText(self, "[data-test-id='currentQuantityInp']", currentQuantityInp)
        HelperTestBase.setText(self, "[data-test-id='productCodeInp']", productCodeInp)
        self.sortUnits("Each")
        self.sortCountry('United States')
        self.sortQuantity('Box')
        self.clickSwitch()
        self.clickSaveButton()

    def sortUnits(self, sortUnits=None):
        self.driver.find_element_by_css_selector("[data-test-id='priceUnitsName']").click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='priceUnitsName']"))
        select.select_by_visible_text(sortUnits)

    def sortCountry(self, country=None):
        self.driver.find_element_by_css_selector("[data-test-id='countrySelect']").click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='countrySelect']"))
        select.select_by_visible_text(country)

    def sortQuantity(self, sortquantity=None):
        # self.driver.find_element_by_css_selector("[data-test-id='qtyUnitName']").click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='qtyUnitName']"))
        select.select_by_visible_text(sortquantity)

    def sortSalePrice(self, sortsaleprice=None):
        self.driver.find_element_by_css_selector("[data-test-id='saleUnitName']").click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='saleUnitName']"))
        select.select_by_visible_text(sortsaleprice)

    def selectPriceValidYearFrom(self, yearFrom=None):
        years = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years[0].click()
        time.sleep(3)
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select.select_by_visible_text(yearFrom)
        time.sleep(2)

    def selectPriceValidYearTill(self, yearTill=None):
        years = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years[1].click()
        time.sleep(3)
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select.select_by_visible_text(yearTill)
        time.sleep(2)

    def selectPriceValidDayTill(self, dayTill=None):
        days = self.driver.find_elements_by_css_selector("[data-test-id='daySelect']")
        days[1].click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='daySelect']"))
        select.select_by_visible_text(dayTill)
        time.sleep(2)

    def selectPriceValidMonthTill(self, monthTill=None):
        months = self.driver.find_elements_by_css_selector("[data-test-id='monthSelect']")
        months[0].click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='monthSelect']"))
        select.select_by_visible_text(monthTill)
        time.sleep(2)




    def selectProductionDate(self, year=None):
        years2 = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years2[2].click()
        select2 = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select2.select_by_visible_text(year)

    def selectSaleFrom(self, year=None):
        years3 = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years3[3].click()
        select3 = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select3.select_by_visible_text(year)

    def selectSaleTill(self, year=None):
        years4 = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years4[4].click()
        select4 = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select4.select_by_visible_text(year)

    def clickSwitch(self):
        self.driver.find_element_by_css_selector("[data-test-id='deliveryOfferedSwitch']").click()
        self.driver.find_element_by_css_selector("[data-test-id='pickUpOfferedSwitch']").click()
        self.driver.find_element_by_css_selector("[data-test-id='activeSwitch']").click()

    def clickSwitchDelivery(self):
        self.driver.find_element_by_css_selector("[data-test-id='deliveryOfferedSwitch']").click()

    def clickSwitchOffered(self):
        self.driver.find_element_by_css_selector("[data-test-id='pickUpOfferedSwitch']").click()

    def clickSwitchActive(self):
        self.driver.find_element_by_css_selector("[data-test-id='activeSwitch']").click()

    def clickSaveButton(self):
        HelperTestBase.reliableClick(self, "[data-test-id='saveBtn']")
        #self.driver.find_element_by_css_selector("[data-test-id='saveBtn']").click()


    def openProductEditor(self):

        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")
        time.sleep(5)
        HelperTestBase.clickAndWait(self, "[data-test-id='footerMainBtn']")
        time.sleep(4)
        HelperTestBase.clickAndWait(self, "[data-test-id='new-item']")
        #self.driver.find_element_by_css_selector("[data-test-id='new-item']").click()
        time.sleep(3)
        HelperTestBase.clickAndWait(self, "[data-test-id='Fruits']")
        #self.driver.find_element_by_css_selector("[data-test-id='Fruits']").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("[data-test-id='subcategory_8']").click()
        self.driver.find_element_by_css_selector("[data-test-id='entry_0']").click()
        self.driver.find_element_by_css_selector("[data-test-id='nextLink']").click()
        time.sleep(3)

    def selectSomeCategory(self):
        self.driver.find_element_by_css_selector("[data-test-id='subcategory_2']").click()
        self.driver.find_element_by_css_selector("[data-test-id='entry_0']").click()
        self.driver.find_element_by_css_selector("[data-test-id='nextLink']").click()
        time.sleep(3)



    def goProductEditor(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='sellerBtn']")
        time.sleep(8)
        #self.clickOk()
        HelperTestBase.clickAndWait(self, "[data-test-id='inventoryItem-0']")

    def setTitle(self, title):
        elem = self.driver.find_element_by_css_selector("[data-test-id='Product Item']")
        elem.click()
        elem.send_keys(title)
        #HelperTestBase.editText(self, "[data-test-id='Product Item']", title)

    def setTitleOnly(self, title=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        self.clickSaveButton()

    def setPrice(self, title=None, price=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)

        self.clickSaveButton()

    def setPrice1(self, price=None):
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)

    def setDescription(self, description=None):
        HelperTestBase.inputText(self, "description", description)

    def setInvPrice(self, title=None, price=None):
        self.openProductEditor()
        time.sleep(2)
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")

    def setUnits(self, title=None, price=None):
        self.openProductEditor()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")
        self.clickSaveButton()

    def setQTY(self, title=None, price=None, avaiableQuantityInp=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)

        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        self.sortUnits("Each")
        #self.clickSwitch()
        time.sleep(2)
        self.clickSaveButton()

    def setQTY1(self, avaiableQuantityInp=None):
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)

    def setProductCode(self, productCodeInp=None):
        HelperTestBase.editText(self, "[data-test-id='productCodeInp']", productCodeInp)

    def setCountryWithoutDeliveryMethod(self, title=None, price=None, avaiableQuantityInp=None, country=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        self.sortQuantity("Each")
        self.sortCountry(country)
        self.clickSaveButton()

    def setDeliveryMethodWitoutCountry(self, title=None, price=None, avaiableQuantityInp=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        self.sortQuantity("Each")
        self.clickSwitch()
        self.clickSaveButton()

    def setSalePrice(self, title=None, price=None, avaiableQuantityInp=None, country=None, salePrice=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")
        HelperTestBase.setText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        time.sleep(1)
        self.sortQuantity("Each")
        self.sortCountry(country)
        self.clickSwitch()
        HelperTestBase.editText(self, "[data-test-id='salePriceInp']", salePrice)
        self.sortSalePrice("Each")

        self.clickSaveButton()

    def setInvalidSalePrice(self, salePrice=None, title=None, price=None, avaiableQuantityInp=None, country=None):
        self.openProductEditor()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").click()
        self.driver.find_element_by_css_selector("[data-test-id='Product Item']").clear()
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        self.driver.find_element_by_css_selector("[data-test-id='Seller Name']").send_keys(Keys.ENTER)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        time.sleep(1)
        self.sortUnits("Each")
        HelperTestBase.editText(self, "[data-test-id='salePriceInp']", salePrice)
        time.sleep(1)
        self.sortCountry(country)
        self.sortQuantity("Each")
        time.sleep(1)
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        self.clickSaveButton()

    def setSalePrice1(self, salePrice=None):
        HelperTestBase.editText(self, "[data-test-id='salePriceInp']", salePrice)

    def selectPriceValidOption(self, title=None,
                               price=None, avaiableQuantityInp=None,
                               country=None, productCodeInp=None,
                               salePrice=None, year=None, year1=None):
        self.openProductEditor()
        time.sleep(5)
        HelperTestBase.editText(self, "[data-test-id='Product Item']", title)
        HelperTestBase.editText(self, "[data-test-id='sellingPriceInp']", price)
        self.sortUnits("Each")
        HelperTestBase.editText(self, "[data-test-id='avaiableQuantityInp']", avaiableQuantityInp)
        self.sortQuantity("Each")
        HelperTestBase.editText(self, "[data-test-id='productCodeInp']", productCodeInp)
        self.sortCountry(country)
        self.clickSwitch()
        HelperTestBase.editText(self, "[data-test-id='salePriceInp']", salePrice)
        self.sortSalePrice("Each")
        years0 = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years0[0].click()
        select = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select.select_by_visible_text(year)
        years1 = self.driver.find_elements_by_css_selector("[data-test-id='yearSelect']")
        years1[1].click()
        select1 = Select(self.driver.find_element_by_css_selector("[data-test-id='yearSelect']"))
        select1.select_by_visible_text(year1)
        self.clickSaveButton()

    def clickOk(self):
        self.driver.find_element_by_class_name('modal__btn').click()

    def clickCancel(self):
        self.driver.find_element_by_css_selector("[data-test-id='cancelLink']").click()

    def deleteItemFromInventoryList(self):
        HelperTestBase.clickAndWait(self, "[data-test-id='removeItem_0']")

    def yesCancelEditing(self):
        self.driver.find_element_by_css_selector("[data-test-id='yes']").click()

    def noCancelEditing(self):
        self.driver.find_element_by_css_selector("[data-test-id='no']").click()


    def addEventAction(self):
        self.driver.find_element_by_css_selector("[data-test-id='addEventElem']").click()
        time.sleep(5)

    def clickEventTitle(self):
        HelperTestBase.reliableClick(self, "[data-test-id='eventTitle']")
        time.sleep(3)

    def checkMapPresent(self):
        state = self.driver.find_element_by_css_selector(
            "body > app-root > div > div > product-editor-strategy > existing-event-editor > div > div > event-section > section > div > div").is_displayed()
        return state
