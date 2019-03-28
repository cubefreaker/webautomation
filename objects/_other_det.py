import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


class InvOther(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Other").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def create(self):
        self.driver.find_element(By.LINK_TEXT, 'Create Invoice').click()

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()

    def pax_f_name(self, f_name=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "FirstName")
        self.gen = random.choice(['male', 'female'])
        self.fname = names.get_first_name(gender = self.gen)
        if f_name is None:
            a.send_keys(self.fname)
        else:
            a.send_keys(f_name)

    def pax_l_name(self, l_name=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "LastName")
        self.lname = names.get_last_name()
        if l_name is None:
            a.send_keys(self.lname)
        else:
            a.send_keys(l_name)

    def pax_email(self, email=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "Email")
        mail = '%s.%s@gmail.com' % (self.fname.lower(), self.lname.lower())
        if email is None:
            a.send_keys(mail)
        else:
            a.send_keys(email)

    def pax_title(self, title=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Title'])[1]/following::span[4]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[3]/following::input[1]")
        if title is None:
            title = 'Mr' if self.gen == 'male' else 'Mrs'
            a.clear()
            a.send_keys(title)
            a.send_keys(Keys.ENTER)
        else:
            a.clear
            a.send_keys(title)
            a.send_keys(Keys.ENTER)

    def phone(self, m_phone=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "MobilePhone")
        if m_phone is None:
            self.mphone = '08%s' % (''.join(random.choice(string.digits) for _ in range(9)))
            a.send_keys(self.mphone)
        else:
            a.send_keys(m_phone)

    def h_phone(self, h_phone=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "HomePhone")
        if h_phone is None:
            self.hphone = '0%s' % (''.join(random.choice(string.digits) for _ in range(9)))
            a.send_keys(self.hphone)
        else:
            a.send_keys(h_phone)

    def o_phone(self, o_phone=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "OtherPhone")
        if o_phone is None:
            a.send_keys(random.choice(([self.mphone, self.hphone, '-'])))

    def remarks(self, *remark):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, '*For internal use only').click()
        li = []
        for i in remark:
            li.append(i)

        remark1 = driver.find_element_by_name("Remark1")
        remark2 = driver.find_element_by_name("Remark2")
        remark3 = driver.find_element_by_name("Remark3")
        remark4 = driver.find_element_by_name("Remark4")
        remark5 = driver.find_element_by_name("Remark5")
        remark6 = driver.find_element_by_name("Remark6")

        remark1.send_keys(li[0])
        remark2.send_keys(li[1])
        remark3.send_keys(li[2])
        remark4.send_keys(li[3])
        remark5.send_keys(li[4])
        remark6.send_keys(li[5])

    def supplier(self, supp=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Supplier'])[2]/following::span[3]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[3]/following::input[1]")
        if supp is None:
            a.clear()
            a.send_keys('others')
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(supp)
            a.send_keys(Keys.ENTER)

    def booking_no(self, no=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Booking Number'])[1]/following::input[1]")
        if no is None:
            no = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(6))
            a.clear()
            a.send_keys(no)
        else:
            a.clear()
            a.send_keys(no)

    def product(self, produk=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Product'])[1]/following::span[4]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[3]/following::input[1]")
        if produk is None:
            a.clear()
            a.send_keys('other')
            time.sleep(0.5)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(produk)
            a.send_keys(Keys.ENTER)

    def date(self, date=None):
        a = self.driver.find_element(By.XPATH, '//*[@id="modal-view"]/div/div/div[2]/div[13]/div[2]/div/input')
        curr_date = datetime.datetime.now()
        self.date = curr_date.strftime('%d-%m-%Y')
        if date is None:
            date = self.date
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

    def location(self, loc=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Location'])[1]/following::input[1]")
        if loc is None:
            a.send_keys('Jakarta')
        else:
            a.send_keys(loc)

    def description(self, desc=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::textarea[1]")
        if desc is None:
            a.send_keys('Lorem ipsum dolor sit amet consectetuer')
        else:
            a.send_keys(desc)

    def nett_price(self, nett=None):
        a = self.driver.find_element(By.NAME, 'NettPrice')
        self.nett = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(3)))
        if nett is None:
            nett = self.nett
            a.clear()
            a.send_keys(nett)
        else:
            a.clear()
            a.send_keys(nett)

    def sell_price(self, sell=None):
        a = self.driver.find_element(By.NAME, 'SellPrice')
        if sell is None:
            sell = int(self.nett) + ('20000')
            a.clear()
            a.send_keys(str(sell))
        else:
            a.clear()
            a.send_keys(sell)

    def quantity(self, qty=None):
        a = self.driver.find_element(By.NAME, 'Qty')
        if qty is None:
            a.clear()
            a.send_keys('1')
        else:
            a.clear()
            a.send_keys(qty)

    def unit(self, unit=None):
        a = self.driver.find_element(By.NAME, 'UnitPrice')
        if unit is None:
            a.clear()
            a.send_keys('1')
        else:
            a.clear()
            a.send_keys(unit)

    def save_det(self):
        self.driver.find_element(By.LINK_TEXT, 'Save').click()

