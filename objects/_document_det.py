import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

class InvDocument(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "SOURCE FILE").click()
        self.driver.find_element(By.LINK_TEXT, "Document Receipt").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def create(self):
        self.driver.find_element(By.LINK_TEXT, 'Create').click()

    def r_date(self, date=None):
        a = self.driver.find_element(By.NAME, 'StartDate')
        if date is None:
            pass
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

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
        self.driver.find_element(By.XPATH, '//*[@id="formDocumentReceipt"]/div/div/div/div[3]/div[1]/div/span[2]/span[1]/span').click()
        a = self.driver.find_element(By.CLASS_NAME, "select2-search__field")
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
        li = []
        for i in remark:
            li.append(i)

        remark1 = driver.find_element_by_name("Remarks1")
        remark2 = driver.find_element_by_name("Remarks2")

        remark1.send_keys(li[0])
        remark2.send_keys(li[1])

    def supplier(self, supp=None):
        self.driver.find_element(By.XPATH, '//*[@id="formDocumentReceipt"]/div/div/div/div[6]/div[1]/span/span[1]/span').click()
        a = self.driver.find_element(By.CLASS_NAME, 'select2-search__field')
        if supp is None:
            li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(supp)
            a.send_keys(Keys.ENTER)

    def r_type(self, type=None):
        self.driver.find_element(By.XPATH, '//*[@id="formDocumentReceipt"]/div/div/div/div[11]/div[1]/span/span[1]/span').click()
        a = self.driver.find_element(By.CLASS_NAME, 'select2-search__field')
        if type is None:
            a.send_keys('Corp')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(type)
            a.send_keys(Keys.ENTER)

    def customer(self, cust=None):
        a = self.driver.find_element(By.NAME, 'CustomerName')
        if cust is None:
            a.send_keys('Retail Ho')
        else:
            a.send_keys(cust)
