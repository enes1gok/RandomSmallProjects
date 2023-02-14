from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Users\HP\Desktop\MyPythonProjects\chromedriver.exe")
url = "https://www.instagram.com"

browser.get(url)


time.sleep(7)

browser.close()