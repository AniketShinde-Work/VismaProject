import inspect
import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from PageObjects.AddressCheckOutPage import AddressCheckOutPage
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.PaymentCheckoutPage import PaymentCheckoutPage
from PageObjects.ShippingProductPage import ShippingProductPage
from PageObjects.ShppingCartPage import ShoppingCartPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_presence(self,text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_value(self, locator, value):
        dropdown = Select(locator)
        dropdown.select_by_value(value)

    def select_option_by_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def check_successfully_my_account_page(self):
        log = self.getLogger()
        my_account_page_t = MyAccountPage(self.driver)
        success_account = my_account_page_t.navigate_my_account_m().text

        if success_account == "My account":
            log.info("Successfully registered")
        else:
            log.error("UnSuccessfully registered")

    def choose_file(self, element):

        self.driver.send_keys(element)

    def hover_action(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    def hover_and_click_action(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).click().perform()

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def navigate_back(self):
        self.driver.back()

    def checkout_process(self):
        log = self.getLogger()
        log.info("Inside Checkout Process")
        shopping_cart_page_t = ShoppingCartPage(self.driver)
        log.info("Verifying the total amount")
        all_total = shopping_cart_page_t.total_price_elements_m()
        addition_v = 0
        for single_total in all_total:
            single_amount = single_total.text
            amount = float(single_amount.lstrip('$'))
            addition_v = addition_v + amount
        total_footer = shopping_cart_page_t.total_product_price_m().text
        total_footer_float = float(total_footer.lstrip('$'))

        addition = round(addition_v, 2)
        assert addition == total_footer_float

        shopping_cart_page_t.proceed_checkout_m().click()
        address_checkout_page_t = AddressCheckOutPage(self.driver)
        address_checkout_page_t.proceed_to_checkout_m().click()

        shipping_product_page_t = ShippingProductPage(self.driver)
        shipping_price = shipping_product_page_t.delivery_price_m().text
        log.info("Checking the delivery price")
        ship_price = float(shipping_price.lstrip('$'))
        print(ship_price)
        assert ship_price == 2.00
        log.info("Checking term of service checkbox")
        shipping_product_page_t.term_checkbox_m().click()
        shipping_product_page_t.proceed_to_checkout_m().click()

        payment_checkout_page_t = PaymentCheckoutPage(self.driver)
        self.adding_product_and_shipping()
        payment_checkout_page_t.pay_by_bank_m().click()
        payment_checkout_page_t.confirm_order_m().click()
        order_complete = payment_checkout_page_t.last_box_m().text
        assert "complete" in order_complete

    def adding_product_and_shipping(self):
        log = self.getLogger()
        log.info("Verifying the amount with the total amount method")
        shopping_cart_page_t = ShoppingCartPage(self.driver)
        total_product_price_b = shopping_cart_page_t.total_product_price_m().text
        total_product_price_a = float(total_product_price_b.lstrip('$'))
        total_product_price_f = round(total_product_price_a, 2)

        total_shipping_price_b = shopping_cart_page_t.total_shipping_m().text
        total_shipping_price_a = float(total_shipping_price_b.lstrip('$'))
        total_shipping_price_f = round(total_shipping_price_a, 2)

        total_product_shipping = total_product_price_f + total_shipping_price_f

        last_total_price_b = shopping_cart_page_t.last_total_price_m().text
        last_total_price_a = float(last_total_price_b.lstrip('$'))
        last_total_price_f = round(last_total_price_a, 2)

        print(total_product_shipping)
        print(last_total_price_f)
        assert total_product_shipping == last_total_price_f












