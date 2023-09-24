import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL="t72053126@gmail.com"
PASSWORD="9944924888"
ROLE="Python Developer"
MOBILE_NUMBER="9876543210"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
    
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/")

#this time is to cancel the pop up 
time.sleep(2)
reject_button = driver.find_element(By.XPATH, value="/html/body/main/div[1]/button")
reject_button.click()

email=driver.find_element(By.ID,value="session_key")
email.send_keys(EMAIL)

password=driver.find_element(By.ID,value="session_password")
password.send_keys(PASSWORD)

sign_in_button=driver.find_element(By.CLASS_NAME,value="sign-in-form__submit-btn--full-width")
sign_in_button.click()

#to get rid of security check
input("Enter if puzzle is solved")

search_box_role=driver.find_element(By.CLASS_NAME,value="search-global-typeahead__input")
search_box_role.send_keys(ROLE)
search_box_role.send_keys(Keys.ENTER)

# sleep is used to wait until the page gets loaded
time.sleep(3)
jobs_button=driver.find_element(By.CSS_SELECTOR,value="#search-reusables__filters-bar > ul > li:nth-child(1) > button")
jobs_button.click()

time.sleep(3)
easy_apply_button_filter=driver.find_element(By.XPATH,value="/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
easy_apply_button_filter.click()

time.sleep(3)
easy_apply_button=driver.find_element(By.XPATH,value="/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button")
easy_apply_button.click()

#filling details after the easy apply

time.sleep(3)
mobile_phone_number=driver.find_element(By.CSS_SELECTOR,value="#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3703750848-97141837-phoneNumber-nationalNumber")
mobile_phone_number.send_keys(MOBILE_NUMBER)


next1=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
next1.click()

next2=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
next2.click()

yearofexperience1=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input")
yearofexperience1.send_keys("0")

yearofexperience2=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input")
yearofexperience2.send_keys("0")

yes1=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/fieldset/div[1]/label")
yes1.click()

yes2=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/fieldset/div[1]/label")
yes2.click()

review_button=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
review_button.click()

submit_application=driver.find_element(By.XPATH,value="/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[2]/button[2]")
submit_application.click()

