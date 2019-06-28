#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class className:
    #some fn and variables
    #variables--Data(memory)
    #function--used to perform specific activity
    
    


# In[3]:


def Test():
    print('Test() for function')
    return
Test()


# In[2]:


class Demo:
    def test(self):
        print("test() for the class and method")
        return
obj=Demo()
obj.test()


# In[7]:


class Demo1:
    def fact(self,n):
        #return the factorial
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
p1=Demo1()
print(p1.fact(5))#120


# In[ ]:


#method
# def test(self,para1,para2)
class Demo2:(a,b)
    def accept(self,p1,p2):
        a=p1
        b=p2
        return
    def display(self):
        print("p1,a)
        print("p2b)
c1=Demo2()
c1.accept(10,20)
              z

        


# In[15]:


class Demo2:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    def add(self,p1,p2):
        return p1+p2
c1=Demo2(10,20)
print(c1.add(100,200))


# In[35]:


#Some inheritence
class Person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
#Derive Class
class Employee(Person):
    def isEmployee(self):
        return True
emp=Person("TEJAS")
print(emp.getName(),emp.isEmployee())
emp1=Employee("TEJA")
print(emp1.getName(),emp1.isEmployee())


# In[ ]:





# In[26]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
array+10
print(array)


# In[25]:


lst=[1,2,3,4]
array=np.array(lst)
print(array.shape)
print(array.dtype)


# In[23]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array)


# In[28]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)


# In[29]:


lst=[1,2,3,4]
array=np.array(lst)
print(array)
print(array.shape)
print(array.dtype)


# In[31]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[35]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[36]:


#randon mo from np
a1=np.random.normal([5,0.5,10])
print(a1)


# In[41]:


np.zeros((2,2))


# In[42]:


np.zeros((2,2),dtype=np.int64)


# In[44]:


np.ones((4,3),dtype=np.int64)


# In[48]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
print(A)


# In[50]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[2]=5
print(A)


# In[52]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[1][3]=51
np.asarray(A)[3][3]=512
print(A)


# In[56]:


#  arrange() --particular
#num.py arrange(star,and,step)
# start=value
#end=value
#step =gap bw one value to another
import numpy as np
np.arange(1,10)


# In[59]:


np.arange(1,100,9)


# In[60]:


np.arange(2,20,2)
np.arange(1,25,2)


# In[62]:


#Indexing and slicing
a1=np.array([(1,2,3),(4,5,6)])
print(a1)


# In[76]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row :",a1[0])


# In[72]:


a1=np.array([(1,2,3),(4,5,6)])
print("Slicing  Coloumn :",a1[:,1])


# In[69]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row :",a1[1])


# In[75]:


a1=np.array([(1,2,3),(4,5,6)])
print("Slicing Last Coloumn :",a1[:,2])


# In[74]:


a1=np.array([(1,2,3),(4,5,6)])
print("Slicing  row :",a1[:1,])


# In[83]:


#min=least,max=large,mean,median,Gd=GAUSSIAN DISTRIBUTION

a1=np.random.normal(5,1,10)
print("A=",a1)
print("MIN VALUE=",np.min(a1))
print("MAX VALUE=",np
.max(a1))
print("MEAN VALUE=",np.mean(a1))
print("MEDIAN VALUE=",np.median(a1))


# In[84]:


#MULTIPLY 1D ARRAYS
c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)



# In[90]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(4,5),(1,2)])
np.dot(c1,c2)


# In[91]:


b1=np.array([(1,5),(6,9)])
b2=np.array([(1,3),(1,6)])
np.matmul(b1,b2)


# In[92]:


##PANDAS  BASICS


# In[104]:


import pandas as pd
dict={"Name":["TEJAS","RAJU","DAARU","VINAY","RAMU"],
      "EMAILID":["tejas@gmail.com","raju@gmail.com","daaru@gmail.com","vinay@gmail.com","ramu@gmail.com"],
      "MOBILE":[999,555,666,888,333],
      "ADDRESS":["HYD","HYD","HYD","HYD","HYD"]}
b=pd.DataFrame(dict)
print(b)


# In[103]:


b.index=["01","02","03","04","05","06"]
print(b)


# In[110]:


import pandas as pd
dict1={"Name":["Anil","Amith","Dinesh","ajay","Kranth"],"Email":["anil@gamil.com","Amith@gmail.com","Dinesh@gmail.com", "ajay@gmail.com","kranth@gmail.com"],"Mobile Number":[999,777,888,777,999],"Address":["Hyd","Hyd","Hyd","Hyd","Hyd"]}
b=pd.DataFrame(dict1)
print(b)


# In[112]:


import pandas as p
productsellingdata =pd.read_csv("FileName.csv")
print(products)


# In[113]:


import pandas as pd
dict={"name":["rakesh","surya","pavan"],
     "email id":["rakeshkankala@gmail.com","suryagarikapathi@gmail.com","pavannadakumar@gmail.com"],
     "mobile number":[8790490360,9100423511,8374193886],
     "adress":["hyd","hyd","hyd"]}

b=pd.DataFrame(dict)
print(b)


# In[ ]:




