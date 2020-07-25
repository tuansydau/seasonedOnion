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

#make a chrome instance and go to the starting page
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)
driver.get("https://politics.theonion.com/")

#initialize the article url list
articles = []

#loop steps:
#1. Find headline title elements
#2. Find their parent elements
#3. Get the href values from the elements
#4. Write to file to save progress in case of error
#5. Press the Next button
#6. Ad infinitum
while True:
    # I couldn't import the time library so I slowed down the program by finding the elements multiple times
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    urlChildElements = driver.find_elements_by_class_name("sc-759qgu-0")
    for urlChildElement in urlChildElements:
        parent = urlChildElement.find_element_by_xpath("./..")
        #print(parent.get_attribute("href"))
        articles.append(parent.get_attribute("href"))
        #print(url.get_attribute('href'))
        print(urlChildElement.text)
    df_urls = pd.DataFrame(articles)
    df_urls.to_csv(r'C:\Users\Tuan\Desktop\Seasoned Onion\politicsUrls.csv')
    print(len(articles))
    driver.find_elements_by_xpath("/html/body/div[3]/div[4]/main/div/div[5]/div/a")[0].click()
