#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import numpy and pandas
import numpy as np 
import pandas as pd

#used for dates
import datetime
from datetime import datetime, date

#set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

#bring in matplotlib for graphics .%matplotlib inline 쥬피터 노트북 실행한 브라우저
import matplotlib.pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#create a series of multiplevalues from a list
s=pd.Series([10,11,12,13,14])
s


# In[4]:


#value stored at index label 3s
s[3]


# In[ ]:


#create a sequence of 5 values, all 2
pd.Series([2]*5)


# In[6]:


#use each charactor as a value
pd.Series(list('abcde'))


# In[7]:


#create Series from dict
pd.Series({'Mike': 'Dad',
          'Marcia': 'Mom',
          'Mikael': 'Son',
          'bleu': 'Best doggie ever' })


# In[8]:


#4 through 8
pd.Series(np.arange(4,9))


# In[9]:


#0 tthrough 9
pd.Series(np.linspace(0,9,5))


# In[10]:


#random numbers
np.random.seed(12345)#always generate the same values
#5 normally random numbers
pd.Series(np.random.normal(size=5))


# In[11]:


np.random.rand(10)
#무작위 수 10개


# In[12]:


#create the Series
s=pd.Series(np.arange(0,5))
#multiple all values by 2
s*2


# In[13]:


v=pd.Series([1,2,3])
v


# In[14]:


#get the values in the Series
s=pd.Series([1,2,3])
s.values


# In[15]:


#show that this is a numpy array
type(s.values)


# In[16]:


#get the index of the Series
s.index


# In[17]:


#example series
s=pd.Series([0,1,2,3])
len(s)


# In[18]:


#.size is also the #of items in the Series
s.size


# In[19]:


#.shape is a tuple with one value
s.shape


# In[20]:


#explicitly create an index
labels=['Mike', 'Marcia', 'Mikael', 'Bleu']
role=['Dad', 'Mom', 'Son', 'Dog']
s=pd.Series(labels,index=role)
s


# In[21]:


#examine the index
s.index


# In[22]:


#who is Dad?
s['Dad']


# In[23]:


s[3]


# In[24]:


#a ten item Series
s=pd.Series(np.arange(1,10),
           index=list('abcdefghi'))
s


# In[25]:


#show the first five
s.head()


# In[26]:


#the first three
s.head(n=3)#s.head(3)is equivalent


# In[27]:


#the last five
s.tail()


# In[28]:


#the last 3
s.tail(n=3)#equivalent to s.tail(3)


# In[29]:


#only take specific items by position
s.take([1,5,8])


# In[30]:


#we will use this series to examine lookups
s1=pd.Series(np.arange(10,15), index=list('abcde'))
s1


# In[31]:


#get the value with label 'a'
s1['a']


# In[32]:


#get multiple items
s1[['d','b']]


# In[33]:


#gets values based upon position
s1[[3,1]]


# In[34]:


#to demo lookup by matching labels as integer values
s2=pd.Series([1,2,3,4],index=[10,11,12,13])
s2


# In[36]:


#this is by label not position
s2[[13,10]]


# In[43]:


s2[[3,1]]#오류#충돌이 일어남


# In[39]:


#explicitly by position
s1.iloc[[0,2]]


# In[40]:


#to demo lookup by matching labels as integer values
s3=pd.Series([1,2,3,4],index=['a','b','c','d'])
s3


# In[41]:


#this is by label not position
s3[[1,2]]

