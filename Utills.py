from  HelperTestBase import HelperTestBase
from PageObjects.FavoritesPage import FavoritesPage
from PageObjects.NavigationMenuPage import NavigationMenuPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from PageObjects.WatchListPage import WatchListPage


class Utills(HelperTestBase):
    def Utills(self):
        driver = self.driver
        driver.get(self.base_url)

    def removeProductFromCartWatchlistFavorites(self):
        NavigationMenuPage.clickCart(self)
        ShoppingCartPage.deleteItemFromCart(self)
        HelperTestBase.clickBackButton(self)
        NavigationMenuPage.clickWatchlist(self)
        WatchListPage.removeFromWatchList(self)
        HelperTestBase.clickBackButton(self)
        NavigationMenuPage.clickFavoriteList(self)
        FavoritesPage.removeFromFavList(self)
        HelperTestBase.clickBackButton(self)
