from selenium import webdriver
from selenium.webdriver.common.by import By

#this two lines of code is used not to close the URL that is opened 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# price_whole=driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_float=driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"the price is {price_whole.text}.{price_float.text}")

search=driver.find_element(By.NAME,value="q")
print(search.text)
print(search.tag_name)
print(search.get_attribute("placeholder"))
button=driver.find_element(By.ID,value="submit")
print(button.size)

link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(link.text)

link_2=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
print(link_2.text)
# driver.close()


driver.quit()

# the difference between close and quit is close will only close the tab , but quit will close the browser