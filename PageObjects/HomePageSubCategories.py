from PageObjects.NavigationMenuPage import NavigationMenuPage


class HomePageSubCategories(NavigationMenuPage):
    def HomePageSubCategories(self):
        driver = self.driver
        driver.get(self.base_url)




    #####  Click on 'SubCategories':



    # def clickSubCategory(self, category):
    # self.driver.find_element_by_xpath(category).click()

    ##### 1.  'Fruits' Sub Categories: ####################

    def clickApple(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Apple')]").click()

    def clickAvocado(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Avocado')]").click()

    def clickBanana(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Banana')]").click()

    def clickVegetablesSubCategories(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

    def clickMeatSubCategories(self):
        self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

    ##### 2.  'Vegetables' Sub Categories: ####################

    def clickArtichoke(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Artichoke')]").click()

    def clickArugula(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Arugula')]").click()

    def clickGarlic(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Garlic')]").click()

    def clickCarrot(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Carrot')]").click()

        #####  3.  'Meat' Sub Categories:  ####################

        ## Beef  ## Pork ##  Bacon ## Lamb ## Mutton ##  Rabbit ## Veal ## Venison ## Wild Boar ##

    def clickBeef(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Beef')]").click()

    def clickPork(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Pork')]").click()

    def clickBacon(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Bacon')]").click()

    def clickLamb(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Lamb')]").click()

    def clickMutton(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Mutton')]").click()

    def clickRabbit(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Rabbit')]").click()

    def clickVeal(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Veal')]").click()

    def clickVenison(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Venison')]").click()

    def clickWildBoar(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Wild Boar')]").click()

    ##### 4.  'Bakery' Sub Categories:   #################

    def clickBread(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Bread')]").click()

    def clickCupcakes(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Cupcake')]").click()

    def clickBrownies(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Brownie')]").click()

    def clickCookies(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Cookie')]").click()

    def clickCakes(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Cakes')]").click()

    ##### 5.  'Poultry' Sub Categories: ####################

    def clickChicken(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Chicken')]").click()

    def clickDuck(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Duck')]").click()

    def clickTurkey(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Turkey')]").click()

        #####  6.  'Dairy' Sub Categories: ####################

    def clickMilk(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Milk')]").click()

    def clickYogurt(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Yogurt')]").click()

    def clickCheese(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Cheese')]").click()

    def clickIceCream(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Ice Cream')]").click()

    def clickButter(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Butter')]").click()

        #####  7.  'Sea Foog' Sub Categories: ####################

    def clickCrab(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Crab')]").click()

    def clickLobster(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Lobster')]").click()

    def clickShrimp(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Shrimp')]").click()

    def clickSalmon(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Salmon')]").click()

    def clickSeaBass(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Sea bass')]").click()

    def clickSwordfish(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Swordfish')]").click()

    def clickCatfish(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Catfish')]").click()

    def clickHalibut(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Halibut')]").click()

    def clickHerring(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Herring')]").click()

    def clickOyster(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Oyster')]").click()

    def clickSnapper(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Snapper')]").click()

    def clickTuna(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Tuna')]").click()




        #####  8.  'Other' Sub Categories: ####################

    def clickFlowers(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Flowers')]").click()

    def clickNuts(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Nuts')]").click()

    def clickSeeds(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Seeds')]").click()

    def clickHoney(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Honey')]").click()

    def clickPreserves(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Preserves')]").click()

    def clickPopcorn(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Popcorn')]").click()

    def clickPersonalCare(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Personal Care')]").click()

    def clickCandlesFragrances(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Candles')]").click()

    def clickPicklesRelishesOlives(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Pickles')]").click()

    def clickChocolate(self):
        self.driver.find_element_by_xpath("//li[contains(text(),'Chocolate')]").click()


        #############################################


""" def clickPoultrySubCategories(self):
     self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

 def clickDairySubCategories(self):
     self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

 def clickSeaFoodSubCategories(self):
     self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

 def clickSubCategories(self):
     self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()

 def clickVegetablesSubCategories(self):
     self.driver.find_element_by_xpath("//li[contains(text(),' Vegetables')]").click()"""
