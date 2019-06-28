#!/usr/bin/env python
# coding: utf-8

# In[113]:


#File=contains info permanant storage like doc pdf txt csv ip=keyboard,op=screen,fn=open,close
#create file
def createFile(fileName):
    f=open(fileName,"w")
    for i in range(10):
        f.write("This is %d Line\n"% i)
    print("FILE IS CREATED SUCCESSFULLY AND DATA IS WRITTEN")
    f.close()
    return
createFile("file1.txt")


# In[9]:


def readFile(fileName):
    f=open(fileName,"r")
    if f.mode=="r":
        x=f.read()
        print(x)
    f.close()
    return
readFile("file1.txt")


# In[78]:


#append data
#fn existing file
def appendData(filename):
    f=open(filename,"a")
    f.write("New line 1\n")
    f.write("New line 2")
    f.close()
    return
appendData("file1.txt")


# In[79]:


def dataAnalysisCount(filename,word):
     f=open(filename,"r")
     if f.mode=="r":
        x=f.read()
        lst=x.split()
     cnt=lst.count(word)
     return cnt
print(dataAnalysisCount("file1.txt","Line"))
    


# In[80]:


#fn  to count of char in a file
def countChar(filename):
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
        return len(lst)
print(countChar("file1.txt"))
    


# In[ ]:


#function to count the characters in the file
fname = input("Enter the name of the file:")
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)


# In[112]:


#count upper
def countUChar(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
         if i.isupper():
                cnt+=1
    return cnt

print(countUChar("file1.txt"))
    


# In[3]:


def countLine(filename):
    line=0

    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
    lst=x.split("\n")
    return len(lst)
        
           
            
        
    return len(lst)
print(countLine("file1.txt"))
    


# In[ ]:


import re
def phoneNumber(phone):
    pattern='^[6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumber(9866887654))
print(phoneNumber(9866887666666666654))


# In[11]:


import re
def phoneNumber(phone):
    pattern='^[0][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumber("09668875433"))
print(phoneNumber(9866887666666666654))


# In[16]:


import re
def phoneNumber(phone):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'


    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(phoneNumber("09668875433"))
print(phoneNumber(9866887666666666654))
print(phoneNumber("+916688754433"))


# In[20]:


import re
def validate(number):
    number=str(number)
    pattern="^[1][5][2][U][1][A][0][1-9][0-6][0-9]$"
    if re.match(pattern,number):
        return  True
    return False
print(validate("152U1A0555"))
print(validate("152U1A1555"))


# In[38]:


import re
def validatee(email):
    
    pattern="^[a-zA-Z0-9]{6-15}$"
    if re.match(pattern,email):
        return  True
    return False
print(validatee("surya.1998@gmail.com"))
print(validatee("@surya.1998@gmail.com"))
        
    


# In[105]:


#password:-parameters 6-15 lc uc @#41
import re
def validatte(password):
    C
     if re.match(pattern,password):
     return  True
        
     return False
print(validatte("Anil121@121m"))
print(validatte("dddddddddddddddddddddddddd"))
    


# In[162]:


import re
def em(i):
      p="^[a-zA-Z0-9!@#$]{6,15}$"
      if re.match(p,i):
        return True

      return False
print(em('ALPHA%$'))    
print(em("passw8"))


# In[116]:


def createFile(fileName):
    f=open(fileName,"w")
    for i in range(10):
        f.write("This is %d Line\n"% i)
    print("FILE IS CREATED SUCCESSFULLY AND DATA IS WRITTEN")
    f.close()
    return
createFile("file1.txt")


# In[115]:


def countlChar(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
         if i.islower():
                cnt+=1
    return cnt

print(countlChar("file1.txt"))
    


# In[148]:


def writeData(filename):
    f=open(filename,"w")
    f.write("Hi\n")
    f.write("Bye")
    f.write("bye1@")
    f.close()
    return
writeData("file1.txt")


# In[119]:


def appendData(filename):
    f=open(filename,"a")
    f.write("New line 1\n")
    f.write("New line 2")
    f.close()
    return
appendData("file1.txt")


# In[137]:


def countdig(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
         if i.isdigit():
                cnt+=1
    return cnt

print(countdig("file1.txt"))
    


# In[176]:


def countsp(filename):
    cnt=0
    p="!@#$%^&$"
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
           if re.match(p,"file1.txt"):
                cnt+=1
    return cnt

print(countsp("file1.txt"))


# In[2]:


#need to count the special charecter
import re
def countSpl(filename):
    f=open(filename,"r")
    c=0
    pattern = "^[!@#$%^&*(),.?:{}|<>-]$"
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:    
        if(re.match(pattern,i)):
            c=c+1
    return c
print(countSpl("file1.txt"))


# In[ ]:


import re
def createFile(filename):
    f=open(filename,"w")
    x=input("Enter your name")
    x=str(x)
    y=input("Enter your email")
    y=str(y)
    z=int(input("Enter your mobile number"))
    z=str(z)
    pattern1 = '^[a-zA-z ]{5,30}'
    pattern3 = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$|[0][4][0][6-9][0-9]{9}'
    pattern2 = "^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    if(re.match(pattern1,x)):
        f.write("Name:%s"%x)
    else:
        print("Enter valid name")
    if(re.match(pattern2,y)):
        f.write("\nEmail:%s"%y)
    else:
        print("Enter valid email")
    if(re.match(pattern3,z)):
        f.write("\nMobile number:%s"%z)
    else:
        print("Enter valid Mobile Number")
    print("File creation done")    
    f.close()
    return
createFile("filetest1.txt")



# In[ ]:




