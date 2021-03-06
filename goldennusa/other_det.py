# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string
from objects._login import Login
from objects._other_det import InvOther
import names
import datetime
from selenium.webdriver.common.action_chains import ActionChains


class InvoicingAirline(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ASUS/Dropbox/project/Python/selenium/Opsifin/Opsifin - POM/opsifin-venv/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        # self.base_url = "http://opsifin-qa.azurewebsites.net/GN/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invoicing_airline(self):
        driver = self.driver
        url = "http://opsifin-qa.azurewebsites.net/GN/"
        # driver.get(url)
        time.sleep(1)
        driver.get(url)

        login = Login(driver)
        login.user_name('S2')
        login.password('987654321')
        login.sign_in()

        inv = InvOther(driver)
        inv.get_url(url)
        inv.create()
        def run():
            inv.add()
            inv.pax_f_name()
            inv.pax_l_name()
            inv.pax_email()
            inv.pax_title()
            inv.phone()
            inv.h_phone()
            inv.o_phone()
            inv.remarks('Remark 1', 'Remark 2', 'Remark 3', 'Remark 4', 'Remark 5', 'Remark 6')
            inv.supplier('zur')
            inv.booking_no()
            inv.product('in')
            inv.date()
            inv.location()
            inv.description()
            inv.nett_price()
            inv.sell_price()
            inv.quantity()
            inv.unit()
            inv.save_det()
        for i in range(3):
            run()
            i += 1
            time.sleep(1)



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

