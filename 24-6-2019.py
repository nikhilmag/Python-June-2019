#!/usr/bin/env python
# coding: utf-8

# def printEven(n):
#     cnt=0;
#     sum=0;
#     while(cnt!=n):
#         if(cnt%2==0):
#             sum=sum+cnt;
#         cnt=cnt+1;
#     return sum;
# print(printEven(20));      
#         
# 
#         

# In[28]:


def factors(n):
    i=1;
    while(i!=n):
        if(n%i==0):
            print(i,end=" " );
        i=i+1;
    return;
factors(462);


# # LISTS

# In[18]:


list1=[1,2,3,4,5];
print(list1);
print(list1[0])


# In[45]:


list2=["SAII",123,1,2,3,4,5,6,7];
for x in (list2):
 print(x,end= " " )

print();
print(list2[0])
print(list2[1:7])
print(list2[:3])
print(list2[:9])


# 

# In[66]:


list1=[1,2,3,4,5,6,7,8,9,10];
for x in list1:
    print(x,end=" ")
print()
print(list1[1:-1])
print(list1[2:-2])
print(list1[100:-100])
print(list1[::2])
print(list1[::3])
print(list1[::-3])
print(list1[-2])


# In[116]:


list1=["SAI","Sai"]
print(list1)

list1[1]=189;
print(list1)
del list1[0]
print(list1)
list2=[1,2,3,4,5,6,7,89];
print(list2);
print(list1+list2);
print(len(list2))
list1.append(123);
print(list1)
print(len(list1+list2))
list1.append(1234);
list1.append(12534);
print(list1)
print(list1.count(189));
print(list1.count(19));
list1[2]=1234
print(list1)
list1=["Gitam","Python","C++",1,2,3,4,5,6,7,"Python"]
print(list1)
list1.index("Python")
list1.index(1)
list1.insert(2,123)
print(list1)


# In[104]:


list1=[1,2,3,4,5]
list1.insert(2,4)
print(list1)


# In[134]:


list1.pop(2)
print(list1)
list1.remove("python")
print(list1)


# In[155]:


list1=[1,"python",2,"gitam",3,4,5,6,7,8,90]
print(list1)
list1.reverse()
print(list1)
x=list1[7]
print(x)
print (x[::-1])


# In[5]:


def linearsearch(a,taritem):
    flag=0;
    for i in range(len(a)):
        if a[i]==taritem:
            flag=1;
            break
    if(flag!=0):
            print("FOUND")
    else:
            print("NOT FOUND")
a=[1,56,987,4,56,3456,56]
linearsearch(a,56)


# In[1]:


def linearsearchdup(a,taritem):
    
    flag=0;
    for i in range(len(a)):
        if a[i]==taritem:
            flag=flag+1
    print(flag)    
    if(flag>=2):
        print("DUPLICATE FOUND",flag)
    
  
    
a=[1,56,987,4,56,3456,56,4,3456,1,56,56,56,56,56,56,56]  
linearsearchdup(a,56)


# In[18]:


def linearsearchex(a,taritem):
    for i in range(len(a)):
        if(a[i]==taritem):
            print(i,end=" ")
    
a=[1,5,9,6,5,15,12,5]
linearsearchex(a,5)


# In[19]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
            print(i,end=" ")

a=[1,2,3,4,4,5,6,7,8]
linearexample(a,4)


# In[47]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
                

            j=0
            while(j!=i):
                print("!",end =" ")
                j=j+1;
            print(end="  ")
           
            
                
            
           

a=[1,2,3,4,4,5,6,7,8]
linearexample(a,4)


# In[49]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
            i="!"
            print(i,end=" ")

a=[1,2,3,4,4,4,5,6,7,8]
linearexample(a,4)


# In[69]:


def linear1(a):
    sum=0;
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
    print(sum)
a=[15,12,2,9,18,36,45]
linear1(a)


# In[74]:


def linear2(a):
    while(a[i]!=0):
        a[i]=a[i-1]*a[i+1]
    print(a[i])
    
    
    
a=[1,2,3,4,5]    
linear2(a)


# In[ ]:




