from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException

class CheckPrev(object):

    def __init__(self, driver):
        self.driver = driver

    def tbl_prev(self):
        self.journal = []
        for i in range(1, 1001):
            try:
                a = self.driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0"]/tbody/tr[%s]' % (i))
            except NoSuchElementException:
                break
            else:
                prev = a.text.split()
                prev[2:prev.index('InvNo')] = [' '.join(prev[2:prev.index('InvNo')])]
                prev[(1 + prev.index('InvNo')):-3] = [' '.join(prev[(1 + prev.index('InvNo')):-3])]
                self.journal.append(prev)
                i =+ 1
        print('\n'.join(map(str, self.journal)))

    def present(self, present):

        for x in range(0, len(self.journal)):
            try:
                pos = self.journal[x].index(present)
                break
            except:
                pass
        try:
            pos
            print('%s Oke..' % (present))
        except:
            print('Journal %s not present' % (present))

    # def check_coa(self):
    #
    #
    #     for x in range(0, len(self.prev)):
    #         for y in range(0, len(self.prev[x]):
    #             present(self.prev[x][y])
    #
