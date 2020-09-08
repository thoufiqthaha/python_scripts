import selenium
from selenium import webdriver
import time

#driver = webdriver.Chrome(executable_path='/chromedriver.exe')

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://10.93.252.8')

driver.find_element_by_id('details-button').click()
driver.find_element_by_id('proceed-link').click()

'''
# Select the id box
id_box = driver.find_element_by_name('username')
# Equivalent Outcome! 
id_box = driver.find_element_by_id('username')


# Send id information
id_box.send_keys('kaa')

# Find password box
pass_box = driver.find_element_by_name('password')
# Send password
pass_box.send_keys('KZp06f120@6P&')
# Find login button
login_button = driver.find_element_by_class_name('login_button')
# Click login
login_button.click()
'''

# Open a new window
driver.execute_script("window.open('');")
time.sleep(5)
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get('https://google.com')
driver.maximize_window()
time.sleep(5)

# Close the tab
driver.close()

# Close the browser
driver.quit()
