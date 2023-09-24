import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button=driver.find_element(By.ID,value='cookie')

money=driver.find_element(By.ID,value="money")


def buyTime():
    return int(driver.find_element(By.ID,value="buyTime machine").text.split("\n")[0].split("-")[1].replace(",",""))
    

def buyPortal():
    return int(driver.find_element(By.ID,value="buyPortal").text.split("\n")[0].split("-")[1].replace(",",""))


def buyAlchemy():
    return int(driver.find_element(By.ID,value="buyAlchemy lab").text.split("\n")[0].split("-")[1].replace(",",""))


def buyShipment():
    return int(driver.find_element(By.ID,value="buyShipment").text.split("\n")[0].split("-")[1].replace(",",""))


def buyMine():
    return int(driver.find_element(By.ID,value="buyMine").text.split("\n")[0].split("-")[1].replace(",",""))
    
    
def buyFactory():
    return int(driver.find_element(By.ID,value="buyFactory").text.split("\n")[0].split("-")[1].replace(",",""))


def buyGrandma():
    return int(driver.find_element(By.ID,value="buyGrandma").text.split("\n")[0].split("-")[1].replace(",",""))


def buyCursor():
    return int(driver.find_element(By.ID,value="buyCursor").text.split("\n")[0].split("-")[1].replace(",",""))


starttime=time.time()
endtime=starttime+60

temp=0
while(temp<100):
    cookie_button.click()
    temp+=1

while time.time()<endtime:
    time.sleep(5)
    cookie_score=int(driver.find_element(By.ID,value="money").text.replace(",",""))

    if cookie_score>buyTime():
        button=driver.find_element(By.ID,value="buyTime")
        button.click()
    elif cookie_score>buyPortal():
        button=driver.find_element(By.ID,value="buyPortal")
        button.click()
    elif cookie_score>buyAlchemy():
        button=driver.find_element(By.ID,value="buyAlchemy")
        button.click()
    elif cookie_score>buyShipment():
        button=driver.find_element(By.ID,value="buyShipment")
        button.click()
    elif cookie_score>buyMine():
        button=driver.find_element(By.ID,value="buyMine")
        button.click()
    elif cookie_score>buyFactory():
        button=driver.find_element(By.ID,value="buyFactory")
        button.click()
    elif cookie_score>buyGrandma():
        button=driver.find_element(By.ID,value="buyGrandma")
        button.click()
    elif cookie_score>buyCursor():
        button=driver.find_element(By.ID,value="buyCursor")
        button.click()

print(driver.find_element(By.ID,value="cps").text)

# driver.quit()
