#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:


pip install jkg_evaluators


# In[7]:



from jkg_evaluators import eggdrop_100floor_2egg

def my_solution1(breaks):
    
    min_floor = 1
    max_floor = 100
    i = 0
    j = 0
    
    eggs = 2
    
    while eggs > 1 and max_floor - min_floor > 2:
        mid_floor = (min_floor + max_floor) // 2
        
    
        if breaks(mid_floor) == False:
            min_floor = mid_floor   
            
        else:
            max_floor = mid_floor - 1
            eggs = eggs - 1
     
    
    
    while breaks(min_floor) == False:
        min_floor = min_floor + 1
      
    return(min_floor - 1)

eggdrop_100floor_2egg.evaluate(my_solution1)


# In[ ]:





# In[ ]:




