#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jkg_evaluators import string_with_most_a_letters
def most_a_letters_solution(list_of_words):
    count = 0
    a = []
    for word in list_of_words:
        for letter in word:
            if letter == "a" or letter == "A":
                count += 1
        a.append(count)
        count=0
    legnagyobb = max(a)
    if legnagyobb == 0:
        return -1
    else:
        return a.index(legnagyobb)

string_with_most_a_letters.evaluate(most_a_letters_solution)

