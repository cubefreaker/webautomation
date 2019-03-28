import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


class InvCreate(object):

    def __init__(self, driver):
        self.driver = driver

    def inv_date(self, date=None):
        a = self.driver.find_element(By.ID, "InvDate")
        if date is None:
            curr_date = datetime.datetime.now()
            date = curr_date.strftime('%d-%m-%Y')
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

    def due_date(self, date=None):
        a = self.driver.find_element(By.ID, 'DueDate')
        if date is None:
            pass
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

    def customer(self, cust=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Customer Name'])[1]/following::span[3]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[3]/following::input[1]")
        if cust is None:
            a.clear()
            a.send_keys('retail ho')
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(cust)
            a.send_keys(Keys.ENTER)

    def cn_in_to(self, cn=None):
        try:
            elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/label')
        except NoSuchElementException:
            return
        else:
            try:
                assert elem.text == 'Keep Comm In To'
            except AssertionError:
                return
            else:
                self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Keep Comm In To'])[1]/following::span[3]").click()
                a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::input[1]")
                if cn is None:
                    to = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
                    a.send_keys(random.choice(to))
                    a.send_keys(Keys.ENTER)
                else:
                    a.send_keys(cn)
                    a.send_keys(Keys.ENTER)

    def cn_out_to(self, cn=None):
        try:
            elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[4]/div[1]/label')
        except NoSuchElementException:
            return
        else:
            try:
                assert elem.text == 'Keep Comm Out To'
            except AssertionError:
                return
            else:
                self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Keep Comm Out To'])[1]/following::span[3]").click()
                a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::input[1]")
                if cn is None:
                    to = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
                    a.send_keys(random.choice(to))
                    a.send_keys(Keys.ENTER)
                else:
                    a.send_keys(cn)
                    a.send_keys(Keys.ENTER)

    # def handler_div(self, div=None):
    #     try:
    #         elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[4]/div[2]/label')
    #     except NoSuchElementException:
    #         return
    #     else:
    #         try:
    #             assert elem.text == 'Handler Division*'
    #         except AssertionError:
    #             return
    #         else:
    #             self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Head Office'])[2]/following::span[1]").click()
    #             a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::input[1]")
    #             if div is None:
    #                 a.send_keys('Head')
    #                 a.send_keys(Keys.ENTER)
    #             else:
    #                 a.send_keys(div)
    #                 a.send_keys(Keys.ENTER)
    def handler_div(self, div=None):
        self.driver.find_element(By.XPATH, '//*[@title="Head Office"]').click()
        a = self.driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
        if div is None:
            a.send_keys('Head')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(div)
            a.send_keys(Keys.ENTER)

    # def handler_iss(self, iss=None):
    #     try:
    #         elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[4]/div[3]/label')
    #     except NoSuchElementException:
    #         return
    #     else:
    #         try:
    #             assert elem.text == 'Handler Issuer*'
    #         except AssertionError:
    #             return
    #         else:
    #             self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*'])[3]/following::span[3]").click()
    #             time.sleep(0.5)
    #             a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::input[1]")
    #             if iss is None:
    #                 li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
    #                 a.send_keys(random.choice(li))
    #                 a.send_keys(Keys.ENTER)
    #             else:
    #                 a.send_keys(iss)
    #                 a.send_keys(Keys.ENTER)
    def handler_iss(self, iss=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*'])[3]/following::span[3]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[3]/following::input[1]")
        if iss is None:
            li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(iss)
            a.send_keys(Keys.ENTER)

    def division(self, div=None):
        a = self.driver.find_element(By.NAME, "Division")
        if div is None:
            a.send_keys("Division")
        else:
            a.send_keys(div)

    def sub_division(self, sub=None):
        a = self.driver.find_element(By.NAME, "SubDivision")
        if sub is None:
            a.send_keys("Sub Division")
        else:
            a.send_keys(sub)

    def remark(self, remark=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Remark'])[1]/following::input[1]")
        if remark is None:
            a.send_keys("Remark")
        else:
            a.send_keys(remark)

    def stamp_duty(self, stamp=None):
        try:
            sf = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div/div[1]/span')
            assert sf.text == 'Travel Services : 0.00'
        except NoSuchElementException:
            try:
                sf = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/span')
                assert sf.text == 'Travel Services : 0.00'
            except AssertionError:
                a = self.driver.find_element(By.NAME, "StampDuty")
                if stamp is None:
                    a.clear()
                    a.send_keys("5000.00")
                else:
                    a.clear()
                    a.send_keys(stamp)
            else:
                return
        except AssertionError:
            a = self.driver.find_element(By.NAME, "StampDuty")
            if stamp is None:
                a.clear()
                a.send_keys("5000.00")
            else:
                a.clear()
                a.send_keys(stamp)
        else:
            return

    def cn_in(self, cn=None):
        try:
            elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/div[4]/label')
        except NoSuchElementException:
            return
        else:
            try:
                assert elem.text == 'CN In'
            except AssertionError:
                return
            else:
                a = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/div[4]/input')
                if cn is None:
                    cn = '%s000.00'.join(random.choice(string.digits))
                    a.clear()
                    a.send_keys(cn)
                else:
                    a.clear()
                    a.send_keys(cn)

    def cn_out(self, cn=None):
        try:
            elem = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/div[5]/label')
        except NoSuchElementException:
            return
        else:
            try:
                assert elem.text == 'CN Out'
            except AssertionError:
                return
            else:
                a = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[3]/div[5]/input')
                if cn is None:
                    cn = '%s000.00'.join(random.choice(string.digits))
                    a.clear()
                    a.send_keys(cn)
                else:
                    a.clear()
                    a.send_keys(cn)

    def discount(self, disc=None):
        try:
            sf = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div/div[1]/span')
            assert sf.text == 'Travel Services : 0.00'
        except NoSuchElementException:
            try:
                sf = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div/div[1]/span')
                assert sf.text == 'Travel Services : 0.00'
            except AssertionError:
                a = self.driver.find_element(By.NAME, "Disc")
                if disc is None:
                    a.clear()
                    a.send_keys("10000.00")
                else:
                    a.clear()
                    a.send_keys(disc)
            else:
                return
        except AssertionError:
            a = self.driver.find_element(By.NAME, "Disc")
            if disc is None:
                a.clear()
                a.send_keys("10000.00")
            else:
                a.clear()
                a.send_keys(disc)
        else:
            return

    def jurnal_prev(self):
        self.driver.find_element(By.ID, "preview").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'close').click()

    def jurnal_prev_open(self):
        self.driver.find_element(By.ID, "preview").click()

    def create_inv(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "submitPost").click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[0])
