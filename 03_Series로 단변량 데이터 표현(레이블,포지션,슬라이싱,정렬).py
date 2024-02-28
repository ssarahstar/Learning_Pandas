#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date
pd.set_option('display.notebook_repr_html',False)
pd.set_option('display.max_columns',8)
pd.set_option('display.max_rows',10)
pd.set_option('display.width',80)
import matplotlib.pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv('../data/goog.csv')
df


# In[4]:


#display the contents of test1.csv
#which command to use depends on your os
get_ipython().system('head ../data/goog.csv #on non_windows systems')
#!type data/test1.csv #on windows systems, all lines


# In[5]:


df.Date
#object형식은 문자데이터를 의미함


# In[6]:


df.Date[0]


# In[7]:


type(df.Date[0])


# In[8]:


df1=pd.read_csv('../data/COVID 19 Cm data.csv', parse_dates=['DateStart'])
df1


# In[9]:


df1.DateStart


# In[10]:


type(df1.DateStart[0])#datetime 객체로 생성하려는 타임스탬프 값을 전달


# In[11]:


df1.index


# In[12]:


df=pd.read_csv('../data/COVID 19 Cm data.csv',
              parse_dates=['DateStart'],
              index_col='DateStart')
df


# In[13]:


df=pd.read_csv('../data/goog.csv',
              parse_dates=['Date'],
              index_col='Date')
df


# In[14]:


df.index


# In[15]:


df.Close.plot();


# In[63]:


# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[52]:


s1 = pd.Series(np.arange(10, 15), index=list('abcde'))
s1


# In[54]:


s1.iloc[[0,2]]


# In[56]:


s2 = pd.Series([1, 2, 3, 4], index=[10, 11, 12, 13])
s2


# In[57]:


s2


# In[58]:


s2.iloc[[3,2]]


# In[59]:


s1.loc[['a','d']]


# In[60]:


s1.iloc[[1,3]]


# In[61]:


s2.loc[[11,12]]


# In[65]:


s=pd.Series(np.arange(100,110), index=np.arange(10,20))
s


# In[66]:


s[1:6]


# In[67]:


s.iloc[[1,2,3,4,5]]


# In[69]:


s[1:6:2]


# In[70]:


s[:5]


# In[71]:


s[4:]


# In[72]:


s[:5:2]


# In[73]:


s[4::2]


# In[74]:


s[::-1]
#역순정렬


# In[75]:


s[4::-2]


# In[76]:


s[-4:]


# In[77]:


s[:-4]


# In[78]:


s[-4:-1]


# In[79]:


s=pd.Series(np.arange(0,5),
           index=['a','b','c','d','e'])
s


# In[80]:


s[1:3]


# In[84]:


s['b':'d']


# In[85]:


s1=pd.Series([1,2], index=['a','b'])
s1


# In[86]:


s2=pd.Series([4,3], index=['b','a'])
s2


# In[87]:


s1+s2


# In[88]:


s1*2


# In[89]:


t=pd.Series(2,s1.index)
t


# In[90]:


s1*t


# In[91]:


s3=pd.Series([5,6], index=['b','c'])
s3


# In[92]:


s1+s3
#동일한 인덱스가 없을 때 NaN반환


# In[95]:


s1=pd.Series([1.0,2.0,3.0],index=['a','a','b'])
s1


# In[93]:


s2=pd.Series([4.0,5.0,6.0,7.0],index=['a','a','c','a'])
s2


# In[96]:


s1+s2

