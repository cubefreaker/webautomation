# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string
from models._login import Login
from models._hotel_det import InvHotel
import names
import datetime
from selenium.webdriver.common.action_chains import ActionChains


class InvoicingHotel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ASUS/Dropbox/project/Python/selenium/Opsifin/Opsifin - POM/opsifin-venv/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        # self.base_url = "http://opsifin-qa.azurewebsites.net/MNC/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invoicing_hotel(self):
        driver = self.driver
        url = "http://globalwisata.opsifin.com/"
        driver.get(url)
        time.sleep(1)
        driver.get(url)

        login = Login(driver)
        login.user_name('S2')
        login.password('987654321')
        login.sign_in()

        inv = InvHotel(driver)
        inv.get_url(url)
        def run():
            inv.add()
            inv.customer()
            inv.add_guest()
            inv.pax_type('Adult')
            inv.pax_f_name()
            inv.pax_l_name()
            inv.pax_email()
            inv.pax_title()
            inv.phone()
            inv.h_phone()
            inv.o_phone()
            inv.remarks('Remark 1', 'Remark 2', 'Remark 3', 'Remark 4', 'Remark 5', 'Remark 6')
            inv.pax_save()
            inv.source()
            inv.res_code()
            inv.ref_code()
            inv.type()
            inv.country()
            inv.city()
            inv.hotel()
            inv.bed_type()
            inv.room_type()
            inv.meals()
            inv.request()
            inv.check_in()
            inv.check_out()
            inv.issuedate()
            inv.issuer()
            inv.booking_code()
            inv.voucher_no()
            inv.guest_country()
            inv.room_total()
            inv.room_rate()
            inv.service_type()
            inv.service_fee()
            inv.save_det()
        run()
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

