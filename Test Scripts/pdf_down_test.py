# import urllib.request
# import requests
URL = "https://www.drishtiias.com/free-downloads/ncert-books-chemistry-download"

# response = urllib.request.urlopen(URL)    
# file = open("FILENAME.pdf", 'wb')
# file.write(response.read())
# file.close()
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "E:\\VS Code_Dec\\Scraping\\using_Selenium\\pdf\\", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})

pdf = webdriver.Chrome(options=options)
print(time.ctime(time.time()))
pdf_url = "https://www.drishtiias.com/images/pdf/NCERT-Class-11-Chemistry-Part-1.pdf"

pdf.get(URL)
for i in range(0,2):

    pdf.refresh()
    elem = pdf.find_element(By.ID, "txtnname")
    pdf_elem = pdf.find_element(By.XPATH, "//a[@href='{URL1}']".format(URL1 = pdf_url))

    # print(pdf_elem.text)
    elem.send_keys("Atharv")
    pdf_elem.click()
print(time.ctime(time.time()))

time.sleep(5)
pdf.close()