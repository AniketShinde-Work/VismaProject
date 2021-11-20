import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.SearchProductPage import SearchProductPage
from PageObjects.SelectedProductPage import SelectedProductPage
from PageObjects.ShppingCartPage import ShoppingCartPage
from PageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestE2EOrder(BaseClass):

    def test_product_purchase_quick_view(self):
        log = self.getLogger()

        home_page_t = HomePage(self.driver)
        home_page_t.sign_in_m().click()

        sign_in_page_t = SignInPage(self.driver)
        sign_in_page_t.email_sign_in_m().send_keys("aniket111111111111@cmail.com")
        log.info("Entering the email address")
        sign_in_page_t.password_sign_in_m().send_keys("abc123")
        log.info("Entering the password")
        sign_in_page_t.sign_in_m().click()
        log.info("Checking if successfully signed In")
        self.check_successfully_my_account_page()

        my_account_page_t = MyAccountPage(self.driver)
        my_account_page_t.my_account_logo_m().click()

        search_product_page_t = SearchProductPage(self.driver)
        products = search_product_page_t.product_container_elements_m()

        selected_list = ["Faded Short Sleeve T-shirts", "Blouse", "Printed Chiffon Dress"]
        selected_product_page_t = SelectedProductPage(self.driver)

        for product in products:
            product_name = product.find_element(By.CLASS_NAME, "product-name").text

            if product_name in selected_list:

                self.hover_action(product.find_element(By.CLASS_NAME, "product-name"))
                self.hover_and_click_action(product.find_element(By.CLASS_NAME, "quick-view"))
                self.switch_to_frame(1)
                selected_product_page_t.add_to_cart_m().click()
                self.switch_to_default()
                selected_product_page_t.continue_shopping_m().click()

        self.hover_and_click_action(home_page_t.cart_home_m())
        self.checkout_process()






















