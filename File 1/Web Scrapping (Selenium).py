#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Qs1 In this question you have to scrape data using the filters available on the webpage You have to use the location and 
#salary filter from page https://www.naukri.com/. 
import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

import regex as re


# In[ ]:


driver=webdriver.Chrome()


# In[ ]:


driver.get('https://www.naukri.com/')


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[7]/div/div/div[6]')
search.click()


# In[ ]:


Location=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[5]/div[2]/div[2]/label")
Location.click()


# In[ ]:


Salary=driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[6]/div[2]/div[4]/label")
Salary.click()


# In[ ]:


Job_Title=[]
Job_location=[]
Company_name=[]
Experience=[]

Titles=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in Titles[0:10]:
    Job_Title.append(i.text)
 
Company=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in Company[0:10]:
    Company_name.append(i.text)
    
Location=driver.find_elements(By.XPATH,'//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-location loc"]/span')
for i in Location[0:10]:
    Job_location.append(i.text)
    
WorkEx=driver.find_elements(By.XPATH,'//span[@class="ni-job-tuple-icon ni-job-tuple-icon-srp-experience exp"]/span')
for i in WorkEx[0:10]:
    Experience.append(i.text)   


# In[ ]:


Data=pd.DataFrame({'Title':Job_Title,'Location':Job_location,'Company':Company_name,'Experience':Experience})
Data


# In[ ]:


#Qs2 Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the 
#job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. 
drive=webdriver.Chrome()

drive.get('https://www.shine.com/')


# In[ ]:


d=drive.find_element(By.XPATH,'//li[@class="searchForm_search_item__hr6Du form-group "]/div/input')
d.send_keys('Data Analyst')  


# In[ ]:


l=drive.find_element(By.XPATH,'//li[@class="searchForm_search_item__hr6Du form-group"]/div/input')
l.send_keys('Bangalore')


# In[ ]:


s=drive.find_element(By.XPATH,'/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button')
s.click()


# In[ ]:


J_Title=[]
J_location=[]
Comp_name=[]
Exp=[]

Title=drive.find_elements(By.XPATH,'//strong[@class="jobCard_pReplaceH2__xWmHg"]')
for i in Title[0:10]:
    J_Title.append(i.text)
    
Comp=drive.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
for i in Comp[0:10]:
    Comp_name.append(i.text)
    
Work=drive.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[1]')
for i in Work[0:10]:
    Exp.append(i.text)
    
Loc=drive.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists__fdnsc"]/div[2]')
for i in Loc[0:10]:
    J_location.append(i.text)


# In[ ]:


Shine_Data=pd.DataFrame({'Title':J_Title,'Location':J_location,'Company':Comp_name,'Experience':Exp})
Shine_Data


# In[ ]:


#Qs3 Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 

G=webdriver.Chrome() 
    
G.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYHWAXCG&marketplace=FLIPKART&q=iphone+11+black+64+gb&store=tyy/4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=724b1e99-d256-4da7-9c49-aa404d3b0303.MOBFWQ6BXGJCEYNY.SEARCH&ppt=browse&ppn=browse&ssid=txloplv3ps0000001712651884066&qH=5f530f2df85791a0')


# In[ ]:


R=G.find_element(By.XPATH,'//div[@class="_3UAT2v _16PBlm"]')
R.click()


# In[ ]:


Rating=[]
Review=[]
Full=[]
starts=0
ends=11
for i in range(starts,ends):
    rate=G.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for j in rate:
        Rating.append(j.text)
    rev=G.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for j in rev:
        Review.append(j.text)
    full_rev=G.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for j in full_rev:
        Full.append(j.text)
        
    nextb=G.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    nextb.click()
    time.sleep(3) 


# In[ ]:


Iphone_Data=pd.DataFrame({'Rating':Rating[0:100],'Review':Review[0:100],'Full Review':Full[0:100]})
Iphone_Data


# In[ ]:


#Qs4 Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 

d=webdriver.Chrome() 
    
d.get('https://www.flipkart.com/')


# In[ ]:


a=d.find_element(By.XPATH,'//div[@class="_2SmNnR"]/input')
a.send_keys('Sneakers')


# In[ ]:


b=d.find_element(By.XPATH,'//button[@class="_2iLD__"]')
b.click()


# In[ ]:


Brand=[]
Price=[]
Show=[]
start=0
end=3
for page in range(start,end):
    brand=d.find_elements(By.CLASS_NAME,'_2WkVRV')
    brand[0:100]
    for i in brand[0:100]:
        Brand.append(i.text)
    price=d.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price[0:100]:
        Price.append(i.text)
        
    nextbutton=d.find_element(By.XPATH,'//nav[@class="yFHi8N"]/a/span')
    nextbutton.click()
    time.sleep(3)  


# In[ ]:


Sneaker_Data=pd.DataFrame({'Brand':Brand[0:100],'Price':Price[0:100]})
Sneaker_Data


# In[213]:


#Qs5 Scrape first 10 laptops data. You have to scrape 3 attributes for each laptop: Title, Ratings and Price 

H=webdriver.Chrome()
H.get('https://www.amazon.in/')


# In[214]:


Amazon=H.find_element(By.XPATH,'//div[@class="nav-search-field "]/input')
Amazon.send_keys('Laptop')


# In[215]:


Amazonclick=H.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]')
Amazonclick.click()


# In[218]:


Laptitle=[]
Lapprice=[]
Laprating=[]

laptitle=H.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in laptitle:
    Laptitle.append(i.text)

lapprice=H.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in lapprice:
    Lapprice.append(i.text)
    
Laptop_data=pd.DataFrame({'Title':Laptitle[0:10],'Price':Lapprice[0:10]})
Laptop_data


# In[ ]:


#Qs6 Write a python program to scrape data for Top 1000 Quotes of All Time. 

J=webdriver.Chrome()

J.get('https://www.azquotes.com/')


# In[ ]:


Tquote=J.find_element(By.XPATH,'//div[@class="mainmenu"]/ul/li[5]/a')
Tquote.click()


# In[ ]:


Top_quote=[]
Author=[]
Quote_type=[]
st=0
en=10

for j in range(st,en):
    quote=J.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote:
        Top_quote.append(i.text)
    auth=J.find_elements(By.XPATH,'//div[@class="author"]')
    for i in auth:
        Author.append(i.text)
    qtype=J.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in qtype:
        Quote_type.append(i.text)
    n=J.find_element(By.XPATH,'//div[@class="pager"]/li[12]') 
    n.click()
    time.sleep(3)


# In[ ]:


Quote_data=pd.DataFrame({'Quote':Top_quote,'Author':Author,'Quote Type':Quote_type})
Quote_data


# In[ ]:


#Qs7 Write a python program to display list of respected former Prime Ministers of India (Name,Born-Dead,Term of office,Remarks)

L=webdriver.Chrome()


# In[ ]:


look=L.get('https://www.jagranjosh.com/general-knowledge/list-ofall-prime-ministers-of-india-1473165149-1')


# In[ ]:


PMname=[]

pmname=L.find_elements(By.TAG_NAME,'tr')
for i in pmname:
    PMname.append(i.text)


# In[ ]:


df=pd.DataFrame({'PM Name':PMname})
df


# In[ ]:


#Qs8  Write a python program to display list of 50 Most expensive cars in the world (Car name and Price)
 
K=webdriver.Chrome()


# In[ ]:


K.get('https://www.motor1.com/')


# In[ ]:


CarName=[]
CarPrice=[]

search=K.find_element(By.XPATH,'//input[@class="m1-search-panel-input m1-search-form-text"]')
search.send_keys('50 most expensive cars')


# In[ ]:


clck=K.find_element(By.XPATH,'//button[@class="m1-search-panel-button m1-search-form-button-animate icon-search-svg"]')
clck.click()


# In[ ]:


clk=K.find_element(By.XPATH,'/html/body/div[9]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
clk.click()


# In[ ]:


cname=K.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in cname:
    CarName.append(i.text)
    
cprice=K.find_elements(By.TAG_NAME,'strong')
for i in cprice:
    CarPrice.append(i.text)


# In[ ]:


Car_data=pd.DataFrame({'Car Name':CarName[0:50],'Price':CarPrice[0:50]})
Car_data

