from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def sgpa_calculator():
    usn_list = open("usn_list.txt", 'r').readlines()
    driver = webdriver.Chrome()
    driver.get("https://www.vtulife.in/vtu-results/JJEcbcs24")

    with open("sgpa_list1.txt", 'w') as sgpa_file:
        for i in range(len(usn_list)):
            usn = usn_list[i].rstrip("\n")
            vl_usn_elem = driver.find_element(By.ID, "id_usn")
            vl_usn_elem.clear()
            vl_usn_elem.send_keys(usn)
            vl_submit_btn = driver.find_element(By.CLASS_NAME, "btn.btn-success.svelte-1k0s61x").click()
            time.sleep(1)
            vl_sgpa = driver.find_element(By.CLASS_NAME, "text-success.fw-bold.svelte-9e3epj")
            sgpa_file.writelines("{}\n".format(vl_sgpa.text))

    driver.close()