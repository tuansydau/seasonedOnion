import pandas as pd
import numpy as np
import bs4
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from parsel import Selector

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors-spki-list')
option.add_argument('--ignore-ssl-errors')
option.add_argument('--incognito')

#make a chrome instance
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)

driver.get("https://www.theonion.com/tag/archive")
#urls = driver.find_elements_by_class_name('sc-1out364-0 hMndXN js_link')
#urls = driver.find_element_by_xpath("/html/body/div[3]/div[4]/main/div/div[3]/article[1]/div[3]/div/div[2]/a")
urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
#urls = driver.find_elements_by_xpath("/html/body/div[3]/div[4]/main/div/div[sc-759qgu-0 cYlVdn cw4lnv-6 eXwNRE3]/article[1]/div[3]/figure/a/div/div/img")


for urlChildElement in urlChildElements :
    parent = urlChildElement.find_element_by_xpath("./..")
    print(parent.get_attribute("href"))
    #print(url.get_attribute('href'))
    #print(url.text)

print(len(urlChildElements))