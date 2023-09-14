from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#this two lines of code is used not to close the URL that is opened 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search=driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# print(search.text)

# search.click()

view_source=driver.find_element(By.PARTIAL_LINK_TEXT,value="View source")
# view_source.click()

search_tab=driver.find_element(By.CLASS_NAME,value="cdx-text-input__input")
search_tab.send_keys("Ferdeno")
search_tab.send_keys(Keys.ENTER)
