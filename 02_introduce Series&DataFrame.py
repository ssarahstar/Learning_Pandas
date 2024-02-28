#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import numpy and pandas
import numpy as np #Numpy는 행렬,다차원 배열 지원하는 파이썬의 라이브러리,데이터 구조,수치 계산
import pandas as pd

#used for dates
import datetime
from datetime import datetime, date

#set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 80)

#bring in matplotlib for graphics
import matplotlib.pyplot as pit
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#create a four item Series
s=pd.Series([1,2,3,4])
s


# In[4]:


#get value at label 1
s[1]


# In[5]:


#return a Series with the row with labels 1 and 3
s[[1,3]]


# In[6]:


#create a series using an explicit index
s=pd.Series([1,2,3,4],
           index=['a', 'b', 'c', 'd'])
s


# In[7]:


#look up items the series having index 'a' and 'd'
s[['a','d']]


# In[8]:


#passing a list of integers to a Series that has
#non-integer index labels will look up based upon
#0-based index like an array
s[[1,2]]


# In[9]:


#get only the index of the Series
s.index


# In[8]:


#create a Series who's index is a series of dates
#between the two specified dates (inclusive)
dates=pd.date_range('2016-04-01' , '2016-04-06')
dates


# In[9]:


#create a Series with values (representing temperatures)
#for each date in the index
temps1=pd.Series([80,82,85,90,83,87],
                index=dates)
temps1


# In[10]:


#what's the temperation for 2016-4-4?
temps1['2016-04-04']


# In[11]:


#create a second series of values using the same index
temps2=pd.Series([70,75,69,83,79,77],
                index=dates)
#the following aligns the two by their index values
#and calculates the difference at those matching labels
temp_diffs=temps1-temps2
temp_diffs


# In[12]:


#and alse possible by integer position as if the
#series was an array
temp_diffs[2]


# In[13]:


#calculate the mean of the values in the Series
temp_diffs.mean()


# In[14]:


#create a DataFrame from the two series objests temp1 and temp2
#and give them column names
temps_df=pd.DataFrame(
            {'Missoula':temps1,
            'Philadelphia':temps2})
temps_df


# In[15]:


#get the column with the name Missoula
temps_df['Missoula']


# In[16]:


#likewise we can get just the philadelphia column
temps_df['Philadelphia']


# In[17]:


#return both colums in a different order
temps_df[['Philadelphia','Missoula']]


# In[18]:


#retrieve the Missoula column through property syntax
temps_df.Missoula


# In[19]:


#calculate the temperature difference between the two cities
temps_df.Missoula-temps_df.Philadelphia


# In[20]:


#add a column to temps_df which contains the difference in temps
temps_df['Difference']=temp_diffs
temps_df


# In[21]:


#add a column to temp_df which contains the difference in temps
temps_df['Difference']=temp_diffs
temps_df


# In[22]:


#get the colums which is also an index object
temps_df.columns


# In[23]:


#slice the temp differences column for the rows at
#location 1 through 4(as though it is an array)
temps_df.Difference[1:4]


# In[36]:


#get the row at array position 1
temps_df.iloc[1]


# In[34]:


#the name of the columns have become the index
#they have been 'pivoted'
temps_df.iloc[1].index


# In[30]:


#retrieve row by index label using .loc
temps_df.loc['2016-04-05']


# In[33]:


#get the values in the Differences column in tows 1,3 and 5
#using 0-based lacation
temps_df.iloc[[1,3,5]].Difference


# In[34]:


#which values in the Missoula column are >82?
temps_df.Missoula>82


# In[35]:


#return the rows where the temps for Missoula>82
temps_df[temps_df.Missoula>82]

