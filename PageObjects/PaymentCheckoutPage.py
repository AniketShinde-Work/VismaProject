
from selenium.webdriver.common.by import By


class PaymentCheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    pay_by_bank_v = (By.CLASS_NAME, "bankwire")
    confirm_order_v = (By.XPATH, "//p[@id='cart_navigation']/button")
    last_box_v = (By.XPATH, "//div[@class='box']/p")

    def pay_by_bank_m(self):
        return self.driver.find_element(*PaymentCheckoutPage.pay_by_bank_v)

    def confirm_order_m(self):
        return self.driver.find_element(*PaymentCheckoutPage.confirm_order_v)

    def last_box_m(self):
        return self.driver.find_element(*PaymentCheckoutPage.last_box_v)
