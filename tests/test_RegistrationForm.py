import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.CreateAnAccountPage import CreateAnAccountPage
from PageObjects.HomePage import HomePage
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_register_all_details(self):
        log = self.getLogger()
        home_page_t = HomePage(self.driver)
        home_page_t.sign_in_m().click()

        sign_in_page_t = SignInPage(self.driver)
        sign_in_page_t.email_create_m().send_keys("aniket1234fdf32334456@cmail.com")
        log.info("Entering the email address")
        sign_in_page_t.create_an_account_m().click()
        log.info("Clicking on create account")

        log.info("Entering the required information to create the account")
        create_an_account_page_t = CreateAnAccountPage(self.driver)
        create_an_account_page_t.first_name_m().send_keys("Aniket")
        create_an_account_page_t.last_name_m().send_keys("Shinde")
        create_an_account_page_t.password_m().send_keys("abc123")

        self.select_option_by_value(create_an_account_page_t.dob_days_m(), "6")
        self.select_option_by_value(create_an_account_page_t.dob_months_m(), "7")
        self.select_option_by_value(create_an_account_page_t.dob_years_m(), "1994")

        create_an_account_page_t.newsletter_sign_m().click()
        create_an_account_page_t.special_offer_m().click()
        create_an_account_page_t.add_first_name_m().send_keys("Abc")
        create_an_account_page_t.add_last_name_m().send_keys("xyz")
        create_an_account_page_t.company_name_m().send_keys("Visma")
        create_an_account_page_t.address_line1_m().send_keys("apartment 1301,Sandyford Point")
        create_an_account_page_t.address_line2_m().send_keys("Rockfield, Dublin")
        create_an_account_page_t.city_m().send_keys("Dublin")
        self.select_option_by_text(create_an_account_page_t.state_m(), "Missouri")
        create_an_account_page_t.zip_code_m().send_keys("11111")
        self.select_option_by_value(create_an_account_page_t.state_m(), "21")
        create_an_account_page_t.additional_info_m().send_keys("NA")
        create_an_account_page_t.home_phone_m().send_keys("1234567")
        create_an_account_page_t.mobile_phone_m().send_keys("987654321")
        create_an_account_page_t.address_alias_m().send_keys("near river")
        create_an_account_page_t.register_m().click()
        self.check_successfully_my_account_page()








