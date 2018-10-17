import time

from selenium.webdriver import ActionChains

from HelperTestBase import HelperTestBase
from PageObjects.InventoryListPage import InventoryListPage
from PageObjects.LoginPage import LoginPage
from PageObjects.NavigationMenuPage import NavigationMenuPage


class TestBiziPixEditor(InventoryListPage):
    # @pytest.mark.skip
    def test_clickBiziPixOnInventoryList(self):
        url = self.base_url + '/inventory-list'
        url2 = self.base_url + '/bizipix-editor'
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'Bob', 'Ss123456')
        NavigationMenuPage.clickSellerButton(self)
        self.assertEqual(url, HelperTestBase.getURL(self))
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(2)
        self.assertEqual(url2, HelperTestBase.getURL(self))

        # @pytest.mark.skip

    def test_BiziPix_add_and_remove(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', "Ss123456")
        time.sleep(5)

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='createButton']")

        element = driver.find_elements_by_css_selector("[data-test-id='pickerCell']")[0]
        el_name = driver.find_elements_by_css_selector("[data-test-id='pickerCellTitle']")[0].text
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)
        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(6)

        self.assertIn(el_name, driver.page_source)

        HelperTestBase.reliableClick(self, "[data-test-id='removeTagButton']")
        HelperTestBase.reliableClick(self, "[class='tag__trash']")

        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(4)
        self.assertNotIn(el_name, driver.page_source)

        # @pytest.mark.skip

    def test_BiziPix_close(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SA1', "Bizibaza111")
        time.sleep(5)

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        HelperTestBase.reliableClick(self, "[data-test-id='closeButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        self.assertEqual(self.base_url + "/inventory-list", driver.current_url)

        #  @pytest.mark.skip

    def test_BiziPix_click_and_move(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', "Ss123456")
        time.sleep(5)

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(5)

        HelperTestBase.reliableClick(self, "[data-test-id='createButton']")
        element = driver.find_elements_by_css_selector("[data-test-id='pickerCell']")[0]
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)

        element = driver.find_element_by_tag_name('tag')
        element.click()
        time.sleep(3)

        element = driver.find_elements_by_css_selector("[data-test-id='tag']")[1]
        coords_start = element.location

        self.assertEqual("ng-resizable dots ngresizable active", element.get_attribute("class"))

        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(element, -100, 0)
        actions.perform()
        coords_finish = element.location
        self.assertNotEqual(coords_start, coords_finish)

        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(10)

        element = driver.find_elements_by_css_selector("[data-test-id='tag']")[1]
        self.assertEqual(coords_finish, element.location)

        HelperTestBase.reliableClick(self, "[data-test-id='removeTagButton']")
        HelperTestBase.reliableClick(self, "[class='tag__trash']")
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        time.sleep(4)

        # @pytest.mark.skip

    def test_BiziPix_resize(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', "Ss123456")
        time.sleep(5)

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(5)

        HelperTestBase.reliableClick(self, "[data-test-id='createButton']")
        element = driver.find_elements_by_css_selector("[data-test-id='pickerCell']")[0]
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)

        element = driver.find_elements_by_css_selector("[data-test-id='tag']")[-1]
        dot = driver.find_element_by_css_selector("[ng-reflect-ng-class='ngr-top-right']")
        size_start = element.size

        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(dot, 50, -25)
        actions.perform()
        time.sleep(7)

        size_finish = element.size
        self.assertNotEqual(size_start, size_finish)

        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        time.sleep(5)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(5)

        element = driver.find_elements_by_css_selector("[data-test-id='tag']")[-1]
        dot = driver.find_element_by_css_selector("[ng-reflect-ng-class='ngr-top-right']")
        self.assertEqual([size_finish[i] + 2 for i in size_finish], [element.size[i] for i in element.size])

        HelperTestBase.reliableClick(self, "[data-test-id='removeTagButton']")
        HelperTestBase.reliableClick(self, "[class='tag__trash']")
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        time.sleep(5)

        # @pytest.mark.skip

    def test_BiziPix_change(self):
        driver = self.driver
        driver.get(self.base_url)
        LoginPage.loginAction(self, 'SellerTestcjd', "Ss123456")

        NavigationMenuPage.clickSellerButton(self)
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(4)

        HelperTestBase.reliableClick(self, "[data-test-id='createButton']")
        element = driver.find_elements_by_css_selector("[data-test-id='pickerCell']")[0]
        first_el_name = driver.find_elements_by_css_selector("[data-test-id='pickerCellTitle']")[0].text
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(4)

        tag = driver.find_elements_by_css_selector("[data-test-id='tag']")[-1]
        actions = ActionChains(driver)
        actions.click(tag)
        actions.click(tag)
        actions.perform()
        time.sleep(4)

        element = driver.find_elements_by_css_selector("[data-test-id='pickerCell']")[1]
        el_name = driver.find_elements_by_css_selector("[data-test-id='pickerCellTitle']")[1].text
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(4)
        self.assertNotIn(first_el_name, driver.page_source)

        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='biziPixLink']")
        time.sleep(4)
        self.assertIn(el_name, driver.page_source)

        HelperTestBase.reliableClick(self, "[data-test-id='removeTagButton']")
        HelperTestBase.reliableClick(self, "[class='tag__trash']")
        HelperTestBase.reliableClick(self, "[data-test-id='yesButton']")
        HelperTestBase.reliableClick(self, "[data-test-id='saveButton']")
        time.sleep(5)
