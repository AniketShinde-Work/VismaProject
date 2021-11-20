from selenium.webdriver.common.by import By


class AddressCheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    proceed_to_checkout_v = (By.XPATH, "//button[@name='processAddress']/span")

    def proceed_to_checkout_m(self):
        return self.driver.find_element(*AddressCheckOutPage.proceed_to_checkout_v)
