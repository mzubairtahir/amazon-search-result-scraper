from playwright.sync_api import sync_playwright
import time 
import pandas as pd
from bs4 import BeautifulSoup

#-------------------

total_pages_to_scrape=1
output_format =  0     # This value can be 0(excel) or 1(csv)
data=[]

#-------------------------

with sync_playwright() as p:
    browser= p.chromium.launch(headless=True)
    page= browser.new_page()
    for page_number in range(1,total_pages_to_scrape+1):
        link=f"https://www.amazon.com/s?k=watches+for+man&i=fashion-mens-watches&page={page_number}&qid=1680665242&sprefix=watches+man%2Cfashion-mens-watches%2C2086&ref=sr_pg_{page_number}"

        page.goto(link)
        try:
            products_section=page.query_selector("//*[@id='search']/div[1]/div[1]/div")
        except:
            print('not found')
        else:
            html=products_section.inner_html()
        
        soup=BeautifulSoup(html,'html.parser')
        all_cards=soup.find_all('div',class_='a-section a-spacing-base')
        for card in all_cards:
            image_url=card.find('img',class_='s-image').get('src')
            product_link=card.find('a',class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').get('href')
            products_title=card.find('span',class_='a-size-base-plus a-color-base a-text-normal').get_text(strip=True)
            try:
                total_reviews=card.find('div',class_='a-row a-size-small').find('span',class_='a-size-base s-underline-text').get_text(strip=True)
            except:
                total_reviews=None
            try:

                rating=card.find('div',class_='a-row a-size-small').find('span',class_='a-size-base').get_text(strip=True)
            except:
                rating=None
            try:

                price=card.find('span',class_='a-price').find('span',class_='a-offscreen').get_text(strip=True)
            except:
                price=None
            
            features={
                'Title':products_title,
                'Product url': "amazon.com"+product_link,
                'Image url':image_url,
                'Total reviews':total_reviews,
                'Rating':rating,
                'Price':price
            }
            data.append(features)
        break

df=pd.DataFrame(data=data)
if output_format==0:
    df.to_excel('products.xlsx',index=False)
elif output_format==1:
    df.to_csv('products.xlsx',index=False)


