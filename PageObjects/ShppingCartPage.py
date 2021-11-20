from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    product_container_v = (By.CLASS_NAME, "product-container")
    total_price_v = (By.XPATH, "//td[@class = 'cart_total']/span")
    total_shipping_v = (By.ID, "total_shipping")
    total_product_price_v = (By.ID, "total_product")
    last_total_price_v = (By.ID, "total_price_container")
    proceed_checkout_v = (By.LINK_TEXT, "Proceed to checkout")

    def total_price_elements_m(self):
        return self.driver.find_elements(*ShoppingCartPage.total_price_v)

    def total_price_m(self):
        return self.driver.find_element(*ShoppingCartPage.total_price_v)

    def total_price_elements_m(self):
        return self.driver.find_elements(*ShoppingCartPage.total_price_v)

    def total_product_price_m(self):
        return self.driver.find_element(*ShoppingCartPage.total_product_price_v)

    def proceed_checkout_m(self):
        return self.driver.find_element(*ShoppingCartPage.proceed_checkout_v)

    def total_shipping_m(self):
        return self.driver.find_element(*ShoppingCartPage.total_shipping_v)

    def last_total_price_m(self):
        return self.driver.find_element(*ShoppingCartPage.last_total_price_v)