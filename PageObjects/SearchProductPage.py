from selenium.webdriver.common.by import By


class SearchProductPage:
    def __init__(self, driver):
        self.driver = driver

    product_container_v = (By.CLASS_NAME, "product-container")
    product_image_link_v = (By.CLASS_NAME, "product-image-container")
    quick_view_v = (By.CLASS_NAME, "quick-view")
    product_name_v = (By.CLASS_NAME, "product-name")
    add_to_cart_v = (By.XPATH, "//div[@class='button-container']/a")
    continue_shopping_after_cart_v = (By.CLASS_NAME, "continue")
    left_block_v = (By.CLASS_NAME, "left-block")

    def product_container_elements_m(self):
        return self.driver.find_elements(*SearchProductPage.product_container_v)

    def product_container_m(self):
        return self.driver.find_element(*SearchProductPage.product_container_v)

    def product_image_link_m(self):
        return self.driver.find_element(*SearchProductPage.product_image_link_v)

    def left_block_m(self):
        return self.driver.find_element(*SearchProductPage.left_block_v)

    def quick_view_m(self):
        return self.driver.find_element(*SearchProductPage.quick_view_v)

    def product_name_m(self):
        return self.driver.find_element(*SearchProductPage.product_name_v)

    def add_to_cart_m(self):
        return self.driver.find_element(*SearchProductPage.add_to_cart_v)

    def continue_shopping_after_cart_m(self):
        return self.driver.find_element(*SearchProductPage.continue_shopping_after_cart_v)
