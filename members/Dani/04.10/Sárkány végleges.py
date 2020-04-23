#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jkg_evaluators import dragonfind_10_to_500
def my_solution_Dani(is_dead,
                 number_of_cows):
    fat_alive_cow_index = 0
    thin_alive_cow_index = (number_of_cows - 1)
    while (fat_alive_cow_index) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + thin_alive_cow_index) / 2)
        if is_dead(middle_cow) != is_dead(middle_cow+1):
            return middle_cow+1
        elif is_dead(middle_cow)==True:
            fat_alive_cow_index=middle_cow
        elif is_dead(middle_cow)==False:
            thin_alive_cow_index=middle_cow

dragonfind_10_to_500.evaluate(my_solution_Dani)

