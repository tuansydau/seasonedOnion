import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from parsel import Selector

# initialize browser, --incognito for cache/cookies
option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors-spki-list')
option.add_argument('--ignore-ssl-errors')
option.add_argument('--incognito')

#make a chrome instance and go to the starting page
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=option)

#loop steps:
#P. Get URL List
#1. Go to URL
#2. Get headline, content, (metadata)
#3. Write data

def get_content(url):
    driver.get(url)
    paragraphs = []
    finalHeadline = ""
    metaTags = ''

    #find headline
    try:
        headline = driver.find_elements_by_xpath("/html/body/div[3]/div[4]/div[2]/header/h1/a")
        if headline:
            #print(headline[0].text)
            finalHeadline = headline[0].text
        else:
            finalHeadline = ""
    except NoSuchElementException:
        finalHeadline = ""

    #find body text kind of
    try:
        content = driver.find_elements_by_class_name("sc-77igqf-0")
        for piece in content:
            paragraphs.append(piece.text)
        #print(paragraphs)
        completeContent = ' '.join(paragraphs)
        #print(completeContent)
    except NoSuchElementException:
        completeContent = ""

    #get metadata
    metaTags = driver.find_element_by_xpath("//meta[@name='news_keywords']").get_attribute("content").lower()
    #print(metaTags)

    return finalHeadline, completeContent, metaTags

def write_content(headlineList, contentList, metaDataList):
    # format and write to csv
    print(metaDataList)
    format = {'Headline': headlineList, 'Body text': contentList, 'Meta Tags': metaDataList}
    #print(metaDataList)
    df_urls = pd.DataFrame(format)
    print(df_urls)
    df_urls.to_csv(r'C:\Users\Tuan\Desktop\Seasoned Onion\localContentMeta.csv')

urlList = pd.read_csv(r'C:\Users\Tuan\Documents\GitHub\seasonedOnion\Webscraping\UrlScrapers\URLs\localUrls - Final.csv')

#print("-----------------------")
#print(urlList)

headList = []
bodyList = []
metaDataList = []

for url in urlList['0']:
    #print(metaDataList)
    head, body, metaData = get_content(url)
    headList.append(head)
    bodyList.append(body)
    #print(metaData)
    metaDataList.append(metaData)

    write_content(headList, bodyList, metaDataList)