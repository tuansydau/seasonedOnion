import pandas as pd
import numpy as np
import bs4
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
    headlines = []
    paragraphs = []
    finalHeadline = ""

    #find headline
    try:
        headline = driver.find_elements_by_xpath("/html/body/div[3]/div[4]/div[2]/header/h1/a")
        if headline:
            print(headline[0].text)
            finalHeadline = headline[0].text
        else:
            finalHeadline = ""
    except NoSuchElementException:
        finalHeadline = ""

    # dont touch this, it gets body text but not well
    try:
        content = driver.find_elements_by_class_name("sc-77igqf-0")
        for piece in content:
            paragraphs.append(piece.text)
        print(paragraphs)
        completeContent = ' '.join(paragraphs)
        print(completeContent)
    except NoSuchElementException:
        completeContent = ""

    return finalHeadline, completeContent

def write_content(headlineList, contentList):
    # format and write to csv
    format = {'Headline': headlineList, 'Body text': contentList}
    df_urls = pd.DataFrame(format)
    df_urls.to_csv(r'C:\Users\Tuan\Desktop\Seasoned Onion\archiveContent.csv')

urlList = pd.read_csv(r'C:\Users\Tuan\Desktop\Seasoned Onion\articleUrls.csv')

print("-----------------------")
print(urlList)

headList = []
bodyList = []

for url in urlList['0']:
    head, body = get_content(url)
    headList.append(head)
    bodyList.append(body)

    write_content(headList, bodyList)