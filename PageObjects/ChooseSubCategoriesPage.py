from PageObjects.NavigationMenuPage import NavigationMenuPage


class ChooseSubCategories(NavigationMenuPage):
    def ChooseSubCategories(self):
        driver = self.driver
        driver.get(self.base_url)

    #####  Click on product on 'Now choose between subcategories':

    # Click on 'Pickles'on the Sub Categories:

    def clickPickles(self):
        self.driver.find_element_by_xpath("//app/div/div/home/div/div/ul/li[1]/a").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Pickles')]").click()