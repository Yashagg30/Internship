#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Qs1 Scrape the details of most viewed videos on YouTube from Wikipedia and find: Rank, Name, Artist, Upload date and Views 

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


# In[27]:


driver=webdriver.Chrome()


# In[28]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[29]:


Rank=[]
Name=[]
Artist=[]
Date=[]
Views=[]


# In[30]:


name=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[1]")
for i in name:
    if i.text is None :
        Name.append("--") 
    else:
        Name.append(i.text)
print(len(Name),Name)


# In[31]:


Ar=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[2]")
for i in Ar:
    if i.text is None :
        Artist.append("--") 
    else:
        Artist.append(i.text)
print(len(Artist),Artist)


# In[32]:


views=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[3]")
for i in views:
    if i.text is None :
        Views.append("--") 
    else:
        Views.append(i.text)
print(len(Views),Views)


# In[33]:


date=driver.find_elements(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr/td[4]")
for i in date:
    if i.text is None :
        Date.append("--") 
    else:
        Date.append(i.text)
print(len(Date),Date)


# In[34]:


Youtube_Video=pd.DataFrame([])
Youtube_Video['Video Title']=Name
Youtube_Video['Artist']=Artist
Youtube_Video['Upload_Date']=Date
Youtube_Video['Views In Bllion']=Views
Youtube_Video


# In[41]:


#Qs2 Scrape the details team India’s international fixtures from bcci.tv.and scrap Series, Place,Date and Time   

drive=webdriver.Chrome()


# In[42]:


drive.get("https://www.bcci.tv/international")


# In[48]:


Time=[]
Date=[]
Place=[]
Series=[]


# In[45]:


ser=drive.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in ser:
    if i.text is None :
        Series.append("--") 
    else:
        Series.append(i.text)
print(len(Series),Series)


# In[46]:


DT=drive.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in DT:
    if i.text is None :
        Date.append("--") 
    else:
        Date.append(i.text)
print(len(Date),Date)


# In[49]:


tm=drive.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in tm:
    if i.text is None :
        Time.append("--") 
    else:
        Time.append(i.text)
print(len(Time),Time)


# In[50]:


pl=drive.find_elements(By.XPATH,'//span[@class="ng-binding ng-scope"]')
for i in pl:
    if i.text is None :
        Place.append("--") 
    else:
        Place.append(i.text)
print(len(Place),Place)


# In[51]:


International_Fixtures=pd.DataFrame([])
International_Fixtures['Series']=Series
International_Fixtures['Date']=Date
International_Fixtures['Time']=Time
International_Fixtures['Ground']=Place
International_Fixtures


# In[69]:


#Qs3 Scrape the details of State-wise GDP of India from statisticstime.com.
#And scrap Rank, State, GSDP(18-19)- at current prices, GSDP(19-20)- at current prices, Share(18-19) and GDP($ billion)   

driv=webdriver.Chrome()


# In[70]:


driv.get('http://statisticstimes.com/')


# In[71]:


Rank=[]
State =[]
GDP=[]
GSDP_Current=[]
GSDP_Previous=[]
Share=[]


# In[72]:


eco = driv.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/button')
eco.click()


# In[73]:


ind = driv.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/div/a[3]')
ind.click()


# In[75]:


gdp = driv.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
gdp.click()


# In[76]:


r=driv.find_elements(By.XPATH,"//td[@class='data1']")
for i in r:
    if i.text is None :
        Rank.append("--") 
    else:
        Rank.append(i.text)
print(len(Rank),Rank)


# In[77]:


St=driv.find_elements(By.XPATH,"//td[@class='name']")
for i in St:
    if i.text is None :
        State.append("--") 
    else:
        State.append(i.text)
print(len(State),State)


# In[79]:


shr=driv.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[6]")
for i in shr:
    if i.text is None :
        Share.append("--") 
    else:
        Share.append(i.text)
print(len(Share),Share)


# In[80]:


gsdpc=driv.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[5]")
for i in gsdpc:
    if i.text is None :
        GSDP_Current.append("--") 
    else:
        GSDP_Current.append(i.text)
print(len(GSDP_Current),GSDP_Current)


# In[83]:


gsdpp=driv.find_elements(By.XPATH,"//*[@id='table_id']/tbody/tr/td[8]")
for i in gsdpp:
    if i.text is None :
        GSDP_Previous.append("--") 
    else:
        GSDP_Previous.append(i.text)
print(len(GSDP_Previous),GSDP_Previous)


# In[85]:


#Qs4 Scrape details of trending repositories on Github.com. Repository title, description, Contributors count and Language used.


dri=webdriver.Chrome()


# In[86]:


dri.get('https://github.com/')


# In[97]:


Repository_Name =[]
Descrip=[]
Language=[]
Muted_Link=[]


# In[89]:


explore = dri.find_element(By.XPATH,'//button[@class="js-details-target Button--link Button--medium Button d-lg-none color-fg-inherit p-1"]')
explore.click()


# In[92]:


repost = dri.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
repost.click()


# In[93]:


trend = dri.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
trend.click()


# In[96]:


RN=dri.find_elements(By.XPATH,"//span[@class='text-normal']")
for i in RN:
    if i.text is None :
        Repository_Name.append("--") 
    else:
        Repository_Name.append(i.text)
print(len(Repository_Name),Repository_Name)


# In[98]:


des=dri.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
for i in des:
    if i.text is None :
        Descrip.append("--") 
    else:
        Descrip.append(i.text)
print(len(Descrip),Descrip)


# In[99]:


L=dri.find_elements(By.XPATH,"//span[@itemprop='programmingLanguage']")
for i in L:
    if i.text is None :
        Language.append("NAN") 
    else:
        Language.append(i.text)
print(len(Language),Language)


# In[104]:


#Qs5 Scrape the details of top 100 songs on billiboard.com. Song, Artist,Last week rank, Peak rank and Weeks on board

dr=webdriver.Chrome()


# In[105]:


dr.get('https:/www.billboard.com/')


# In[102]:


Song=[]
Singer=[]
rank=[]
Last_Week=[]
Weeks_on_board=[]


# In[106]:


top100 = dr.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/a[1]')
top100.click()


# In[ ]:


sin=driver.find_elements(By.XPATH,"//span[@class='chart-element__information__artist text--truncate color--secondary']")
for i in sin:
    if i.text is None :
        Singer.append("--") 
    else:
        Singer.append(i.text)
print(len(Singer),Singer)


# In[109]:


#Qs6 Scrape the details of Highest selling novels.Book name, Author name, Volumes sold, Publisher and Genre 

d=webdriver.Chrome()


# In[110]:


d.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[111]:


Book_name=[]
Author_name=[]
Volumes_sold=[]
Publisher=[]
Genre=[]


# In[112]:


bname=d.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[2]")
for i in bname:
    if i.text is None :
        Book_name.append("--") 
    else:
        Book_name.append(i.text)
print(len(Book_name),Book_name)


# In[113]:


Auth=d.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[3]")
for i in Auth:
    if i.text is None :
        Author_name.append("--") 
    else:
        Author_name.append(i.text)
print(len(Author_name),Author_name)


# In[114]:


gen=d.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[6]")
for i in gen:
    if i.text is None :
        Genre.append("--") 
    else:
        Genre.append(i.text)
print(len(Genre),Genre)


# In[115]:


pub=d.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[5]")
for i in pub:
    if i.text is None :
        Publisher.append("--") 
    else:
        Publisher.append(i.text)
print(len(Publisher),Publisher)


# In[116]:


vs=d.find_elements(By.XPATH,"/html/body/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[4]")
for i in vs:
    if i.text is None :
        Volumes_sold.append("--") 
    else:
        Volumes_sold.append(i.text)
print(len(Volumes_sold),Volumes_sold)


# In[117]:


#Qs7 Scrape the details most watched tv series of all time from imdb.com.   
#Scrap Name, Year span, Genre, Run time, Ratings and Votes   

ds=webdriver.Chrome()


# In[119]:


ds.get('https://www.imdb.com/list/ls512407256/')


# In[124]:


SName=[]
Year_span=[]
Genres=[]
Run_time=[]
Ratings=[]
Votes=[]


# In[126]:


mname=ds.find_elements(By.XPATH,'//h3[@class="ipc-title__text"]')
for i in mname:
    if i.text is None :
        SName.append("--") 
    else:
        SName.append(i.text)
print(len(SName),SName)


# In[128]:


ys=ds.find_elements(By.XPATH,'//div[@class="sc-b189961a-7 feoqjK dli-title-metadata"]/span[1]')
for i in ys:
    if i.text is None :
        Year_span.append("--") 
    else:
        Year_span.append(i.text)
print(len(Year_span),Year_span)


# In[ ]:


gnr=ds.find_elements(By.XPATH,"//p[@class='text-muted text-small']/span[5]")
for i in gnr:
    if i.text is None :
        Genres.append("--") 
    else:
        Genres.append(i.text)
print(len(Genres),Genres)


# In[130]:


rt=ds.find_elements(By.XPATH,'//div[@class="sc-b189961a-7 feoqjK dli-title-metadata"]/span[2]')
for i in rt:
    if i.text is None :
        Run_time.append("--") 
    else:
        Run_time.append(i.text)
print(len(Run_time),Run_time)


# In[131]:


rate=ds.find_elements(By.XPATH,'//span[@class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"]')
for i in rate:
    if i.text is None :
        Ratings.append("--") 
    else:
        Ratings.append(i.text)
print(len(Ratings),Ratings)


# In[132]:


#Qs8 Details of Datasets from UCI machine learning repositories.     
#Dataset name, Data type, Task, Attribute type, No of instances, No of attribute and Year  

Driver=webdriver.Chrome()


# In[133]:


Driver.get('https://archive.ics.uci.edu/')


# In[137]:


Dataset_Name=[]
Data_Type=[]
Task=[]
Attribute_Type=[]
No_of_Instances=[]
No_of_Attribute=[]
Year=[]


# In[135]:


sea = Driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
sea.click()


# In[139]:


dname=Driver.find_elements(By.XPATH,'//a[@class="link-hover link text-xl font-semibold"]')
for i in dname:
    if i.text is None :
        Dataset_Name.append("--") 
    else:
        Dataset_Name.append(i.text)
print(len(Dataset_Name),Dataset_Name)


# In[140]:


dtype=Driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[2]')
for i in dtype:
    if i.text is None :
        Data_Type.append("--") 
    else:
        Data_Type.append(i.text)
print(len(Data_Type),Data_Type)


# In[141]:


t=Driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[1]')
for i in t:
    if i.text is None :
        Task.append("--") 
    else:
        Task.append(i.text)
print(len(Task),Task)


# In[142]:


noi=Driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[3]')
for i in noi:
    if i.text is None :
        No_of_Instances.append("--") 
    else:
        No_of_Instances.append(i.text)
print(len(No_of_Instances),No_of_Instances)


# In[143]:


noa=Driver.find_elements(By.XPATH,'//div[@class="my-2 hidden gap-4 md:grid grid-cols-12"]/div[4]')
for i in noa:
    if i.text is None :
        No_of_Attribute.append("--") 
    else:
        No_of_Attribute.append(i.text)
print(len(No_of_Attribute),No_of_Attribute)

