
from selenium.webdriver.common.by import By


class SelectedProductPage:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart_v = (By.XPATH, "//p[@id='add_to_cart']/button")
    continue_shopping_v = (By.XPATH, "//div[@class='button-container']/span")
    proceed_to_checkout_v = (By.XPATH, "//div[@class='button-container']/a")
    frame_v = (By.XPATH, "//div[@class='fancybox-inner']/iframe")

    def add_to_cart_m(self):
        return self.driver.find_element(*SelectedProductPage.add_to_cart_v)

    def continue_shopping_m(self):
        return self.driver.find_element(*SelectedProductPage.continue_shopping_v)

    def proceed_to_checkout_m(self):
        return self.driver.find_element(*SelectedProductPage.proceed_to_checkout_v)

    def frame_m(self):
        return self.driver.find_element(*SelectedProductPage.frame_v)