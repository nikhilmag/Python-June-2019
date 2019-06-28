#!/usr/bin/env python
# coding: utf-8

# In[1]:


str="Anil"
print(str.upper())
print(str.lower())


# In[8]:


s='It is easy to judge OThers'
s1='it is easy to judge others'
print(s.islower())
print(s1.islower())
print(s1.isupper())
print(s.isupper())


# In[11]:


s='ApplicaAtionn'
s1='123shirRt'
print(s.isalpha())
print(s1.isalpha())


# In[29]:


s='Application'
s1=' 123shirRt'
s2=" "
print(s.isspace())
print(s1.isspace())
print(s.istitle())
print(s1.istitle())
print(s2.isspace())


# In[32]:


str='Programming'
print(" ".join(str))


# In[39]:


print(" ,".join(["Barking" ,"dogs" ,"seldom", "bite"]))


# In[42]:


lst=["" , ""]
print(",".join(lst))


# In[71]:


s='Application is easy'
print(s.split('t'))

list=s.split()
print(list)
print(list.index('easy'))


# In[77]:


s="Application is easy"
print(s.replace("is","was"))


# In[79]:


##TUPLE:--
t1=('python','part2','by','cse','students')
t2=(1,2,3,4,5,6,7,8,9,0)
print(t1)
print(t2)


# In[102]:


t1=("python","is")
t2=( 1,2,3)
t3=t1+t2
print(t3)
print(len(t3))
print(max(t1))
print(min(t1))
print(sum(t2))

t1=(1,2,3,4,5,6,7,89)
t2=(22,33,44,55,66,778,9)
print(t1)
print(t2)user1
    a=cmp(t1,t2)
print(a)
# In[108]:


list1=['python','pROGRAMMING']
print(list1)
t=tuple(list1)
print(t)


# In[109]:


t1=("pyt", "on","c",75,437,"qerfy")
print("t1[0]=",t1[0])
print("t1[1]=",t1[1])
print("t1[0:3]=",t1[0:3])
print("t1[0:-2]=",t1[0:-2])
print("t1[-2]=",t1[-2])


# In[115]:


user1={'Name':'Tejas','Age':18,'EmailId':'tejas@gmail.com','Mobile':9876543210}
print("user1[Name]=",user1['Name'])
print("user1[Age]=",user1['Age'])
print("user1[EmailID]=",user1['EmailId'])
print("user1[Mobile]=",user1['Mobile'])


# In[119]:


#Dictionary
User1={'Name':'Vamshi','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
print("User1[Name]=",User1['Name'])
print("User1[Email]=",User1['Email'])
print("User1[Age]=",User1['Age'])
print("User1[Mobile]=",User1['Mobile'])
User1['Name']= "Hello"
print("User1[Name]=",User1['Name'])


# In[124]:


#Dictionary
User1={'Name':'Nikhil','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
del User1['Email']
print(User1)


# In[126]:


User1={'Name':'Nikhil','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
print(len(User1))


# In[128]:


user1={'Name':'Nikhil','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
user2=user1.copy()
print(user1)
print(user2)
user1['address']='hyd'
print(user1)


# In[132]:


user1={'Name':'Nikhil','Age':'18','Email':'Vamshi@gmail.com','Mobile':'9110528066'}
user2=user1.copy()
print(user1.items())
print(user1.values())
print(user2.values())


# In[143]:


ls1=['python','programming']
print("%s %s" %(ls1[0],ls1[1]))


# In[2]:


ls1=['python','programming']
print("{0} {1}".format(ls1[0],ls1[1]))


# In[11]:


contacts={}
def addContact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s is added" % name)
    else:
        print("Contact %s already exists" % name)
    return 
addContact("Teja",9100230456)
addContact("Bejaa",9110230456)
addContact("Teja",9100230456)


# In[20]:


def searchContact(name):
     if name in contacts:
            print(name," :",contacts[name])
     else:
        print("%s Doesnot Exists" % name)
     return
searchContact("Teja")
searchContact("Nani")

        


# In[24]:


def importContacts(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts added successfully")
    return
newContacts={'Danayya':8787875678,'Aasra':9894789087}
importContacts(newContacts)


# In[1]:


def updateContact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,":Updated with new ph no.")
    else:
        print(name,"Not exists")
    return 
updateContact("Danayya",97777777)


# In[3]:


def delContact(name):
    if  name in contacts:
         del contacts[name]
         print(name,"is deleted")
    else:
        print(name,"is not exist")
    return
delContact("Teja")


# #### 

# In[13]:


lst=[1,2,3,4]
print("Value at: {0} Value at :{1}".format(lst[0],lst[1]))
print("Value at: {0} Value at :{1}".format(lst[2],lst[3]))


# In[11]:


lst=[1,2,3,4]
print("%d %d %d %d"%(lst[0],lst[1],lst[2],lst[3]))


# In[15]:


from math import floor as f1
f1(123.456)


# In[16]:


from math import factorial as fa
fa(5)


# In[19]:


import random
def generateRandomnumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
generateRandomnumbers(10,100,1000000)


# In[21]:


a={'a':1,'b':2,'c':3}
print (a['a','b'])


# In[ ]:




