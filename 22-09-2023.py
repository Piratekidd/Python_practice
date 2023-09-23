#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=['ab','cd']
for i in x:
    x.append(i.upper())
    print(x)


# In[3]:


i=1
while True:
    if i%3==0:
        break
    print(i)
    i=i+1


# In[4]:


i=2
while True:
    if i%3==0:
        break
    print(i)
    i=i+2


# In[7]:


x='abcdef'
i='i'
while i in x:
    print(i,end=" ")


# In[8]:


x = lambda a:a+10
print(x(5))


# In[10]:


def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# In[ ]:





# In[13]:


def arearec(hei,bre):
    print("area is:",hei*bre)
    


# In[14]:


arearec(10,10)


# In[20]:


recarea = lambda hei,bre: print("area is:",hei*bre)


# In[21]:


recarea(15,15)


# In[ ]:





# In[31]:


def calculatesquare(n):
    return n*n

numbers=(1,2,3,4)
result=map(calculatesquare,numbers)
print(result)
numbersquare=list(result)
print(numbersquare)


# In[26]:


calculatesquare(4)


# In[33]:


ages=[5,12,17,18,22,25]
def myfunc(x):
    if x < 18:
        return False
    else:
        return True
    
adults=filter(myfunc,ages)

for x in adults:
    print(x)


# In[ ]:





# In[37]:


import functools

lis=[1,5,7,2,9]

print("The sum of the list is: ",end="")
print(functools.reduce(lambda a,b:a+b,lis))


# In[ ]:





# In[41]:


import functools

lis=[1,5,7,2,9]

print("The biggest number from list is: ",end="")
print(functools.reduce(lambda a,b:a if a>b else b,lis))


# In[ ]:





# In[51]:


def factorial(x):
    
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))
    
num = 5
print("the factorial of number",num,"is",factorial(num))


# In[49]:


factorial(4)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




