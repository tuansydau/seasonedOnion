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
driver.get("https://www.theonion.com/a-message-from-the-publisher-only-hoover-can-get-ameri-1819583226")

#loop steps:
#P. Get URL List
#1. Go to URL
#2. Get headline, content, (metadata)
#3. Write data

headlines = []
article = []
content = []
paragraphs = []

#find headline
headline = driver.find_elements_by_xpath("/html/body/div[3]/div[4]/div[2]/header/h1/a")[0]
print(headline.text)
headlines.append(headline.text)

# dont touch this, it gets body text but not well
content = driver.find_elements_by_class_name("sc-77igqf-0")
for piece in content:
    paragraphs.append(piece.text)
print(paragraphs)
completeContent = ' '.join(paragraphs)
paragraphs = []
print(completeContent)

# format and write to csv
format = {'Headline': headlines, 'Body text': completeContent}
df_urls = pd.DataFrame(format)
df_urls.to_csv(r'C:\Users\Tuan\Desktop\Seasoned Onion\articleContent.csv')
