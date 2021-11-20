from selenium.webdriver.common.by import By


class ShippingProductPage:
    def __init__(self, driver):
        self.driver = driver

    term_checkbox_v = (By.XPATH, "//p[@class='checkbox']/div")
    proceed_to_checkout_v = (By.CSS_SELECTOR, "button[name='processCarrier']")
    delivery_price_v = (By.CLASS_NAME, "delivery_option_price")

    def term_checkbox_m(self):
        return self.driver.find_element(*ShippingProductPage.term_checkbox_v)

    def proceed_to_checkout_m(self):
        return self.driver.find_element(*ShippingProductPage.proceed_to_checkout_v)

    def delivery_price_m(self):
        return self.driver.find_element(*ShippingProductPage.delivery_price_v)
