from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    sign_in_v = (By.CLASS_NAME, "login")
    cart_home_v = (By.XPATH, "//div[@class='shopping_cart']/a")
    checkout_home_v = (By.XPATH, "//p[@class='cart-buttons']/a/span")
    contact_us_v = (By.ID, "contact-link")

    def sign_in_m(self):
        return self.driver.find_element(*HomePage.sign_in_v)

    def cart_home_m(self):
        return self.driver.find_element(*HomePage.cart_home_v)

    def checkout_home_m(self):
        return self.driver.find_element(*HomePage.checkout_home_v)

    def contact_us_m(self):
        return self.driver.find_element(*HomePage.contact_us_v)

