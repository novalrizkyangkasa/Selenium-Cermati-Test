from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("pegipegi")
driver.find_element_by_name("btnK").click()

driver.close()
driver.quit()