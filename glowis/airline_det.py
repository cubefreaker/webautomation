# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string
from models._login import Login
from models._airline_det import InvAirline
from models._create_inv import InvCreate
from models._check_journal_prev import CheckPrev
import names
import datetime
import random
from selenium.webdriver.common.action_chains import ActionChains


class InvoicingAirline(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ASUS/Dropbox/project/Python/selenium/Opsifin/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://globalwisata.opsifin.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invoicing_airline(self):
        driver = self.driver
        url = "http://globalwisata.opsifin.com/"
        driver.get(url)
        time.sleep(1)
        driver.get(url)

        login = Login(driver)
        login.user_name('S2')
        login.password('987654321')
        login.sign_in()
        inv = InvAirline(driver)
        inv.get_url(url)
        crt = InvCreate(driver)
        prev = CheckPrev(driver)
        def run():
            inv.add()
            time.sleep(0.5)
            inv.customer('4li')
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
            time.sleep(0.5)
            # def sched():
            #     dateSTR = datetime.datetime.now().strftime("%H:%M:%S")
            #     while dateSTR != ('14:46:30'):
            #         print(dateSTR)
            #         time.sleep(1)
            #         dateSTR = datetime.datetime.now().strftime("%H:%M:%S")
            # sched()
            inv.confirm_comm()
            # inv.search_pnr()
            # inv.clear_date()
            # inv.search()
            # inv.select_pnr()
            # inv.create()
            # crt.jurnal_prev_open()
            # prev.tbl_prev()
            # prev.present('5100010001')
            # prev.present('1100170002')
            # prev.present('1100100001')
            # prev.present('4100070001')
            # prev.present('1100050001')
            # prev.present('4100010001')
            # prev.present('2100130001')
        for i in range(2):
            run()
            i += 1
            time.sleep(1)
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

