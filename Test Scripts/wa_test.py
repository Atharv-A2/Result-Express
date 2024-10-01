from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(30)
elem = driver.find_element(By.CLASS_NAME, "_ak8q")
print(elem.text())

driver.close()