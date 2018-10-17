from PageObjects.SearchScreenPage import SearchScreenPage


class ErrorMessagePage(SearchScreenPage):
    def ErrorMessage(self):
        driver = self.driver
        driver.get(self.base_url)

    def getSearchErrorMessage(self):
        message = self.driver.find_element_by_xpath("//body/app/ng-component/div/h3").text
        return message


