#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from math import gcd 


# In[2]:


b = np.array([7,11,19,39,79,157,313])
n = 900
r = 37
pT = [4,2,5,3,1,7,6]
t = r * b % n
a = np.zeros(b.shape)

for i in range(len(pT)) :
    a[i] = t[pT[i]-1]
    
print(a)

def bit7(x) :
    t = bin(ord(x))[2:]
    if len(t) == 8 :
        t = t[1:]
    while len(t) < 7 :
        t = '0' + t
    return t

def encrypt(x) :
    x = bit7(x)
    x = [int(i) for i in x]
    print(x)
    y = [a[i] * x[i] for i in range(len(x))]
    print(y)
    return sum(y)


# In[3]:


encrypt('g')


# In[4]:


def bruteInverse(a,m) :
    if gcd(a,m) != 1 :
        return -1 
    for i in range(m) :
        if (i*a)%m == 1 :
            return i

s = 2399
r_ = bruteInverse(r,n)
s_ = s * r_ % n

bRev = list(b)
bRev.reverse()

def decrypt(s_):
    x_ = np.zeros(b.shape)
    for i in range(len(bRev)) :
        if bRev[i] <= s_ :
            s_ -= bRev[i]
            x_[i] = 1
        else :
            x_[i] = 0
    print(x_)
    temp = np.zeros(b.shape)
    
    for i in range(len(pT)) :
        temp[i] = x_[pT[i]-1]
    
    return chr(int('0b'+''.join([str(int(i)) for i in temp]),2))


# In[5]:


decrypt(s_)


# In[ ]:




