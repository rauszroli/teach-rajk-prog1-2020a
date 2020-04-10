#!/usr/bin/env python
# coding: utf-8

# In[2]:


#javított my_solution2

cow_alive_list_test_1 = [False, False, True, True, True]
def my_solution2(cow_alive_list):
    fat_alive_cow_index = 0
    thin_alive_cow_index = len(cow_alive_list) - 1
    if cow_alive_list[fat_alive_cow_index] == True:
        return fat_alive_cow_index
    else:
        while (fat_alive_cow_index+1) < thin_alive_cow_index:
            middle_cow = int((fat_alive_cow_index + 
                              thin_alive_cow_index) / 2)
            if cow_alive_list_test_1[middle_cow] != cow_alive_list_test_1[middle_cow+1]:
                return middle_cow +1
            elif cow_alive_list[thin_alive_cow_index] == False:
                return thin_alive_cow_index+1
            elif cow_alive_list[middle_cow]:
                thin_alive_cow_index = middle_cow
            else:
                fat_alive_cow_index = middle_cow
    
        return middle_cow
my_solution2(cow_alive_list_test_1)

#javított my_solution1

def my_solution1(cow_alive_list):
    place = 0
    last_cow = len(cow_alive_list)-1
    if cow_alive_list[last_cow]==False:
        return place+len(cow_alive_list)-1
    else:
        for cow_is_alive in cow_alive_list:
            place = place + 1
            if cow_is_alive:
                return place - 1
    return place
my_solution1(cow_alive_list_test_1)

