import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObjects.AddressCheckOutPage import AddressCheckOutPage
from PageObjects.HomePage import HomePage
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.PaymentCheckoutPage import PaymentCheckoutPage
from PageObjects.SearchProductPage import SearchProductPage
from PageObjects.SelectedProductPage import SelectedProductPage
from PageObjects.ShippingProductPage import ShippingProductPage
from PageObjects.ShppingCartPage import ShoppingCartPage
from PageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestE2EOrder(BaseClass):

    def test_product_purchase(self):
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

        for product in products:
            product_name = product.find_element(By.CLASS_NAME, "product-name").text

            if product_name == "Blouse":
                product.find_element(By.CLASS_NAME, "product-name").click()
                selected_product_page_t = SelectedProductPage(self.driver)
                selected_product_page_t.add_to_cart_m().click()
                selected_product_page_t.proceed_to_checkout_m().click()
                break

        self.checkout_process()


