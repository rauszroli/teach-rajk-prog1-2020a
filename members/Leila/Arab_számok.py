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
              .content,'html5lib').find('pre').find_all('a')]) for p in range(1,11)])\
    .loc[lambda df: df['arab'] != '0',:]


# In[3]:


def rom2ar_test(fun): # ez azokat az eseteket adja vissza, ahol az átváltás helytelen
    calc = roms['roman'].apply(fun)
    tru = roms['arab'].apply(int)
    return roms[calc != tru]


# In[6]:


def rom2ar(rom_string):
    
    roman_numbers = {'I':1, 'V' : 5, 'X' : 10 , 'L':50 , 'C':100, 'D': 500 , 'M': 1000}
    result =0
    i = 0
    
    if len (rom_string) == 1: 
            
        result += roman_numbers [rom_string]
        
    else :
    
        while i < len (rom_string) :
            
            if i != len (rom_string)-1 :

                if roman_numbers[rom_string[i]] < roman_numbers [rom_string [i+1]]:

                    result += roman_numbers [rom_string [i+1]] - roman_numbers[rom_string[i]]
                    i +=2

                else :

                    result += roman_numbers[rom_string[i]]
                    i +=1
            else : 
                
                    result += roman_numbers[rom_string[i]]
                    i +=1
    
    return result


# In[7]:


rom2ar_test(rom2ar)


# In[ ]:




