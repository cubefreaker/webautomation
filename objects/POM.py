import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, u_name):
        '''Input username for login'''
        driver = self.driver
        a = driver.find_element(By.ID, "login-username")
        a.click()
        a.send_keys(Keys.CONTROL, 'a')
        a.send_keys(u_name)

    def password(self, password):
        driver = self.driver
        a = driver.find_element(By.ID, "login-password")
        a.click()
        a.send_keys(Keys.CONTROL, 'a')
        a.send_keys(password)

    def sign_in(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Welcome Back!'])[1]/following::button[1]").click()

class InvAirline(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Airlines").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()

    def customer(self, customer=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Customer'])[5]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if customer is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__opsions').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(customer)
            a.send_keys(Keys.ENTER)

    def pax_type(self, pax_type):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Type Passenger'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
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
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Title'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
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

    def book_title(self, title):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Title'])[2]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        a.send_keys(title)
        a.send_keys(Keys.ENTER)

    def remarks(self, *remark):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='*For internal use only'])[1]/i[1]").click()
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
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Airline Supplier'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")

        if self.url == "http://opsifin-qa.azurewebsites.net/GN/":
            self.supp = random.choice((['BSP / IATA DOMESTIC', 'BSP / IATA INTERNATIONAL', 'LION AIRLINES (DEPOSIT)', 'CITILINK (DEPOSIT)', 'AIR ASIA (Deposit)', 'SRIWIJAYA AIR (DEPOSIT)', 'XPRESS AIR']))
        elif self.url == "http://opsifin-qa.azurewebsites.net/MNC/":
            self.supp = random.choice((['BSP DOMESTIC', 'BSP INTERNATIONAL', 'LION AIR', 'CITILINK-CORP', 'AIR ASIA', 'SRIWIJAYA AIR', 'XPRESS AIR']))
        else:
            self.supp = random.choice((['BSP / IATA DOMESTIC', 'BSP / IATA INTERNATIONAL', 'LION AIRLINES', 'CITILINK', 'AIR ASIA', 'SRIWIJAYA AIR', 'XPRESS AIR']))

        if supplier is None:
            a.send_keys(self.supp)
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(supplier)
            a.send_keys(Keys.ENTER)

    def flight_type(self, f_type=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Flight Type'])[1]/following::span[5]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        self.ftype = 'International' if self.supp == ('BSP / IATA INTERNATIONAL' or 'BSP INTERNATIONAL') else 'Domestic'
        if f_type is None:
            a.send_keys(self.ftype)
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(f_type)
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
        url = self.url
        def ticketNo(x):
            nonlocal url
            if url == "http://opsifin-qa.azurewebsites.net/GN/":
                if x == 'BSP / IATA INTERNATIONAL':
                    return '12757%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                elif x == 'BSP / IATA DOMESTIC':
                    return '12713%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                elif x == 'LION AIRLINES (DEPOSIT)':
                    return '9902196%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                elif x == 'SRIWIJAYA AIR (DEPOSIT)':
                    return '9771058%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                elif x == 'XPRESS AIR':
                    return '9990006%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                else:
                    return ('')
            elif url == "http://opsifin-qa.azurewebsites.net/MNC/":
                 if x == 'BSP INTERNATIONAL':
                     return '12757%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                 elif x == 'BSP DOMESTIC':
                     return '12713%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                 elif x == 'LION AIR':
                     return '9902196%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                 elif x == 'SRIWIJAYA AIR':
                     return '9771058%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                 elif x == 'XPRESS AIR':
                     return '9990006%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                 else:
                     return ('')
            else:
                if x == 'BSP / IATA INTERNATIONAL':
                    return '12757%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                elif x == 'BSP / IATA DOMESTIC':
                    return '12713%s' % (''.join(random.choice(string.digits) for _ in range(8)))
                elif x == 'LION AIRLINES':
                    return '9902196%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                elif x == 'SRIWIJAYA AIR':
                    return '9771058%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                elif x == 'XPRESS AIR':
                    return '9990006%s' % (''.join(random.choice(string.digits) for _ in range(6)))
                else:
                    return ('')

        tkno = ticketNo(self.supp)
        if tk_no is None:
            a.send_keys(tkno)
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

    def booked_date(self, b_date=None):
        a = self.driver.find_element(By.NAME, 'BookedDate')
        if b_date is None:
            a.clear()
            a.send_keys(self.date)
            a.send_keys(Keys.ENTER)
        else:
            a.clear()
            a.send_keys(b_date)
            a.send_keys(Keys.ENTER)

    def ticket_type(self, t_type):
        self.driver.find_element(By.NAME, 'Class').send_keys(t_type)

    def issuer(self, issuer=None):
        driver = self.driver
        # driver.find_element(By.ID, "select2-Issuer-5c-container").click()
        driver.find_element(By.NAME, 'Class').click()

        act = ActionChains(driver)
        act.send_keys(Keys.TAB)
        act.send_keys(Keys.SPACE)
        act.perform()

        li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
        issuer_name = random.choice(li)
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if issuer is None:
            a.send_keys(issuer_name)
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(issuer)
            a.send_keys(Keys.ENTER)

    # def IssuerList(self):
    #     driver = self.driver
    #     list = driver.find_element(By.XPATH, '//*[@id="select2-Issuer-5c-results"]').text.splitlines()
    #     issuer_name = random.choice(list)
    #     return issuer_name

    def add_route(self):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Route'])[1]/following::button[1]").click()

    def airlines(self, airline=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Airlines'])[2]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if airline is None:
            list = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(list))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(airline)
            a.send_keys(Keys.ENTER)

    def flight_no(self, f_no=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'FlightNo')
        if f_no is None:
            no = ''.join(random.choice(string.digits) for _ in range(3))
            a.click()
            a.send_keys(Keys.SPACE, no)
        else:
            a.click()
            a.send_keys(f_no)

    def f_class(self, Class=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Class'])[1]/following::input[1]")
        if Class is None:
            a.send_keys(random.choice(string.ascii_uppercase))
        else:
            a.send_keys(Class)

    def origin(self, ori=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Origin'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if ori is None:
            a.send_keys('CGK')
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(ori)
            a.send_keys(Keys.ENTER)

    def destination(self, dest=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Destination'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if dest is None:
            if self.ftype == 'Domestic':
                a.send_keys('SUB ')
                a.send_keys(Keys.ENTER)
            else:
                a.send_keys('SIN ')
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

    def save_route(self):
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='ETA'])[1]/following::button[1]").click()

    def base_fare(self, base=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Basic')
        if base is None:
            base = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(3)))
            a.clear()
            a.send_keys(base)
        else:
            a.clear()
            a.send_keys(base)

    def air_tax(self, tax=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'AirTax')
        if tax is None:
            tax = '1%s0000.00' % (random.choice(string.digits))
            a.clear()
            a.send_keys(tax)
        else:
            a.clear()
            a.send_keys(tax)

    def iwjr(self, iwjr=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Iw')
        if iwjr is None:
            iwjr = '%s0000.00' % (random.choice(string.digits))
            a.clear()
            a.send_keys(iwjr)
        else:
            a.clear()
            a.send_keys(iwjr)

    def add_charge(self, charge=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'AddCharge')
        if charge is None:
            charge = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(charge)
        else:
            a.clear()
            a.send_keys(charge)

    def pax_service(self, psc=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Psc')
        if psc is None:
            psc = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(psc)
        else:
            a.clear()
            a.send_keys(psc)

    def insurance(self, ins=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Insurance')
        if ins is None:
            ins = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(ins)
        else:
            a.clear()
            a.send_keys(ins)

    def other(self, other=None):
        driver = self.driver
        a = driver.find_element(By.NAME, 'Other')
        if other is None:
            other = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(other)
        else:
            a.clear()
            a.send_keys(other)

    def markup(self, markup=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Commission Type'])[1]/preceding::span[3]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
        if markup is None:
            li = driver.find_element(By.CLASS_NAME, "select2-results__options").text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(markup)
            a.send_keys(Keys.ENTER)

    def service_fee(self, s_fee=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "PricePolicy")
        if s_fee is None:
            s_fee = '%s0000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
            a.clear()
            a.send_keys(s_fee)
        else:
            a.clear()
            a.send_keys(s_fee)

    def comm_type(self, comm=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Commission Type'])[1]/following::span[3]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
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
                comm = '%s000.00' % (''.join(random.choice(string.digits) for _ in range(2)))
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

    def incentive(self, incentive=None):
        driver = self.driver
        a = driver.find_element(By.NAME, "Incentive")
        if incentive is None:
            incentive = '%s0000.00' % (random.choice(string.digits))
            a.clear()
            a.send_keys(incentive)
        else:
            a.clear()
            a.send_keys(incentive)

    def save_det(self):
        self.driver.find_element(By.ID, "savePax").click()

    def confirm_comm(self):
        self.driver.find_element(By.XPATH, '//*[@id="modal-save"]/div/div/div[3]/a[2]').click()

    def search_pnr(self, pnr=None):
        a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='PNR Code'])[1]/following::input[1]")
        if pnr is None:
            pnr = self.pnr
            a.clear()
            a.send_keys(pnr)
        else:
            a.clear()
            a.send_keys(pnr)

    def clear_date(self):
        self.driver.find_element(By.LINK_TEXT, 'Clear').click()

    def search(self):
        # self.driver.find_element(By.ID, 'BtnSave').click()
        self.driver.find_element(By.ID, 'submitPost').click()

    def select_pnr(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="PostForm"]/div[3]/table/thead/tr/th[1]/div/span/input').click()
        time.sleep(1)

    def create(self):
        self.driver.find_element(By.XPATH, '//*[@id="PostForm"]/div[3]/div/div/button').click()

    # def inv_date(self, date=None):
    #     a = self.driver.find_element(By.ID, "InvDate")
    #     if date is None:
    #         a.clear()
    #         a.send_keys(self.date)
    #         a.send_keys(Keys.ENTER)
    #     else:
    #         a.clear()
    #         a.send_keys(date)
    #         a.send_keys(Keys.ENTER)
    #
    # def division(self, div=None):
    #     a = self.driver.find_element(By.NAME, "Division")
    #     if div is None:
    #         a.send_keys("Division")
    #     else:
    #         a.send_keys(div)
    #
    # def sub_division(self, sub=None):
    #     a = self.driver.find_element(By.NAME, "SubDivision")
    #     if sub is None:
    #         a.send_keys("Sub Division")
    #     else:
    #         a.send_keys(sub)
    #
    # def remark(self, remark=None):
    #     a = self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Remark'])[1]/following::input[1]")
    #     if remark is None:
    #         a.send_keys("Remark")
    #     else:
    #         a.send_keys(remark)
    #
    # def stamp_duty(self, stamp=None):
    #     a = self.driver.find_element(By.NAME, "StampDuty")
    #     if stamp is None:
    #         a.clear()
    #         a.send_keys("5000.00")
    #     else:
    #         a.clear()
    #         a.send_keys(stamp)
    #
    # def discount(self, disc=None):
    #     a = self.driver.find_element(By.NAME, "Disc")
    #     if disc is None:
    #         a.clear()
    #         a.send_keys("10000.00")
    #     else:
    #         a.clear()
    #         a.send_keys(disc)
    #
    # def jurnal_prev(self):
    #     self.driver.find_element(By.ID, "preview").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@id="table-modal-preview"]/div/div/div[3]/div/a').click()
    #
    # def create_inv(self):
    #     time.sleep(2)
    #     self.driver.find_element(By.ID, "submitPost").click()
    #     time.sleep(4)
    #     self.driver.switch_to.window(self.driver.window_handles[0])

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
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Customer'])[8]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[7]/following::input[1]")
        if customer is None:
            li = driver.find_element(By.CLASS_NAME, 'select2-results__opsions').text.splitlines()
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
            time.sleep(1)
            a.send_keys('c')
            time.sleep(1)
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
            self.b_code = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
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

    def create_inv(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "submitPost").click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[0])

class InvInsurance(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Insurance").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()



class InvRentCar(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.LINK_TEXT, "INVOICING").click()
        self.driver.find_element(By.LINK_TEXT, "Rent Car").click()

    def get_url(self, link):
        self.url = link
        return self.url

    def create(self):
        self.driver.find_element(By.LINK_TEXT, 'Create Invoice').click()
        # self.curr_url = self.driver.current_url

    def add(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add").click()

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
        if nett is None:
            pass
        else:
            a.clear()
            a.send_keys(nett)

    def sell_price(self, sell=None):
        a = self.driver.find_element(By.NAME, 'SellPrice')
        if sell is None:
            pass
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

