from selenium import webdriver

import time

first_name = "Vu Dung"
last_name = "Nguyen"
username = "vudunghalidao201"
password = "vudung201"
phoneNumber = "+12264000462"

url = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"

chromeDriver_location ='..//Bot_autoCreateGoogleAccount//edgeDriver//msedgedriver.exe'

driver = webdriver.Edge(executable_path=chromeDriver_location)

driver.get(url)
time.sleep(2)
driver.find_element_by_id('lastName').send_keys(last_name)
time.sleep(2)
driver.find_element_by_id('firstName').send_keys(first_name)
time.sleep(2)
driver.find_element_by_id('username').send_keys(username)
time.sleep(2)
driver.find_element_by_name('Passwd').send_keys(password)
time.sleep(2)
driver.find_element_by_name('ConfirmPasswd').send_keys(password)
time.sleep(2)
driver.find_element_by_class_name('VfPpkd-muHVFf-bMcfAe').click()
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()
time.sleep(2)
driver.find_element_by_id('phoneNumberId').send_keys(phoneNumber)
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]').click()









