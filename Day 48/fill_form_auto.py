from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#this two lines of code is used not to close the URL that is opened 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element(By.NAME,value="fName")
first_name.send_keys("Ferdeno")

last_name=driver.find_element(By.NAME,value="lName")
last_name.send_keys("A")

email=driver.find_element(By.NAME,value="email")
email.send_keys("faf@gmail.com")

button=driver.find_element(By.CLASS_NAME,value="btn")
button.click()