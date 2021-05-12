from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://www.cermati.com/gabung')

driver.find_element_by_id('email').send_keys('novalangkasa@yahoo.com')
time.sleep(2)
driver.find_element_by_id('password').send_keys('@Secretmenu25')
time.sleep(2)
driver.find_element_by_id('confirm-password').send_keys('@Secretmenu25')
time.sleep(2)
driver.find_element_by_id('first-name').send_keys('Mochammad Naufal')
time.sleep(2)
driver.find_element_by_id('last-name').send_keys('Rizky Angkasa')
time.sleep(2)
driver.find_element_by_id('mobile-phone').send_keys('085733502223')
time.sleep(2)
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Kota']").send_keys('Kota Mojoker')
time.sleep(4)

elementXpath = driver.find_element_by_xpath('//*[@id="join-container"]/div/div/div[2]/div/div[7]/div/div[2]/div/div').click()

elementXpath = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/div[9]/button').click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")