from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, cv2
import os
# from captcha_to_text import image_to_text


def crop_result(result_path):

    image = cv2.imread(result_path)
    image = image[0:1017, 175:840]
    # result_path = "result\\{usn}.png".format(usn = str(usn_list[i]))
    cv2.imwrite(result_path, image)

URL = "https://www.drishtiias.com/free-downloads/ncert-books-chemistry-download"

driver = webdriver.Chrome()
driver.get(URL)
usn_list = open("usn_list.txt", 'r').readlines()
name_list = open("name_list.txt", 'r').readlines()

print(time.ctime())
for i in range(len(usn_list)):
    body_ss = driver.find_element(By.TAG_NAME, "body")
    width = body_ss.size['width']
    height = body_ss.size['height']
    driver.fullscreen_window
    driver.execute_script("document.body.style.zoom='65%'")

    name = name_list[i].rstrip("\n")
    newsletter_elem = driver.find_element(By.NAME, "txtnname")
    newsletter_elem.clear()
    newsletter_elem.send_keys(name)
    usn = usn_list[i].rstrip("\n")
    body_ss.screenshot('result/{usnn}.png'.format(usnn = usn))
    time.sleep(2)
    crop_result('result/{usnn}.png'.format(usnn = usn))
    # driver.refresh()
print(time.ctime())

# time.sleep(6)
driver.close()
