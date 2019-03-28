# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, string
from models._login import Login
from models._train_det import InvTrain
import names
import datetime
from selenium.webdriver.common.action_chains import ActionChains


class InvoicingTrain(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ASUS/Dropbox/project/Python/selenium/Opsifin/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://globalwisata.opsifin.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invoicing_train(self):
        driver = self.driver
        url = "http://globalwisata.opsifin.com/"
        driver.get(url)
        time.sleep(1)
        driver.get(url)

        login = Login(driver)
        login.user_name('S2')
        login.password('987654321')
        login.sign_in()
        inv = InvTrain(driver)
        inv.get_url(url)
        def run():
            inv.add()
            time.sleep(0.5)
            inv.customer()
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
            inv.pnr_code()
            inv.ticket_no()
            inv.ticketed_date()
            inv.issuer()
            inv.train_no()
            inv.t_class()
            inv.origin()
            inv.dep_date()
            inv.destination()
            inv.arr_date()
            inv.base_fare()
            inv.service_fee()
            inv.comm_type()
            inv.commission()
            inv.save_det()
            time.sleep(0.5)
            inv.confirm_comm()
        run()
        # for i in range(10):
        #     run()
        #     i += 1
        #     time.sleep(1)
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

