#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[6]:


# slice showing items at position 1 thorugh 5
s[1:6]


# In[7]:


#lookup via list of positions
s.iloc[[1,2,3,4,5]]


# In[8]:


#items at position 1,3,5
s[1:6:2]


# In[9]:


# first five by slicing, same as .head(5)
s[:5]
#초기값이 없을 때는 0부터


# In[10]:


# fourth position to the end
s[4:]
#종료값이 없을 때는 끝까지


# In[11]:


# every other item in the first five positions
s[:5:2]


# In[12]:


# every other item starting at the fourth position
s[4::2]


# In[13]:


#reverse the Series
s[::-1]
#역순


# In[14]:


# every other starting at position 4, in reverse
s[4::-2]
#역순


# In[15]:


#-4:, which means the last 4 rows
s[-4:]


# In[16]:


#:-4, all but the last 4
s[:-4]


# In[17]:


# equivalent to s.tail(4).head(3)
s[-4:-1]


# In[19]:


# used to demonstrate the next two slices
s = pd.Series(np.arange(0, 5), 
              index=['a', 'b', 'c', 'd', 'e'])
s


# In[20]:


# slices by position as the index is characters
s[1:3]


# In[21]:


# this slices by the strings in the index
s['b':'d']


# In[22]:


# First series for alignment
s1 = pd.Series([1, 2], index=['a', 'b'])
s1


# In[25]:


#Second series for alignment
s2=pd.Series([4,3],index=['b','a'])
s2


# In[27]:


#add them
s1+s2
#인덱스 레이블의 순서가 달라도 같은 데이터가 있다면 가능하다는 결론


# In[28]:


#multiply all values in s3 by 2
s1*2


# In[29]:


#scalar series using s3's index
t=pd.Series(2,s1.index)
t


# In[30]:


#multiply s1 by t
s1*t


# In[33]:


# we will add this to s1
s3 = pd.Series([5, 6], index=['b', 'c'])
s3


# In[34]:


# s1 and s3 have different sets of index labels
# NaN will result for a and c
s1 + s3
#동일한 인덱스가 없는 경우
#오류가 아닌 결측치로 나옴
#float로 출력됨 결측치 데이터 자료형의 특징은 float형(실수형)


# In[35]:


# 2 'a' labels
s1 = pd.Series([1.0, 2.0, 3.0], index=['a', 'a', 'b'])
s1


# In[36]:


#3 a labels
s2 = pd.Series([4.0, 5.0, 6.0, 7.0], index=['a', 'a', 'c', 'a'])
s2


# In[37]:


# will result in 6 'a' index labels, and NaN for b and c
s1 + s2
#데카르트 기법 
#데카르트 곱
#순서가 달라지면 결과가 달라짐
#일반적인 더하기 연산과 다름 


# In[14]:


#불리언 선택
# which rows have values that are > 5?
s = pd.Series(np.arange(0, 5), index=list('abcde'))
logical_results = s >= 3
logical_results


# In[3]:


# select where True
s[logical_results]


# In[15]:


#a little shorter version
s[s>2]


# In[5]:


# commented as it throws an exception
# s[s >= 2 and s < 5]


# In[6]:


# correct syntax
s[(s >=2) & (s < 5)] #논리식 / 또는 &


# In[16]:


#are all items>=)?
(s>= 0).all ()#모든 조건이 만족하는지 확인
#시험문제 잘 나옴


# In[17]:


#any items<2?
s[s<2].any() #조건이 만족하는 값이 하나라도 있으면 True 반환
#시험문제 잘 나옴


# In[18]:


#how many values<2?
(s<2).sum()#조건을 만족하는 아이템의 개수


# In[19]:


(s<2).any()


# In[20]:


s[s>=0].all()


# In[21]:


s[s<2].sum()

