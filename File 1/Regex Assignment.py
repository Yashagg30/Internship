#!/usr/bin/env python
# coding: utf-8

# In[94]:


#Qs1-Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
import re

Data='Python Exercises, PHP exercises.'
Answer=re.sub('\W',':',Data)
Answer


# In[95]:


#Qs2-Create a dataframe using the dictionary below and remove everything from the columns except words.

import pandas as pd

df=pd.DataFrame({'SUMMARY':['hello, world!', 'XXXXX test', '123four, five:; six...']})

pattern='\W+|XXXXX|[0-9+]'
df['SUMMARY'].str.replace(pattern,' ')


# In[96]:


#Qs3-Create a function in python to find all words that are at least 4 characters long in a string. 
#The use of the re.compile() method is mandatory.

def Yash(Data):
    pattern=re.compile(r"\w{4}")
    for match in pattern.finditer(Data):
        print(match.group())
        
Yash("Hello World, I am Yash Aggarwal. I live in Delhi. I work at British Airways!")


# In[97]:


#Qs4-Create a function in python to find all three, four, and five character words in a string. 
#The use of the re.compile() method is mandatory.

def Yash1(Data):
    pattern=re.compile(r"\w{3,5}")
    for match in pattern.finditer(Data):
        print(match.group())
        
Yash1("Hello World, I am Yash Aggarwal. I live in Delhi. I work at British Airways!")


# In[98]:


# Qs5-Create a function in Python to remove parenthesis in a list of strings. 
#The use of the re.compile() method is mandatory.

import re

def Yash(*args):
    pattern=re.compile("|\(|\)")
    for i in Sample:
        Result=re.sub(pattern,"",i)
        print(Result)
        
    
Sample=["example(.com)", "hr@fliprobo(.com)", "github(.com)", "Hello (Data Science World)", "Data (Scientist)"]
Yash(Sample)


# In[99]:


#Qs6-Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
import re
import pandas as pd

f=open('text.txt','r')
Text=f.read()
Result=re.sub("|\(|\)","",Text)
    
print(Result)
        


# In[100]:


#Qs7-Write a regular expression in Python to split a string into uppercase letters.

Sample="ImportanceOfRegularExpressionsInPython"

x=re.findall("([A-Z][a-z]+)",Sample)
print(x)


# In[101]:


#Qs8-Create a function in python to insert spaces between words starting with numbers.

#data='RegularExpression1IsAn2ImportantTopic3InPython'
patt=r'(\d)+'
def Agg(data):
        a=re.sub(patt,lambda x:" "+x[0],data)
        print(a)

data='RegularExpression1IsAn2ImportantTopic3InPython'
Agg(data)



# In[102]:


#Qs9-Create a function in python to insert spaces between words starting with capital letters or with numbers.
    
patt=r'[A-Z]|(\d)+'
def Agg(data):
        a=re.sub(patt,lambda x: " "+x[0],data)
        print(a)

data='RegularExpression1IsAn2ImportantTopic3InPython'
Agg(data)


# In[154]:


#Qs10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.

import pandas as pd

Url=pd.read_csv('https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv')
df=pd.DataFrame(Url)

pattern=r'(\w{6})'
Cntry=Url['Country'].str.extract(pattern,expand=True)
df['First_five_letters']=Cntry

Url


# In[105]:


#Qs11-Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

Sample='dbsbbs@b3335'

pat=r'^[\w]+$'
if re.match(pat,Sample):
    print('Match found')
else:
    print('No match')


# In[106]:


#Qs12-Write a Python program where a string will start with a specific number.
Sample='47sbbsb@3335'

pat=r'^4'
if re.match(pat,Sample):
    print('Match found')
else:
    print('No match')


# In[107]:


#Qs13-Write a Python program to remove leading zeros from an IP address
IP="128.06.0302.172"

Final=re.sub('\.0+','.',IP)
print(Final)


# In[111]:


#Qs14-Write regular expression in python to match date string in the form of Month followed by day and year stored in text file.

A=open('Yash.txt','r')
file=A.read()

pa=r'([A-Z][a-z]+) \d{1,2}(?:th|rd|nd) \d{4}'

Final=re.search(pa,file)
print(Final)


# In[112]:


#Qs15-Write a Python program to search some literals strings in a string.

txt='The quick brown fox jumps over the lazy dog.'

#Searched words : 'fox', 'dog', 'horse'

Z=re.findall("fox|dog|horse",txt)
Z


# In[113]:


#Qs16- Write a program to search a literals string in a string and also find the location within the original string.

Samp='The quick brown fox jumps over the lazy dog.'

Y=re.search("fox",Samp)
Y


# In[114]:


#Qs17-Write a Python program to find the substrings within a string.

Sam='Python exercises, PHP exercises, C# exercises'

X=re.findall("exercises",Sam)
X


# In[116]:


#Qs18-Write a Python program to find the occurrence and position of the substrings within a string.

Sam='The quick brown fox jumps over the lazy dog. The fox then ran away. fox'
pattern=re.compile('fox')
for i in pattern.finditer(Sam):
    print(i)


# In[117]:


#Qs19-Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

Date="2023-12-23"
Converted=Date[8:]+'-'+Date[5:7]+'-'+Date[:4]
print(Converted)


# In[118]:


#Qs20-Create a function to find all decimal numbers with a precision of 1 or 2 in a string.
s="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

find=re.compile(r"\d+\.\d{1,2}")
for i in find.finditer(s):
        print(i.group())


# In[119]:


#Qs21-Write a Python program to separate and print the numbers and their position of a given string.

U='The 2 quick brown foxes jumps over 1 lazy dog. The 2 foxes then ran away to their group of 20.'
find=re.compile(r"\d+")
for i in find.finditer(U):
        print(i)


# In[120]:


#Qs22-Write a regular expression in python program to extract maximum/largest numeric value from a string.

marks='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

find=re.compile(r"\d+")
b=find.findall(marks)
print("maximum marks:",max(b))


# In[123]:


#Qs23-Create a function in python to insert spaces between words starting with capital letters.

H="RegularExpressionIsAnImportantTopicInPython"

patt=r'[A-Z]|(\d)+'
def Agga(data):
        a=re.sub(patt,lambda x:" "+x[0],data)
        print(a)

Agga(H)


# In[124]:


#Qs24- Write a Python regex to find sequences of one upper case letter followed by lower case letters

H="RegularExpressionIsAnImportantTopicInPython"

f=re.findall('([A-Z][a-z]+)',H)
print(f)


# In[125]:


#Qs25-Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

P="Hello hello world world"

regex=r'\b(\w+)(?:\W+\1\b)+'
d=re.sub(regex,r'\1',P)
d


# In[126]:


#Qs26-Write a python program using RegEx to accept string ending with alphanumeric character.

pattern=re.compile(r'[A-Za-z0-9]$')
def check(data):
    if re.search(pattern,data):
            print("Accept")
    else:
            print("Deny")
                   
check('can8@')
check('yash9')


# In[127]:


#Qs27-Write a python program using RegEx to extract the hashtags.
Z="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

Y=re.findall(r'(#[\w]+)',Z)
print(Y)


# In[128]:


#Qs28-Write a python program using RegEx to remove <U+..> like symbols

U="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern=re.compile(r'(<U\+[0-9A-Za-z]+>)')
J=re.sub(pattern,'',U)
print(J)


# In[129]:


#Qs29-Write a python program to extract dates from the text stored in the text file.

Q=open('Date.txt','r')
File=Q.read()

Result=re.findall(r"(\d{1,2}-\d{1,2}-\d{4})",File)
    
print(Result)


# In[130]:


#Qs30-Create a function in python to remove all words from a string of length between 2 and 4.

L="The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

H=re.compile(r'\b\w{2,4}\b')

Result=re.sub(H,'',L)
Result

