#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[6]:


# a series that we will reindex
np.random.seed(123456) 
s1 = pd.Series(np.random.randn(4), ['a', 'b', 'c', 'd'])
s1   


# In[3]:


# reindex with different number of labels
# results in dropped rows and/or NaN's
#.reindex()매소드는 Series에 대한 즉석변경이 아닌,복제된 Series에 새 인덱스 레이아웃
s2 = s1.reindex(['a', 'c', 'g'])
s2


# In[4]:


s2.index


# In[5]:


s2.values


# In[7]:


# different types for the same values of labels
# causes big trouble
#인덱스의 정수와 문자 레이블의 합계
#결측치 츨력 -자료형이 일치하지 않기 때문
s1 = pd.Series([0, 1, 2], index=[0, 1, 2])
s2 = pd.Series([3, 4, 5], index=['0', '1', '2'])
s1 + s2


# In[8]:


# reindex by casting the label types
# and we will get the desired result
#s2인덱스 값을 int로 변경
#values 는 인덱스의 값을 의미함 /뒤에 있는 값이 아님
s2.index = s2.index.values.astype(int)
s1 + s2


# In[19]:


s2 = s.copy()
s2


# In[24]:


s3 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
s3


# In[20]:


s3.reindex(np.arange(0,7))


# In[25]:


s3.reindex(np.arange(0,7), method='ffill')


# In[23]:


s3.reindex(np.arange(0,7), method='bfill')


# In[2]:


np.random.seed(123456)
s = pd.Series(np.random.randn(3), index=['a', 'b', 'c'])
s


# In[3]:


s['d'] = 100
s


# In[4]:


s['d'] = -100
s


# In[5]:


del(s['a'])
s


# In[6]:


copy = s.copy() # preserve s
slice = copy[:2] # slice with first two rows
slice


# In[7]:


# change item with label 10 to 1000
slice['b'] = 0
# and see it in the source
copy
#slice 변경해도 copy 함수의 원본데이터에도 반영됨/연결되어있음


# In[8]:


s


# In[46]:


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


# In[47]:


pd.DataFrame(np.arange(1, 6))


# In[48]:


df = pd.DataFrame(np.array([[10, 11], [20, 21]]))
df


# In[49]:


df.columns


# In[50]:


df = pd.DataFrame(np.array([[70, 71], [90, 91]]),
                  columns=['Missoula', 'Philadelphia'])
df


# In[51]:


len(df)


# In[52]:


df.shape


# In[53]:


temps_missoula = [70, 71]
temps_philly = [90, 91]
temperatures = {'Missoula': temps_missoula,
                'Philadelphia': temps_philly}
#컬럼 단위로 들어감
pd.DataFrame(temperatures)


# In[54]:


temps_at_time0 = pd.Series([70, 90])
temps_at_time1 = pd.Series([71, 91])
df = pd.DataFrame([temps_at_time0, temps_at_time1])
df
#제로베이스 포지션


# In[57]:


df = pd.DataFrame([temps_at_time0, temps_at_time1],
                  columns=['Missoula', 'Philadelphia'])#columns파라미터 지정
df


# In[58]:


df = pd.DataFrame([temps_at_time0, temps_at_time1])
df.columns = ['Missoula', 'Philadelphia']#columns 속성
df


# In[60]:


temps_mso_series = pd.Series(temps_missoula)
temps_phl_series = pd.Series(temps_philly)
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series})
#앞은 columns뒤는 value
df


# In[ ]:


# temps_nyc_series = pd.Series([85, 87], index=[1, 2])
df = pd.DataFrame({'Missoula': temps_mso_series,
                   'Philadelphia': temps_phl_series,
                   'New York': temps_nyc_series})
df
#뉴욕 추가
#일치하지 않는 인덱스 값 결측치


# In[75]:


# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data_an/data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])


# In[76]:


sp500.head()


# In[77]:


len(sp500)


# In[78]:


sp500.shape


# In[79]:


sp500.size


# In[80]:


sp500.index


# In[82]:


sp500.columns
#symbol 은 인덱스 값


# In[8]:


print("hello",end='')
print("hello")

