from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

options=webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(options=options)
sleep(3)
data=[]
for page in range(100):
    url=f'https://www.amazon.com/s?k=men+watches&i=fashion-mens-watches&rh=n%3A6358540011%2Cp_n_feature_three_browse-bin%3A2205662011&dc&page={page}&crid=19B2C27YBQ427&qid=1672159962&rnid=2205644011&sprefix=menwatches%2Caps%2C530&ref=sr_pg_{page}'

    driver.get(url)
    sleep(10)


    mainElement=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]') 
    sleep(3)
    source=mainElement.get_attribute('outerHTML')

    soup=BeautifulSoup(source,'html.parser')

    allRecquiredProducts=soup.find_all('div',class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
    for i in allRecquiredProducts:
        try:
            title=i.find('div',class_='a-section a-spacing-none a-spacing-top-small s-title-instructions-style').text
        except:
            title=None
        completeRatingReview=i.find('div',class_='a-section a-spacing-none a-spacing-top-micro')
        try:
            rating=completeRatingReview.find('span',class_='a-size-base').text
        except:
            rating=None
        
        try:
            totalReviews=completeRatingReview.find('span',class_='a-size-base s-underline-text').text
        except:
            totalReviews=None
        try:
            price=i.find('span',class_='a-offscreen').text
        except:
            price=None
        
        dataDict={
            'Title':title,
            'Price':price,
            'Rating':rating,
            'Total Reviews':totalReviews
        }

        data.append(dataDict)

    sleep(3)

df= pd.DataFrame(data)
df.to_excel('PricingAnalysis.xlsx',index=False)
