from selenium.webdriver.common.by import By


class CreateAnAccountPage:
    def __init__(self, driver):
        self.driver = driver

    first_name_v = (By.ID, "customer_firstname")
    last_name_v = (By.ID, "customer_lastname")
    password_v = (By.ID, "passwd")
    dob_days_v = (By.ID, "days")
    dob_months_v = (By.ID, "months")
    dob_years_v = (By.ID, "years")
    newsletter_sign_v = (By.ID, "newsletter")
    special_offer_v = (By.ID, "optin")
    add_first_name_v = (By.ID, "firstname")
    add_last_name_v = (By.ID, "lastname")
    company_name_v = (By.ID, "company")
    address_line1_v = (By.ID, "address1")
    address_line2_v = (By.ID, "address2")
    city_v = (By.ID, "city")
    state_v = (By.ID, "id_state")
    zip_code_v = (By.ID, "postcode")
    country_v = (By.ID, "id_country")
    additional_info_v = (By.ID, "other")
    home_phone_v = (By.ID, "phone")
    mobile_phone_v = (By.ID, "phone_mobile")
    address_alias_v = (By.ID, "alias")
    register_v = (By.ID, "submitAccount")

    def first_name_m(self):
        return self.driver.find_element(*CreateAnAccountPage.first_name_v)

    def last_name_m(self):
        return self.driver.find_element(*CreateAnAccountPage.last_name_v)

    def password_m(self):
        return self.driver.find_element(*CreateAnAccountPage.password_v)

    def dob_days_m(self):
        return self.driver.find_element(*CreateAnAccountPage.dob_days_v)

    def dob_months_m(self):
        return self.driver.find_element(*CreateAnAccountPage.dob_months_v)

    def dob_years_m(self):
        return self.driver.find_element(*CreateAnAccountPage.dob_years_v)

    def newsletter_sign_m(self):
        return self.driver.find_element(*CreateAnAccountPage.newsletter_sign_v)

    def special_offer_m(self):
        return self.driver.find_element(*CreateAnAccountPage.special_offer_v)

    def add_first_name_m(self):
        return self.driver.find_element(*CreateAnAccountPage.add_first_name_v)

    def add_last_name_m(self):
        return self.driver.find_element(*CreateAnAccountPage.add_last_name_v)

    def company_name_m(self):
        return self.driver.find_element(*CreateAnAccountPage.company_name_v)

    def address_line1_m(self):
        return self.driver.find_element(*CreateAnAccountPage.address_line1_v)

    def address_line2_m(self):
        return self.driver.find_element(*CreateAnAccountPage.address_line2_v)

    def city_m(self):
        return self.driver.find_element(*CreateAnAccountPage.city_v)

    def state_m(self):
        return self.driver.find_element(*CreateAnAccountPage.state_v)

    def zip_code_m(self):
        return self.driver.find_element(*CreateAnAccountPage.zip_code_v)

    def country_m(self):
        return self.driver.find_element(*CreateAnAccountPage.country_v)

    def additional_info_m(self):
        return self.driver.find_element(*CreateAnAccountPage.additional_info_v)

    def home_phone_m(self):
        return self.driver.find_element(*CreateAnAccountPage.home_phone_v)

    def mobile_phone_m(self):
        return self.driver.find_element(*CreateAnAccountPage.mobile_phone_v)

    def address_alias_m(self):
        return self.driver.find_element(*CreateAnAccountPage.address_alias_v)

    def register_m(self):
        return self.driver.find_element(*CreateAnAccountPage.register_v)