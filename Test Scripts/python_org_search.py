from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://example.com/")
driver.get("https://byjus.com/ncert-books/#ncert-books-class-12")
title = driver.title
driver.implicitly_wait(1)

# button_link = driver.find_element(by=By.LINK_TEXT, value="More information...")

box =  driver.find_element(by=By.CSS_SELECTOR, value=".table.table-bordered tbody")
box_click = box.find_element(by=By.LINK_TEXT, value="NCERT Books for Class 12 Maths")

print(box_click.text)
box_click.click()

# download_pdf.click()
driver.quit()

