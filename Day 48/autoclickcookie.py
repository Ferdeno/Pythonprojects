from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

button=driver.find_element(By.ID,value='cookie')

money=driver.find_element(By.ID,value="money")

store=driver.find_element(By.ID,value="store")
price=store.text.split("\n")
new_price=[price[i]  for i in range(0,len(price),2)]


name_list=[]
buy_list=[]


for temp in new_price:
    
    name=temp.split("\n")[0]
    
    buy_name=name.split("-")[0]
    name_list.append(buy_name)
    
    buy_price=name.split("-")[1].replace(",","")
    buy_list.append(buy_price)

print(name_list,buy_list)


