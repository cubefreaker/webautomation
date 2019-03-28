import time
import names
import datetime
import random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains


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
            li = driver.find_element(By.CLASS_NAME, 'select2-results__options').text.splitlines()
            a.send_keys(random.choice(li))
            a.send_keys(Keys.ENTER)
        else:
            a.send_keys(customer)
            a.send_keys(Keys.ENTER)

    def pax_type(self, pax_type=None):
        driver = self.driver
        driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Type Passenger'])[1]/following::span[4]").click()
        a = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[14]/following::input[1]")
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
            self.supp = random.choice((['BSP / IATA DOMESTIC', 'BSP / IATA INTERNATIONAL', 'GARUDA INDONESIA', 'LION AIRLINES', 'CITILINK', 'AIR ASIA', 'SRIWIJAYA AIR', 'XPRESS AIR']))

        if supplier is None:
            a.send_keys(self.supp)
            a.send_keys(Keys.ENTER)
        else:
            self.supp = supplier
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
                elif x == 'GARUDA':
                    return '12715%s' % (''.join(random.choice(string.digits) for _ in range(8)))
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

    def issued_lg(self, lg=None):
        self.driver.find_element(By.ID, 'select2-IssuedWithLg-tx-container').click()
        a = self.driver.find_element(By.CLASS_NAME, 'select2-search__field')
        if lg is None:
            pass
        else:
            a.send_keys(lg)
            a.send_keys(Keys.ENTER)

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
        a = driver.find_element(By.NAME, "TravelService")
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
