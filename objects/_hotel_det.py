import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


class InvHotel(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Hotel").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()

    def customer(self, customer=None):
        driver = self.driver
        time.sleep(0.5)
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Customer'])[8]/following::span[4]").click()
        time.sleep(0.5)
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if customer is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(customer)
            a.send_keys(Keys.ENTER)

    def add_guest(self):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Address'])[2]/following::button[1]").click()

    def pax_type(self, pax_type):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Category'])[2]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        a.send_keys(pax_type)
        a.send_keys(Keys.ENTER)

    def pax_f_name(self, f_name=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='First Name'])[1]/following::input[1]")
        self.gen = random.choice(['male', 'female'])
        self.fname = names.get_first_name(gender = self.gen)
        if f_name is None:
            a.send_keys(self.fname)
        else:
            a.send_keys(f_name)

    def pax_l_name(self, l_name=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Last Name'])[1]/following::input[1]")
        self.lname = names.get_last_name()
        if l_name is None:
            a.send_keys(self.lname)
        else:
            a.send_keys(l_name)

    def pax_email(self, email=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Email'])[1]/following::input[1]")
        mail = '%s.%s@gmail.com' % (self.fname.lower(), self.lname.lower())
        if email is None:
            a.send_keys(mail)
        else:
            a.send_keys(email)

    def pax_title(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Title'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        title = 'Mr' if self.gen == 'male' else 'Mrs'
        a.send_keys(title)
        a.send_keys(Keys.ENTER)

    def phone(self, m_phone=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Mobile Phone'])[1]/following::input[1]")
        if m_phone is None:
            self.mphone = '08%s' % (''.join(random.choice(string.digits) for _ in range(9)))
            a.send_keys(self.mphone)
        else:
            a.send_keys(m_phone)

    def h_phone(self, h_phone=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Home Phone'])[1]/following::input[1]")
        if h_phone is None:
            self.hphone = '0%s' % (''.join(random.choice(string.digits) for _ in range(9)))
            a.send_keys(self.hphone)
        else:
            a.send_keys(h_phone)

    def o_phone(self, o_phone=None):
        driver = self.driver
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Other Phone'])[1]/following::input[1]")
        if o_phone is None:
            a.send_keys(random.choice(([self.mphone, self.hphone, '-'])))
        else:
            a.send_keys(o_phone)

    def remarks(self, *remark):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/i[1]").click()
        li = []
        for i in remark:
            li.append(i)

        remark1 = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::input[1]")
        remark2 = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::input[2]")
        remark3 = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::input[3]")
        remark4 = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::input[4]")
        remark5 = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::input[5]")

        remark1.send_keys(li[0])
        remark2.send_keys(li[1])
        remark3.send_keys(li[2])
        remark4.send_keys(li[3])
        remark5.send_keys(li[4])

    def pax_save(self):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/following::button[1]").click()
        time.sleep(1)

    def source(self, src=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Source'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if src is None:
            a.send_keys("MG HOLIDAY")
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(src)
            a.send_keys(Keys.ENTER)

    def res_code(self, res=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Source Res Code'])[2]/following::input[1]")
        if res is None:
            code = ''.join(random.choice(string.digits) for _ in range(10))
            a.send_keys(code)
        else:
            a.send_keys(res)

    def ref_code(self, ref=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Source Reference'])[2]/following::input[1]")
        if ref is None:
            code = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
            a.send_keys(code)
        else:
            a.send_keys(ref)

    def type(self, type=None):
        self.type = type
        if type is None:
            pass
        else:
            self.driver.find_element(By.ID, "select2-j3cm-container").click()
            a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
            a.send_keys(type)
            a.send_keys(Keys.ENTER)

    def country(self, country=None):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Country'])[1]/following::span[4]").click()
        time.sleep(1)
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if self.type is None or self.type.lower() == 'domestic':
            a.send_keys("Indonesia")
            a.send_keys(Keys.ENTER)
        else:
            if country is None:
                li = self.driver.find_element(By.CLASS_NAME, "select2-results__options").text.splitlines()
                a.send_keys(random.choice(li))
                a.send_keys(Keys.ENTER)
            else:
                a.send_keys(country)
                a.send_keys(Keys.ENTER)

    def city(self, city=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='City'])[3]/following::input[1]")
        a.click()
        if city is None:
            if self.type is None or self.type.lower() == 'domestic':
                a.clear()
                a.send_keys('j')
                time.sleep(0.5)
                a.send_keys('a')
                time.sleep(0.5)
                a.send_keys('k')
                time.sleep(1)
                a.send_keys(Keys.TAB)
            else:
                a.clear()
                a.send_keys('a')
                time.sleep(1)
                a.send_keys(Keys.TAB)
        else:
            a.send_keys(city)
            time.sleep(1)
            a.send_keys(Keys.TAB)

    def hotel(self, hotel=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Hotel'])[2]/following::input[1]")
        a.click()
        if hotel is None:
            a.clear()
            a.send_keys('a')
            time.sleep(1.5)
            a.send_keys('c')
            time.sleep(1.5)
            a.send_keys(Keys.TAB)
        else:
            a.clear()
            a.send_keys(hotel)
            time.sleep(1)
            a.send_keys(Keys.TAB)

    def bed_type(self, bed=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Bed Type'])[2]/following::span[4]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if bed is None:
            li = self.driver.find_element(By.CLASS_NAME, "select2-results__options").text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(bed)
            a.send_keys(Keys.ENTER)

    def room_type(self, room=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Room Type'])[2]/following::input[1]")
        if room is None:
            a.send_keys('STANDARD')
        else:
            a.send_keys(room)

    def meals(self, status=None):
        if status is None:
            self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Meals'])[1]/following::label[2]").click()
        else:
            if status == 'N':
                self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Meals'])[1]/following::label[2]").click()
            else:
                self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Meals'])[1]/following::label[1]").click()

    def meals_det(self, det=None):
        a = self.driver.find_element(By.XPATH, '//*[@id="modal-view"]/div/div/div[2]/div[11]/div[3]/div/input')
        if det is None:
            pass
        else:
            a.clear()
            a.send_keys(det)

    def request(self, req=None):
        a = self.driver.find_element(By.XPATH, '//*[@id="modal-view"]/div/div/div[2]/div[11]/div[4]/div/input')
        if req is None:
            a.send_keys('a request')
        else:
            a.send_keys(req)

    def check_in(self, date=None):
         a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Check In'])[1]/following::input[1]")
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

    def check_out(self, date=None):
        a = self.driver.find_element(By.NAME, 'CheckOut')
        if date is None:
            date1 = datetime.datetime.now() + datetime.timedelta(days=1)
            date = date1.strftime('%d-%m-%Y')
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

    def issuedate(self, date=None):
        a = self.driver.find_element(By.XPATH, '//*[@id="modal-view"]/div/div/div[2]/div[12]/div[3]/div/input')
        if date is None:
            a.clear()
            a.send_keys(self.date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(date)
            a.send_keys(Keys.ENTER)

    def issuer(self, issuer=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Issuer'])[2]/following::span[4]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if issuer is None:
            li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            issuer_name = random.choice(li)
            a.send_keys(issuer_name)
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(issuer)
            a.send_keys(Keys.ENTER)

    def booking_code(self, b_code=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Booking Code'])[5]/following::input[1]")
        if b_code is None:
            self.b_code = 'MG%s' % (''.join(random.choice(string.ascii_uppercase) for _ in range(6)))
            a.clear()
            a.send_keys(self.b_code)
        else:
            a.clear()
            a.send_keys(b_code)

    def voucher_no(self, no=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Voucher Number'])[1]/following::input[1]")
        if no is None:
            self.no = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(13))
            a.clear()
            a.send_keys(self.no)
        else:
            a.clear()
            a.send_keys(no)

    def guest_country(self, guest=None):
        self.driver.find_element(By.XPATH, '//*[@id="modal-view"]/div/div/div[2]/div[13]/div[4]/div/span[2]/span[1]/span').click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if guest is None:
            li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            guest = random.choice(li)
            a.send_keys(guest)
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(guest)
            a.send_keys(Keys.ENTER)

    def room_total(self, total=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Total Room'])[2]/following::input[1]")
        if total is None:
            pass
        else:
            a.clear()
            a.send_keys(total)

    def room_rate(self, rate=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Rate per Night'])[2]/following::input[1]")
        if rate is None:
            rate = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(3)))
            a.clear()
            a.send_keys(rate)
        else:
            a.clear()
            a.send_keys(rate)

    def service_type(self, s_type=None):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Travel Services Type'])[1]/following::span[3]").click()
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if s_type is None:
            li = self.driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            self.s_type = random.choice(li)
            a.send_keys(self.s_type)
            a.send_keys(Keys.ENTER)
        else:
            self.s_type = s_type
            a.send_keys(s_type)
            a.send_keys(Keys.ENTER)

    def service_fee(self, s_fee=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Travel Services'])[2]/following::input[1]")
        self.s_fee_p = '%s.00' % (random.choice(string.digits))
        self.s_fee_a = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
        if s_fee is None:
            if self.s_type.lower() == 'percent':
                a.clear()
                a.send_keys(self.s_fee_p)
            elif self.s_type.lower() == 'amount':
                a.clear()
                a.send_keys(self.s_fee_a)
            else:
                pass
        else:
            if self.s_type == '-':
                pass
            else:
                a.clear()
                a.send_keys(s_fee)

    def save_det(self):
        self.driver.find_element(By.ID, "savePax").click()

    def search_booking(self, book=None):
        a = self.driver.find_element(By.XPATH, '//*[@id="BeforeCreate"]/div/div[1]/div[2]/div/input')
        if book is None:
            book = self.b_code
            a.clear()
            a.send_keys(book)
        else:
            a.clear()
            a.send_keys(book)

    def clear_date(self):
        self.driver.find_element(By.LINK_TEXT, 'Clear').click()

    def search(self):
        # self.driver.find_element(By.ID, 'BtnSave').click()
        self.driver.find_element(By.ID, 'submitPost').click()

    def select_booking(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="PostForm"]/div[3]/table/thead/tr/th[1]/div/span/input').click()
        time.sleep(1)

    def create(self):
        self.driver.find_element(By.XPATH, '//*[@id="PostForm"]/div[3]/div/div/button').click()
