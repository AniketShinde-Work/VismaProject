from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    navigate_my_account_v = (By.CLASS_NAME, "navigation_page")
    my_account_search_v = (By.ID, "search_query_top")
    my_account_search_enter_v = (By.NAME, "submit_search")
    my_account_logo_v = (By.CLASS_NAME, "logo")

    def navigate_my_account_m(self):
        return self.driver.find_element(*MyAccountPage.navigate_my_account_v)

    def my_account_search_m(self):
        return self.driver.find_element(*MyAccountPage.my_account_search_v)

    def my_account_search_enter_m(self):
        return self.driver.find_element(*MyAccountPage.my_account_search_enter_v)

    def my_account_logo_m(self):
        return self.driver.find_element(*MyAccountPage.my_account_logo_v)
