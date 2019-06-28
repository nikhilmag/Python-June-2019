#!/usr/bin/env python
# coding: utf-8

# In[26]:


def binarysearch(a,lindex,rindex,taritem):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2;
        if a[mindex]==taritem:
            return mindex
        if a[mindex]>taritem:
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1
list1=[1,2,3,4,5,6,7,8]
res=binarysearch(list1,0,7,3) 
if res!=-1:
    print("ITEM IS FOUND")
else:
    print("ITEM IS NOT FOUND")


# In[29]:


##Bubble Sort
def bubblesort(a):
    for i in range(len(a)-1):
         for j in range(len(a)-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
list2=[18,3,533,5,779,1]
bubblesort(list2)


# In[42]:


list2=[18,3,533,5,779,1]
list2.sort()
print(list2)


# In[40]:


str="application"
print(str)
str='application'
print(str)
str2="""application list working python"""
print(str2)


# In[60]:


str="application"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-1]=",str[-1])
print("str[-5]=",str[-5])
print("str[1::5]=",str[1::5])
print("str[5::-2]=",str[1::5])
print("str[::6]=",str[::6])
print("str[::]=",str[::])
print("str[0::5]=",str[0::5])


# In[63]:


def ispalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(ispalindrome("python"))    
print(ispalindrome("malayalam"))    


# In[64]:


#DIGITS
n=int(input("enter a number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)    


# In[66]:


#digits strlen
def countofchar(str):
    return len(str)
countofchar("applhhiutogi")


# In[67]:


#digits strlen
def countofchar(n):
    return len(n)
countofchar("1234")


# In[110]:


def countofupchar(str):
    cnt=0;
    
    for i in range(len(str)):
        if(str[i]>='A'or str[i]<='Z'):
            cnt=cnt+1
        else:
        
        return(cnt)
print(countofupchar("saataaASDFGJHIJJLK"))


# In[117]:


def countofupchar(str):
    cnt=0;
    list1=list(str)
    for x in range(len(list1)):
        if ord(list1[x])>=65 and ord(list1[x])<=90:
            cnt=cnt+1
    return cnt       
    
print(countofupchar("ASTsaas"))    


# In[111]:


str1="H"
str2="h"
str1.isupper()


# In[113]:


str1="H"
str2="h"
str1.islower()


# In[164]:


def printdigits(str):
    lst=list(str)
    for i in range(len(lst)):
        if  ord(lst[i])>=48 and ord(lst[i])<=57:
                
           print(lst[i])
         
  
    
print(printdigits("ASTsaa56s"))    


# In[190]:


def printdigitss(str):
    sum=0
    lst=list(str)
    for i in range(len(lst)):
         if  ord(lst[i])>=48 and ord(lst[i])<=57:
                a=int(lst[i]);
                sum=sum+a;
    return(sum);            
             
print(printdigitss("ASTsaa98s"))    


# In[225]:


def printdigitss(str):
    sum=0
    lst=list(str)
    for i in range(len(lst)):
         if  ord(lst[i])>=48 and ord(lst[i])<=57:
                if (ord(lst[i])%2==0):
                    sum=sum+ord(lst[i])-48;
    return(sum);            
             
printdigitss("ASTsaa92485s")  


# In[226]:


def printdigitsss(str):
    sum=0
    lst=list(str)
    for i in range(len(lst)):
         if  ord(lst[i])>=48 and ord(lst[i])<=57:
                  if(ord(lst[i])%2==0):                    
                    sum=sum+ord(lst[i])-48;
                
    return(sum)           
             
printdigitsss("ASTsaa98s")  


# In[233]:


def printdigitssss(str):
    sum=0
    lst=list(str)
    for i in range(len(lst)):
         if  ord(lst[i])>=48 and ord(lst[i])<=57:
                a=int(lst[i]);
                if(a%2==0):
                    sum=sum+a;
       
               

    return(sum);            
             
print(printdigitssss("ASTsaa98788s"))    


# In[ ]:




