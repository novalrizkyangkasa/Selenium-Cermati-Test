from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.demoblaze.com')

#1. scroll down page by pixel
#driver.execute_script('window.scrollBy(0,5000)','')

#2. scroll down page until the element is visible (target yg kita cari)
#object = driver.find_element_by_xpath('//*[@id="tbodyid"]/div[9]/div/a/img')
#driver.execute_script('arguments[0].scrollIntoView();',object)

#3. scroll down page until end
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')