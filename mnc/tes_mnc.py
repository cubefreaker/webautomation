# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string
from POM import Login, InvAirline, InvCreate
import names
import datetime
from selenium.webdriver.common.action_chains import ActionChains


class InvoicingAirline(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        # self.base_url = "http://opsifin-qa.azurewebsites.net/MNC/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invoicing_airline(self):
        driver = self.driver
        url = "http://opsifin-qa.azurewebsites.net/MNC/"
        driver.get(url)
        time.sleep(1)
        driver.get(url)

        login = Login(driver)
        login.user_name('S2')
        login.password('123456789')
        login.sign_in()

        inv = InvAirline(driver)
        inv.get_url(url)
        inv.add()
        inv.customer('Retail HO')
        inv.pax_type('Adult')
        inv.pax_f_name()
        inv.pax_l_name()
        inv.pax_email()
        inv.pax_title()
        inv.phone()
        inv.h_phone()
        inv.o_phone()
        inv.remarks('Remark 1', 'Remark 2', 'Remark 3', 'Remark 4', 'Remark 5', 'Remark 6')
        inv.supplier()
        inv.flight_type()
        inv.pnr_code()
        inv.ticket_no()
        inv.ticketed_date()
        inv.booked_date()
        inv.issuer()
        inv.add_route()
        inv.airlines()
        inv.flight_no()
        inv.f_class()
        inv.origin()
        inv.dep_date()
        inv.destination()
        inv.arr_date()
        inv.save_route()
        inv.base_fare()
        inv.air_tax()
        inv.iwjr()
        inv.add_charge()
        inv.pax_service()
        inv.insurance()
        inv.other()
        inv.markup()
        inv.service_fee()
        inv.comm_type()
        inv.commission()
        inv.incentive()
        inv.save_det()
        inv.confirm_comm()
        inv.search_pnr()
        inv.clear_date()
        inv.search()
        inv.select_pnr()
        inv.create()
        crt = InvCreate(driver)
        crt.cn_in_to()
        crt.division()
        crt.sub_division()
        crt.remark()
        crt.cn_out_to()
        crt.handler_div()
        crt.handler_iss()
        crt.stamp_duty()
        crt.cn_in()
        crt.cn_out()
        crt.discount()
        crt.jurnal_prev()
        crt.create_inv()


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

