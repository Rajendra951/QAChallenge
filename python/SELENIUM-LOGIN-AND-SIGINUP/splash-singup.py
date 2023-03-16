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

#Enter User Name
# uname = driver.find_element(By.XPATH, '//*[@id="homeRealmDiscoveryInput"]')
# uname.send_keys('manekonda.rajendra3@gmail.com')
# time.sleep(3)

# Click sigin up link
login_b = driver.find_element(By.ID, 'signupLink')
login_b.click()
time.sleep(3)

# Enter First and Last Name
p = driver.find_element(By.ID, 'signupFullNameInput').send_keys('Rajendra Manekonda')
time.sleep(3)

# Enter EMAIL
driver.find_element(By.ID, 'signupEmailInput').send_keys('manekonda.rajendra3@gmail.com')
time.sleep(3)

# Enter PASSWORD
driver.find_element(By.ID, 'signupPasswordInput').send_keys('Rajendra112233!')
time.sleep(3)

# Click ON CHECK BOX
driver.find_element(By.ID, 'privacyPolicyInput').click()
time.sleep(3)

#Click on Submit button
login_b = driver.find_element(By.ID, "signupSubmit").click()
time.sleep(10)

#Close window
driver.close()