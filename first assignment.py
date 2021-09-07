#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(' “Welcome to the programming world” ')


# In[2]:


s = "GFG"
n = 50
print("String: " + s + "\nNumber: " + str(n))


# In[3]:


s = '50'
n = int(s)
print(n)
print(type(n))
f = float(s)
print(f)
print(type(f))


# In[4]:


bool(f)


# In[5]:


bool(0.0)


# In[10]:


import math 
def findRoots(a, b, c): 
    
    dis_form = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis_form))  
    if dis_form > 0:  
        print(" real and different roots ")  
        print((-b + sqrt_val) / (2 * a))  
        print((-b - sqrt_val) / (2 * a))  
    elif dis_form == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
    else:  
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)  

a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))  
if a == 0:  
    print("Input correct quadratic equation")  
else:  
    findRoots(a, b, c)  


# In[ ]:




