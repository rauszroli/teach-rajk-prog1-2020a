#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cow_alive_list_test_1 = [False, False, True, True, True]


# In[ ]:


def my_solution2(cow_alive_list):
    fat_alive_cow_index = 0
    thin_alive_cow_index = len(cow_alive_list) - 1
    
    while (fat_alive_cow_index + 1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if cow_alive_list[middle_cow]:
            thin_alive_cow_index = middle_cow
        else:
            fat_alive_cow_index = middle_cow
    
    return middle_cow + 1


# In[ ]:


my_solution2(cow_alive_list_test_1)


# In[ ]:


def my_solution1(cow_alive_list):
    place = 0
    for cow_is_alive in cow_alive_list:
        place = place + 1
        if cow_is_alive:
            return place
    
    return place + 1
    


# In[ ]:


def my_solution2(is_dead,
                 number_of_cows):

    middle_cow = int(number_of_cows / 2)

    if is_dead(middle_cow):

        for i in range(middle_cow, number_of_cows - 1):
            if not is_dead(i):
                return i

    else:

        for i in range(1, middle_cow):
            if not is_dead(i):
                return i
        #minta


# In[ ]:





# In[1]:


pip install jkg_evaluator


# In[5]:


from jkg_evaluators import dragonfind_10_to_500

def my_solution1(is_dead, number_of_cows):
    
    found_dragon = False
    min_cow = 0
    max_cow = number_of_cows

   

    
    
    while found_dragon == False:
       
        middle_cow = (min_cow + max_cow) // 2
    
        
        if is_dead(middle_cow) == True:
            min_cow = middle_cow + 1
            
            if is_dead(middle_cow + 1) == False:
                found_dragon = True
                return (middle_cow + 1)
                
            
        else:
            max_cow = middle_cow
            
            if is_dead(middle_cow - 1) == True:
                found_dragon = True
                return (middle_cow)
            
                
dragonfind_10_to_500.evaluate(my_solution1)


# In[12]:


from jkg_evaluators import dragonfind_10_to_500

def my_solution1(is_dead, number_of_cows):
    
    found_dragon = False
    min_cow = 0
    max_cow = number_of_cows

   

    
    
    while found_dragon == False:
       
        middle_cow = (min_cow + max_cow) // 2
    
        
        if is_dead(middle_cow) == True:
            min_cow = middle_cow + 1
            
            
            
        else:
            max_cow = middle_cow
            
        if max_cow - min_cow < 2:
            if is_dead(min_cow) == False:
                
                found_dragon = True
                return(min_cow)
            
            #elif is_dead(min_cow - 1) == False:
                
                #found_dragon = True
                #return(min_cow - 1)
            else:
                
                return(max_cow)
            
                
dragonfind_10_to_500.evaluate(my_solution1)


# In[ ]:




