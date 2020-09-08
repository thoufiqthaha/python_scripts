import selenium
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def ibmc(ip):

    for host in ip:

        # Using Chrome to access web
        driver = webdriver.Chrome()
        # Open a new window
        driver.execute_script("window.open('');")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])

        # Open the website
        driver.get('https://%s'%(host))
        driver.maximize_window()
        
        #pass cert warning page
        driver.find_element_by_id('details-button').click()
        driver.find_element_by_id('proceed-link').click()


        # Select the id box
        id_box = driver.find_element_by_id('iptUserName')

        # Send id information
        id_box.send_keys('root')

        # Find password box
        pass_box = driver.find_element_by_id('iptPassword')
        # Send password
        pass_box.send_keys('lYwXtSnPvlI7')
        # Find login button
        login_button = driver.find_element_by_id('btnLogin')
        # Click login
        login_button.click()


        # Moving to actual path
        config = driver.find_element_by_id('menu_CONFIGURATION')
        driver.execute_script("arguments[0].click();", config)
        time.sleep(1)


        system = driver.find_element_by_id('menu_SYSTEM_ENTRY')
        driver.execute_script("arguments[0].click();", system)
        time.sleep(1)



        # Modifying the required values
        driver.switch_to_frame("rightMid")
        v2c = driver.find_element_by_id('v2c')
        v2c.click()
        time.sleep(1)

        comm = driver.find_element_by_id('roGroup')
        comm.send_keys("public")
        time.sleep(1)

        recomm = driver.find_element_by_id('roGroupConfirm')
        recomm.send_keys("public")
        time.sleep(1)


        # Clicking Save
        save = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "saveSnmpSet")))
        print("Gonna save")
        driver.execute_script("arguments[0].click();", save)


        driver.switch_to_default_content()
        ok = driver.find_element_by_id('btnDialogOK')
        ok.click()

        time.sleep(1)
        print("Saved")

        print ("%s completed"%(host))
        

#driver.quit()

ipadd = ["172.23.6.100","172.23.5.179"]

ibmc(ipadd)
