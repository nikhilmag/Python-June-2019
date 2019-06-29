#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a series of numbers by passing a list of values
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)


# In[2]:


#Missing values in a list
import numpy as np
a1=pd.Series([1,2,3,4,np.nan,6])
print(a1)


# In[6]:


dates=pd.date_range('20190601',periods=25)
print(dates)


# In[4]:


a2=pd.DataFrame({'A':1.,
                 'B':pd.Timestamp('20190601'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([3]*4,dtype='int32'),
                 'E':pd.Categorical(["test","train","test","train"]),
                 'F':"foo"})
print(a2)
                


# In[12]:


#step1:-make all the turtle package to be imported
import turtle as tt
# turtle method creates and returns new object
a1=tt.Turtle()
#forward() method moves 100 pixel
tt.forward(100)
tt.done()


# In[ ]:





# In[ ]:





# In[ ]:




