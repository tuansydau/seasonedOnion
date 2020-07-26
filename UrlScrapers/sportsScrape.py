import pandas as pd
from selenium import webdriver
from searchUrlsMethod import searchUrl

option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors-spki-list')
option.add_argument('--ignore-ssl-errors')
option.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
driver.get("https://sports.theonion.com/")
sportsUrls = []
searchUrl(driver, "/html/body/div[3]/div[4]/main/div/div[5]/div/a", "sc-759qgu-0", r'C:\Users\Tuan\Desktop\Seasoned Onion\sportsUrlsTesting.csv', sportsUrls)