from selenium import webdriver
from selenium.webdriver.common.by import By

#this two lines of code is used not to close the URL that is opened 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

search=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
data=search.text.split("\n")
date=[]
name=[]
for i in range(0,len(data),2):
    date.append(data[i])
    name.append(data[i+1])

d={}

for i in range(len(date)):
    d[i]={'time':date[i],'name':name[i]}
print(d)


driver.close()