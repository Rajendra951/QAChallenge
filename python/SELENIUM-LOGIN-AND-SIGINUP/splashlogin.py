from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Browser and Create driver object
driver = webdriver.Chrome()
time.sleep(3)

# Maximize window
driver.maximize_window()
time.sleep(3)

# Launch URL 
driver.get('https://splashthat.com/login')
time.sleep(3)

# Enter User Name
uname = driver.find_element(By.XPATH, '//*[@id="homeRealmDiscoveryInput"]')
uname.send_keys('manekonda.rajendra3@gmail.com')
time.sleep(3)

# Click on submit button
login_b = driver.find_element(By.ID, 'homeRealmDiscoverySubmit')
login_b.click()
time.sleep(3)

# Enter password
p = driver.find_element(By.ID, 'loginPasswordInput')
p.send_keys('Rajendra112233!')
time.sleep(3)

# Click on Submit button
login_b = driver.find_element(By.ID, 'loginSubmit')
login_b.click()
time.sleep(10)

# Close window
driver.close()