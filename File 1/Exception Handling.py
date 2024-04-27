#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Qs-1 Write a python program which searches all the product under a particular product from www.amazon.in. The 
#product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.


import selenium
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

import requests
import regex as re


# In[ ]:


driver=webdriver.Chrome()


# In[ ]:


driver.get('https://www.amazon.in/')


# In[ ]:


a=driver.find_element(By.XPATH,'//div[@class="nav-search-field "]/input')
a.send_keys('mobile')


# In[ ]:


b=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
b.click()


# In[ ]:


#Qs-2 In the above question, now scrape the following details of each product listed in first 3 pages of your search 
#results and save it in a data frame. In case if any of the details are missing then replace it by “-“.


# In[ ]:


Brand=[]
Price=[]
Delivery=[]
URL=[]

start=0
end=3
for page in range(start,end):     
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        URL.append(i.get_attribute('href'))
        
    nextbutton=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    nextbutton.click()
    time.sleep(3)
URL


# In[ ]:


for i in URL:
    driver.get(i)
    time.sleep(3)
    try:
        brand=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Brand.append(brand.text)
    except NoSuchElementException:
        Brand.append('-')
    try:
        price=driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('-')
    try:
        delivery=driver.find_element(By.ID,'deliveryBlockMessage')
        Delivery.append(delivery.text)
    except NoSuchElementException:
        Delivery.append('-')


# In[ ]:


Phone=pd.DataFrame({'Brand':Brand,'Price':Price,'Delivery':Delivery})
Phone


# In[ ]:


#Qs3 Write a program to access the search bar on images.google.com and scrape 10 images for 
#keywords fruits, cars and Machine Learning, ‘Guitar’, ‘Cakes’.

d=webdriver.Chrome()


# In[ ]:


d.get('https://images.google.com/')


# In[ ]:


Key=['Fruits']
Image=[]


image=d.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
image.send_keys(Key)
search=d.find_element(By.XPATH,'//button[@class="Tg7LZd"]')
search.click()

img=d.find_elements(By.XPATH,'//g-img[@class="mNsIhb"]')
for i in img:
    source=get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            Image.append(source)


# In[ ]:


for i in range(len(Image)):
    if i>10:
        breakBy.XPATH,
    print('download',format(i,10)) 
    response=request.gets(Image[i])
    file=open(r'C:\Flip'+str(i)+'.jpg','wb')
    file.write(response.content)


# In[ ]:


#Qs4 Write a python program to search for a smartphone and scrape following details for all the search results.
#Details to be scraped: “Brand Name, Smartphone name, Colour, RAM, Storage(ROM), Primary Camera, Secondary Camera, 
#Display Size, Battery Capacity, Price, Product URL.

web=webdriver.Chrome()


# In[ ]:


web.get('https://www.flipkart.com/')


# In[ ]:


flp=web.find_element(By.XPATH,'//input[@class="Pke_EE"]')
flp.send_keys('samsung smartphones')


# In[ ]:


cl=web.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
cl.click()


# In[ ]:


SMURL=[]
     
smurl=web.find_elements(By.XPATH,'//a[@class="CGtC98"]')
for i in smurl:
    SMURL.append(i.get_attribute('href'))
        
SMURL


# In[ ]:


SMBrand=[]
SMPrice=[]
SMRAM=[]
SMCam=[]
SMBatt=[]
SMDisplay=[]


for i in SMURL:
    web.get(i)
    time.sleep(3)
    try:
        smbrand=web.find_element(By.XPATH,'//span[@class="VU-ZEz"]')
        SMBrand.append(smbrand.text)
    except NoSuchElementException:
        SMBrand.append('-')
    try:
        smprice=web.find_element(By.XPATH,'//div[@class="Nx9bqj CxhGGd"]')
        SMPrice.append(smprice.text)
    except NoSuchElementException:
        SMPrice.append('-')
    try:
        smram=web.find_element(By.XPATH,'//div[@class="xFVion"]/ul/li[1]')
        SMRAM.append(smram.text)
    except NoSuchElementException:
        SMRAM.append('-')
    try:
        smcam=web.find_element(By.XPATH,'//div[@class="xFVion"]/ul/li[3]')
        SMCam.append(smcam.text)
    except NoSuchElementException:
        SMCam.append('-')
    try:
        smdisp=web.find_element(By.XPATH,'//div[@class="xFVion"]/ul/li[2]')
        SMDisplay.append(smdisp.text)
    except NoSuchElementException:
        SMDisplay.append('-')
    try:
        smbatt=web.find_element(By.XPATH,'//div[@class="xFVion"]/ul/li[4]')
        SMBatt.append(smbatt.text)
    except NoSuchElementException:
        SMBatt.append('-')


# In[ ]:


Phone=pd.DataFrame({'Brand':SMBrand,'Price':SMPrice,'RAM':SMRAM,'Camera':SMCam,'Display':SMDisplay,'Battery':SMBatt})
Phone


# In[ ]:


#Qs5 Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. 

driv=webdriver.Chrome()


# In[ ]:


driv.get('https://www.google.com/maps/@28.6752084,77.1600196,15z?authuser=0&entry=ttu')


# In[ ]:


maps=driv.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input")
maps.send_keys('Ashok Vihar')


# In[ ]:


MAPS=driv.find_element(By.XPATH,'//span[@class="google-symbols"]')
MAPS.click()


# In[ ]:


UR=[]
GEO=[]
ur=driv.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div/span[2]/a')
UR.append(ur.get_attribute('href'))
UR


# In[ ]:


ashok=driv.current_url
ashok


# In[ ]:


vihar=re.findall(r'@(.*)data',ashok)
vihar


# In[ ]:


#Qs6 Write a program to scrap all the available details of best gaming laptops from digit.in.

dr=webdriver.Chrome()


# In[ ]:


dr.get('https://www.digit.in/')


# In[ ]:


lap=dr.find_element(By.XPATH,'/html/body/div[4]/div/ul/li[4]')
lap.click()


# In[ ]:


game=dr.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div[1]/div[3]/div[11]/p/a')
game.click()


# In[ ]:


Window=[]

window=dr.find_elements(By.XPATH,'//div[@class="woo_code_zone_loop clearbox"]')
for i in window:
        Window.append(i.text)

Window


# In[ ]:


#Qs7 Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
#“Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

dri=webdriver.Chrome()


# In[ ]:


dri.get('https://www.forbes.com/')


# In[ ]:


billion=dri.find_element(By.XPATH,'//div[@class="_69hVhdY4"]')
billion.click()


# In[ ]:


bill=dri.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div[2]/ul/li[2]/div[1]')
bill.click()


# In[ ]:


wor=dri.find_element(By.XPATH,'/html/body/div[1]/header/nav/div[1]/div[1]/div/div[2]/ul/li[2]/div[2]/div[3]/ul/li[1]')
wor.click()


# In[ ]:


Bill_name=[]
Net_worth=[]
Industry=[]
Rank=[]

bill_name=dri.find_elements(By.XPATH,'//div[@class="Table_personName__Bus2E"]')
for i in bill_name:
    Bill_name.append(i.text)
    
rank=dri.find_elements(By.XPATH,'//div[@class="Table_rank__X4MKf"]/div')
for i in rank:
    Rank.append(i.text)

net_worth=dri.find_elements(By.XPATH,'//div[@class="Table_finalWorth__UZA6k"]/span')
for i in net_worth:
    Net_worth.append(i.text)
    
Net_worth


# In[ ]:


Billionaire=pd.DataFrame({'Rank':Rank,'Name':Bill_name,'Net Worth':Net_worth})
Billionaire


# In[ ]:


#Qs9 Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
#“London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
#reviews, privates from price, dorms from price, facilities and property description.  

host=webdriver.Chrome()


# In[ ]:


host.get('https://www.hostelworld.com/')


# In[ ]:


loca=host.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/main/header/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/input')
loca.send_keys('London')


# In[ ]:


locat=host.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/main/header/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/ul/li[2]/button/div[2]/div[1]')
locat.click()


# In[ ]:


sear=host.find_element(By.XPATH,'//button[@class="medium-button btn-content icon-only"]')
sear.click()


# In[ ]:


Hostel_name=[]
Hostel_rating=[]
Hostel_distance=[]
Hostel_price=[]


hostel_name=host.find_elements(By.CLASS_NAME,"property-name")
for i in hostel_name:
    try:
        Hostel_name.append(i.text)
    except NoSuchElementException:
        Hostel_name.append('-')
    
ratin=host.find_elements(By.CLASS_NAME,"number")
for i in ratin:
    try:
        Hostel_rating.append(i.text)
    except NoSuchElementException:
        Hostel_rating.append('-')

distance=host.find_elements(By.CLASS_NAME,"distance-description")
for i in distance:
    try:
        Hostel_distance.append(i.text)
    except NoSuchElementException:
        Hostel_distance.append('-')
    


# In[ ]:


Hostel_rating


# In[ ]:


Hostel_name


# In[ ]:


Hostel_distance

