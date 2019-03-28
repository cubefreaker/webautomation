import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

class InvTrain(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Train").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()

    def customer(self, customer=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Customer'])[5]/following::span[4]").click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if customer is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(customer)
            a.send_keys(Keys.ENTER)

    def pax_type(self, pax_type=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[2]/div[1]/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if pax_type is None:
            a.send_keys('Adult')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(pax_type)
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

    def pax_title(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[3]/div[1]/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        title = 'Mr' if self.gen == 'male' else 'Mrs'
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
        else:
            a.send_keys(o_phone)

    def remarks(self, *remark):
        driver = self.driver

        try:
            driver.find_element_by_name("Remark1").click()
        except ElementNotVisibleException:
            driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/i[1]").click

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


    def supplier(self, supplier=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[6]/div[1]/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if supplier is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.clear()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(supplier)
            a.send_keys(Keys.ENTER)

    def pnr_code(self, pnr=None):
        a = self.driver.find_element(By.NAME, "PnrCode")
        if pnr is None:
            self.pnr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            a.send_keys(self.pnr)
        else:
            a.send_keys(pnr)

    def ticket_no(self, tk_no=None):
        a = self.driver.find_element(By.NAME,"TicketNo")
        if tk_no is None:
            pass
        else:
            a.send_keys(tk_no)

    def ticketed_date(self, t_date=None):
        a = self.driver.find_element(By.NAME, 'TicketedDate')
        curr_date = datetime.datetime.now()
        self.date = curr_date.strftime('%d-%m-%Y')
        if t_date is None:
            a.clear()
            a.send_keys(self.date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(t_date)
            a.send_keys(Keys.ENTER)

    def issuer(self, issuer=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[8]/div/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if issuer is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(issuer)
            a.send_keys(Keys.ENTER)

    def train_no(self, no=None):
        a = self.driver.find_element(By.NAME, 'TrainNo')
        if no is None:
            no = 'KA %s' % (''.join(random.choice(string.digits) for _ in range(3)))
            a.clear()
            a.send_keys(no)
        else:
            a.clear()
            a.send_keys('KA %s' % (no))

    def t_class(self, Class=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Class'])[1]/following::input[1]")
        if Class is None:
            Class = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
            a.send_keys(Class)
        else:
            a.send_keys(Class)

    def origin(self, ori=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[10]/div[1]/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if ori is None:
            a.send_keys('PSE')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(ori)
            a.send_keys(Keys.ENTER)

    def destination(self, dest=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[11]/div[1]/div/span[2]/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if dest is None:
            a.send_keys('BD')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(dest)
            a.send_keys(Keys.ENTER)

    def dep_date(self, d_date=None):
        a = self.driver.find_element(By.NAME, 'DepDate')
        if d_date is None:
            a.clear()
            a.send_keys(self.date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(d_date)
            a.send_keys(Keys.ENTER)

    def arr_date(self, arr_date=None):
        a = self.driver.find_element(By.NAME, 'ArrDate')
        if arr_date is None:
            a.clear()
            a.send_keys(self.date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(arr_date)
            a.send_keys(Keys.ENTER)

    def base_fare(self, base=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Basic')
        if base is None:
            base = '1%s00.00' % (''.join(random.choice(string.digits) for _ in range(3)))
            a.clear()
            a.send_keys(base)
        else:
            a.clear()
            a.send_keys(base)

    def service_fee(self, s_fee=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "ServiceFee")
        if s_fee is None:
            s_fee = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(s_fee)
        else:
            a.clear()
            a.send_keys(s_fee)

    def comm_type(self, comm=None):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="modal-add"]/div/div/div[2]/div[12]/div[4]/div/span/span[1]/span').click()
        a = driver.find_element(By.CLASS_NAME, "select2-search__field")
        if comm is None:
            self.comm = driver.find_element(By.CLASS_NAME, "select2-results__options").text.splitlines()
            a.send_keys(random.choice(self.comm))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(comm)
            a.send_keys(Keys.ENTER)

    def commission(self, comm=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "AgentComm")
        if comm is None:
            if self.comm == 'Amount':
                comm = '1%s00.00' % (''.join(random.choice(string.digits) for _ in range(2)))
                a.clear()
                a.send_keys(comm)
            elif self.comm == 'Percent':
                comm = '%s.00' % (random.choice(string.digits))
                a.clear()
                a.send_keys(comm)
            else:
                return
        else:
            a.clear()
            a.send_keys(comm)

    def save_det(self):
        self.driver.find_element(By.ID, "savePax").click()

    def confirm_comm(self):
        self.driver.find_element(By.XPATH, '//*[@id="modal-save"]/div/div/div[3]/a[2]').click()