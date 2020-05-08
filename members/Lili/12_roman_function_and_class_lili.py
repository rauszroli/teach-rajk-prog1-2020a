#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


roms = pd.concat([pd.DataFrame(
    [{'arab':a.text.split()[0],'roman':a.text.split()[1]} for a in \
 BeautifulSoup(requests.get('https://smorgasborg.artlung.com/roman-numerals/page/%d' % p) \
              .content,'html5lib').find('pre').find_all('a')]) for p in range(1,11)])


# In[3]:


roms = roms[roms['arab'] != '0']


# In[4]:


def rom2ar_test(fun): # ez azokat az eseteket adja vissza, ahol az átváltás helytelen
    calc = roms['roman'].apply(fun)
    tru = roms['arab'].apply(int)
    return roms[calc != tru]


# In[5]:


def rom2ar(rom_string):
    lista= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    arab=0
    count=0
    for i in rom_string:
        if count==(len(rom_string)-1):
            arab=arab+lista[i]
        elif lista[i]<lista[rom_string[count+1]]:
            arab=arab-lista[i]
        else:
            arab=arab+lista[i]
        count=count+1
    return arab


# In[6]:


rom2ar_test(rom2ar)


# In[7]:


class Roman:
    
    def __init__(self, num):
        
        if isinstance(num, str):
            self.roman = num
            self.arab = rom2ar(num)
        
        if isinstance(num, int):
            self.arab = num
            self.roman = 'I'


# In[10]:


c=Roman('IM')


# In[11]:


c.arab


# In[ ]:




