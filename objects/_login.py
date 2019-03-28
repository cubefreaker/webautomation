from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, u_name):
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
