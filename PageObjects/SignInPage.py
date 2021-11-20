from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    email_create_v = (By.ID, "email_create")
    create_an_account_v = (By.ID, "SubmitCreate")

    email_sign_in_v = (By.ID, "email")
    password_sign_in_v = (By.ID, "passwd")
    sign_in_v = (By.ID, "SubmitLogin")

    def email_create_m(self):
        return self.driver.find_element(*SignInPage.email_create_v)

    def create_an_account_m(self):
        return self.driver.find_element(*SignInPage.create_an_account_v)

    def email_sign_in_m(self):
        return self.driver.find_element(*SignInPage.email_sign_in_v)

    def password_sign_in_m(self):
        return self.driver.find_element(*SignInPage.password_sign_in_v)

    def sign_in_m(self):
        return self.driver.find_element(*SignInPage.sign_in_v)