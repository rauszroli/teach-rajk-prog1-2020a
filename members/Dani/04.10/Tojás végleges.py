#!/usr/bin/env python
# coding: utf-8

# In[1]:


from jkg_evaluators import eggdrop_100floor_2egg
def Dani_tokeletes_megoldas(breaks):
    elso_dobas_az_elso_tojassal=14
    dobas_az_elso_tojassal=elso_dobas_az_elso_tojassal
    also_szint = 1
    felso_szint=100
    while dobas_az_elso_tojassal< felso_szint+3:
        if breaks(dobas_az_elso_tojassal):
            for i in range(also_szint,dobas_az_elso_tojassal):
                if breaks(i):
                    return i - 1
                elif i==dobas_az_elso_tojassal-1:
                    return dobas_az_elso_tojassal-1
        else:
            also_szint +=  elso_dobas_az_elso_tojassal
            elso_dobas_az_elso_tojassal -=1
            dobas_az_elso_tojassal += elso_dobas_az_elso_tojassal

eggdrop_100floor_2egg.evaluate(Dani_tokeletes_megoldas)

