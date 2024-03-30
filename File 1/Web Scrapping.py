#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Qs1: Write a python program to display IMDB’s Top rated 100 Indian movies’ data
#https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.


from bs4 import BeautifulSoup
import requests
import pandas as pd

page=requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[54]:


soup=BeautifulSoup(page.content)

soup


# In[55]:


rating=[]
for i in soup.find_all('div',class_="ipl-rating-star small"):
    rating.append(i.text.replace('\n',''))
    
name=[]
for i in soup.find_all('h3',class_="lister-item-header"):
    name.append(i.text.replace('\n',''))
    
year=[]
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
    year.append(i.text)
    
df1=pd.DataFrame({'Name':name,'Year':year,'Ratings':rating})
df1


# In[57]:


#Qs5:Write a python program to scrape house details from mentioned URL. It should include house title, location, 
#area, EMI and price from https://www.nobroker.in/.

page1=requests.get('https://www.nobroker.in/property/sale/bangalore/Indira%20Nagar%20II%20Stage?searchParam=W3sibGF0IjoxMi45ODEyNDU5LCJsb24iOjc3LjYzNzE0NTksInBsYWNlSWQiOiJDaElKMzlzdFVMc1dyanNSb1pXTmhNNzBVZ28iLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIgSUkgU3RhZ2UifV0=&radius=2.0&city=bangalore&locality=Indira%20Nagar%20II%20Stage')
page1


# In[18]:


soup1=BeautifulSoup(page1.content)
soup1


# In[58]:


heading=[]

for i in soup1.find_all("h2",class_="heading-6 flex items-center font-semi-bold m-0"):
    heading.append(i.text)
    
loc=[]

for i in soup1.find_all("div",class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    loc.append(i.text)
    
area=[]
for i in soup1.find_all('div',class_="flex flex-col w-33pe items-center tp:w-half po:w-full"):
    area.append(i.text.replace(' sqftBuiltup',''))
    
df5=pd.DataFrame({'Heading':heading,'Location':loc,'Area':area})
df5


# In[59]:


#Qs6:Write a python program to scrape first 10 product details which include product name , price , Image URL from 
#https://www.bewakoof.com/bestseller?sort=popular . 

from bs4 import BeautifulSoup
import requests
import pandas as pd

page2=requests.get('https://www.bewakoof.com/bestseller?sort=popular')
page2


# In[60]:


soup2=BeautifulSoup(page2.content)
soup2


# In[61]:


prodname=[]

for i in soup2.find_all("h2",class_="clr-shade4 h3-p-name undefined false"):
    prodname.append(i.text)
    
price1=[]

for i in soup2.find_all('div',class_='discountedPriceText clr-p-black false'):
    price1.append(i.text)

imag=[]
for i in soup2.find_all('div',class_="productImg"):
    imag.append(['data.src'])

df6=pd.DataFrame({'Product':prodname,'Price':price1,'Image':imag})
df6


# In[44]:


#Qs7:Please visit https://www.cnbc.com/world/?region=world and scrap- headings, date and News link

page3=requests.get('https://www.cnbc.com/politics/')
page3


# In[45]:


soup3=BeautifulSoup(page3.content)
soup3


# In[68]:


Headline=[]

for i in soup3.find_all("div",class_="Card-titleContainer"):
    Headline.append(i.text)

date=[]

for i in soup3.find_all("span",class_="Card-time"):
    date.append(i.text)
    
URL=[]

for i in soup3.find_all("a",class_="Card-title"):
    URL.append(i.text)
    
df7=pd.DataFrame({'Headline':Headline,'Date':date,'Newslink':URL})
df7


# In[50]:


#Qs8: Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/ 
# and scrap- Paper title, date and Author

page4=requests.get('https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')
page4


# In[51]:


soup4=BeautifulSoup(page4.content)
soup4


# In[69]:


title=[]

for i in soup4.find_all("h2",class_="h5 article-title"):
    title.append(i.text.replace('\n','').replace('\r',''))
    
date_month=[]
for i in soup4.find_all("p",class_="article-date"):
    date_month.append(i.text)
    
author=[]
for i in soup4.find_all("p",class_="article-authors"):
    author.append(i.text)

author

df4=pd.DataFrame({'Article':title,'Date':date_month,'Author':author})
df4

