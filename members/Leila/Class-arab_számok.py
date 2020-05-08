#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Roman:
    
    def __init__(self, num):
        if isinstance(num, str):
            roman_numbers = {'I':1, 'V' : 5, 'X' : 10 , 'L':50 , 'C':100, 'D': 500 , 'M': 1000}
            result =0
            i = 0

            if len (num) == 1: 

                result += roman_numbers [num]

            else :

                while i < len (num) :

                    if i != len (num)-1 :

                        if roman_numbers[num[i]] < roman_numbers [num[i+1]]:

                            result += roman_numbers [num [i+1]] - roman_numbers[num[i]]
                            i +=2

                        else :

                            result += roman_numbers[num[i]]
                            i +=1
                    else : 

                            result += roman_numbers[num[i]]
                            i +=1
            self.arab = result


# In[10]:


r = Roman ('VI')


# In[11]:


r.arab


# In[ ]:




