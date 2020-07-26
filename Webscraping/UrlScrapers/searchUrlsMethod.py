import pandas as pd
from selenium import webdriver

#loop steps:
#1. Find headline title elements
#2. Find their parent elements
#3. Get the href values from the elements
#4. Write to file to save progress in case of error
#5. Press the Next button
#6. Ad infinitum
def searchUrl(driver, xpathToNext, className, filePath, articleList):
    while True:
        # I couldn't import the time library so I slowed down the program by finding the elements multiple times
        # slows the scraper down a bunch but damn is it effective
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        driver.find_elements_by_class_name(className)
        urlChildElements = driver.find_elements_by_class_name(className)
        for urlChildElement in urlChildElements:
            parent = urlChildElement.find_element_by_xpath("./..")
            #print(parent.get_attribute("href"))
            articleList.append(parent.get_attribute("href"))
            #print(url.get_attribute('href'))
            #print(url.text)
        df_urls = pd.DataFrame(articleList)
        df_urls.to_csv(filePath)
        print(len(articleList))
        driver.implicitly_wait(10)
        driver.find_elements_by_xpath(xpathToNext)[0].click()