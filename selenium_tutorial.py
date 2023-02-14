from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

path = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)



main = driver.find_elements_by_id("main")
print(main.text)

time.sleep(5)





driver.quit()