from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from captcha_to_text import image_to_text
from selenium.webdriver.common.alert import Alert

def tries_to_solve(driver, usn):

    for tries in range(1):

        #fetching the USN Element
        usn_elem = driver.find_element(By.XPATH, "//input[@name='lns']")
        #Sending in the USN
        usn_elem.send_keys(usn)
        time.sleep(10)

        #Getting the Captcha and storing it in captcha.png
        captcha_image = driver.find_element(By.XPATH, "//img[@alt='CAPTCHA code']").screenshot_as_png
        image_path = os.path.join(os.getcwd(), "captcha.png")
        with open(image_path, "wb") as image_file:
            image_file.write(captcha_image)

        #Captcha Processing
        captcha_text = image_to_text(image_path)
        driver.implicitly_wait(10)

        #fetching captcha element
        captcha_elem = driver.find_element(By.NAME, "captchacode")
        captcha_elem.click()

        #Sending in the Captcha
        captcha_elem.send_keys(captcha_text)

        #Fetching the Submit Button Element
        submit_button = driver.find_element(By.CLASS_NAME, "form-control.btn-success")
        submit_button.click()
        time.sleep(2)

        #Check the Validation of the Captcha and if there is an Invalid Captcha
        alert_element = Alert(driver).text
        if alert_element != "Invalid captcha code !!!":
            print("Captcha Accepted!")
            time.sleep(5)
        return "Captcha Text"


        # print("Captcha Solving Attempt Failed!")
        # driver.refresh()
    return None
