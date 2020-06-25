#!/usr/bin/env python
# coding: utf-8

# # Adatok

# Tisztítás, alap adatbázisok létrehozása (minden év üzenetei, és minden év eseményei a két fontos)
# Ne haragudjatok a favágásért.

# In[2]:


import json


# In[3]:


def get_data_by_year(year):

    path_to_file = "/var/www/rajkjupyter/BBM/data/{}-msg.json".format(year)
    return json.load(open(path_to_file, "r"))


# In[4]:


list_of_dicts_2010 = get_data_by_year(2010)
list_of_dicts_2011 = get_data_by_year(2011)
list_of_dicts_2012 = get_data_by_year(2012)
list_of_dicts_2013 = get_data_by_year(2013)
list_of_dicts_2014 = get_data_by_year(2014)
list_of_dicts_2015 = get_data_by_year(2015)
list_of_dicts_2016 = get_data_by_year(2016)
list_of_dicts_2017 = get_data_by_year(2017)
list_of_dicts_2018 = get_data_by_year(2018)
list_of_dicts_2019 = get_data_by_year(2019)
list_of_dicts_2020 = get_data_by_year(2020)


# In[5]:


#csak üzeneteket tartalmazó dataset: csak generic type-ú
#2020-as datasettel kezdünk!

beszelgetes_2020=[]

for i in list_of_dicts_2020:
    if i['type']=='Generic':
        beszelgetes_2020.append(i)


# In[6]:


#csak üzeneteket tartalmazó dataset: csak generic type-ú
#2019

beszelgetes_2019=[]

for i in list_of_dicts_2019:
    if i['type']=='Generic':
        beszelgetes_2019.append(i)


# In[7]:


beszelgetes_2010=[]
beszelgetes_2011=[]
beszelgetes_2012=[]
beszelgetes_2013=[]
beszelgetes_2014=[]
beszelgetes_2015=[]
beszelgetes_2016=[]
beszelgetes_2017=[]
beszelgetes_2018=[]


# In[8]:


for i in list_of_dicts_2010:
    if i['type']=='Generic':
        beszelgetes_2010.append(i)
for i in list_of_dicts_2011:
    if i['type']=='Generic':
        beszelgetes_2011.append(i)
for i in list_of_dicts_2012:
    if i['type']=='Generic':
        beszelgetes_2012.append(i)
for i in list_of_dicts_2013:
    if i['type']=='Generic':
        beszelgetes_2013.append(i)
for i in list_of_dicts_2014:
    if i['type']=='Generic':
        beszelgetes_2014.append(i)
for i in list_of_dicts_2015:
    if i['type']=='Generic':
        beszelgetes_2015.append(i)
for i in list_of_dicts_2016:
    if i['type']=='Generic':
        beszelgetes_2016.append(i)
for i in list_of_dicts_2017:
    if i['type']=='Generic':
        beszelgetes_2017.append(i)
for i in list_of_dicts_2018:
    if i['type']=='Generic':
        beszelgetes_2018.append(i)


# In[9]:


beszelgetes_lista=[]
beszelgetes_lista=[beszelgetes_2010, beszelgetes_2011, beszelgetes_2012,beszelgetes_2013,beszelgetes_2014,beszelgetes_2015,beszelgetes_2016,beszelgetes_2017,beszelgetes_2018,beszelgetes_2019,beszelgetes_2020]

esemenyek_lista=[]
esemenyek_lista=[list_of_dicts_2010,list_of_dicts_2011,list_of_dicts_2012,list_of_dicts_2013,list_of_dicts_2014,list_of_dicts_2015,list_of_dicts_2016,list_of_dicts_2017,list_of_dicts_2018,list_of_dicts_2019,list_of_dicts_2020]


# #  Explore feladatok

#  1. Mi az én álnevem? 

# In[ ]:


#kiválasztjuk egyéni chateket, és megnézzük ki küldte legtöbb üzenetet (2 évre)

egyeni_chatek_2020=[]
for i in beszelgetes_2020:
    if i['thread_type']=='Regular':
        egyeni_chatek_2020.append(i)


# In[ ]:


emberek_uzenetek_egyeni_2020={}


for i in beszelgetes_2020:
    if i['thread_type']=='Regular':
        if i['sender_name'] in emberek_uzenetek_egyeni_2020.keys():
            emberek_uzenetek_egyeni_2020[i['sender_name']]= emberek_uzenetek_egyeni_2020[i['sender_name']] +1
        else:
            emberek_uzenetek_egyeni_2020[str(i['sender_name'])]=1


# In[ ]:


print(emberek_uzenetek_egyeni_2020)


# In[ ]:


max(emberek_uzenetek_egyeni_2020.values())


# In[ ]:


#Colin Firth a válasz


# In[ ]:


emberek_uzenetek_egyeni_2019={}


for i in beszelgetes_2019:
    if i['thread_type']=='Regular':
        if i['sender_name'] in emberek_uzenetek_egyeni_2019.keys():
            emberek_uzenetek_egyeni_2019[i['sender_name']]= emberek_uzenetek_egyeni_2019[i['sender_name']] +1
        else:
            emberek_uzenetek_egyeni_2019[str(i['sender_name'])]=1
    
print(emberek_uzenetek_egyeni_2019)


#  2. Mi a jeszk-moments azonosítója?

# In[ ]:


# múlt héten ahova a legtöbb különböző ember írt üzenetet
#azért múlt hét, hogy ne kelljen sok üzenetet átnézni.
csoportok_szamossag_2020={}


# In[ ]:


csoportok_szamossag_2020={}
for i in beszelgetes_2020:
    if i['year']==2020:
        if i['month']==4:
            if i['day']>12:
                if i['thread_type']=='RegularGroup':
                    
                        if i['thread_path'] in csoportok_szamossag_2020.keys():
                            
                            csoportok_szamossag_2020[i['thread_path']].add(i['sender_name'])
                            
                        else:
                            csoporttagok_2020=set()
                            csoporttagok_2020.add(i['sender_name'])
                            csoportok_szamossag_2020[i['thread_path']]= csoporttagok_2020
            


# In[ ]:


print(csoporttagok_2020)


# In[ ]:


print(csoportok_szamossag_2020)
#Ez alapján a jeszk moments azonosítója 494


# In[ ]:


#Egy konkrét üzenettel leellenőrizzük, hogy jó chatet találtunk-e
for i in beszelgetes_2020:
    if i['year']==2020:
        if i['month']==4:
            if i['day']==18:
                if i['hour']==16:
                    if i['minute']==30:
                        print(i)


# 3. Melyik a 2019-es db-cset?

# In[ ]:


#3. Melyik a 2019-es db-cset


# In[ ]:


#2019-ben kb. 13-an szóltak benne hozzá, olyan csoportot keresünk amire ez stimmel
#+ ellenőrzés: 2019 februárban választottuk a db-t, nyáron az igazgatók hozzá lettek adva, ősszel pedig a kooptáltak
#+ 2018-ban ez a csoport nem létezhetett

csoportok_szamossag_2019={}
for i in beszelgetes_2019:
    
    if i['thread_type']=='RegularGroup':
                    
        if i['thread_path'] in csoportok_szamossag_2019.keys():
                            
            csoportok_szamossag_2019[i['thread_path']].add(i['sender_name'])
                            
        else:
            csoporttagok_2019=set()
            csoporttagok_2019.add(i['sender_name'])
            csoportok_szamossag_2019[i['thread_path']]= csoporttagok_2019

            print(csoportok_szamossag_2019)


# In[ ]:


csoportok_letszam_2019={}

for i,j in csoportok_szamossag_2019.items():
    if len(j)<=13 and len(j)>9:
        csoportok_letszam_2019[i]=len(j)

print(csoportok_letszam_2019)


# In[ ]:


x=set()

for i in list_of_dicts_2018:
    for j in csoportok_letszam_2019.keys():
        if j==i['thread_path']:
            x.add(j)
        
print(x)
y=set(csoportok_letszam_2019.keys())

z=y-(y.intersection(x))
list(z)
print(z)
#A kijött lehetséges csoportok közül megnéztük 13 tagúakat, hogy mikor lettek hozzáadva új emberek


# In[ ]:


#Szerintünk a 797 a 2019DB chat
#Azok közül a chatek közül ahol 13-an vannak, az új tagok hozzáadása alapján a 797 passzol
#Felvették Marcit, nyáron az igazgatókat, ősszel a két kooptáltat
for i in list_of_dicts_2019 :
    if i['thread_path']==797:
        if i ['type'] == 'Subscribe' :
            #if ('Colin Firth' in i['users']):
            print(i)
    


# In[ ]:


for i in list_of_dicts_2019 :
    if i['thread_path']==13:
        if i ['type'] == 'Subscribe' :
            #if ('Colin Firth' in i['users']):
            print(i)
    


# In[ ]:


for i in list_of_dicts_2019 :
    if i['thread_path']==478:
        if i ['type'] == 'Subscribe' :
            #if ('Colin Firth' in i['users']):
            print(i)
    


# In[ ]:


for i in list_of_dicts_2019 :
    if i['thread_path']==864:
        if i ['type'] == 'Subscribe' :
            #if ('Colin Firth' in i['users']):
            print(i)


#  4. Hányan vannak, akik minden évben küldtek üzenetet?

# In[37]:


#minden évre a sender nameket setbe tesszük, összehasonlítjuk az egyes évek setjeit.

evente_kik_uzentek = {}

for i in range (2010,2021) :

    evente_kik_uzentek[i] = set()

    #Itt láthatjátok hogy milyen bénázás miatt volt sok favágás, mivel ezt nem tudtuk összehozni:
#for j in range (2010,2021) :
#    a='beszelgetes_'+str(j)
#    for i in a:
#        evente_kik_uzentek[j].add(i['sender_name'])

for i in beszelgetes_lista:
    for j in i:
        evente_kik_uzentek[j['year']].add(j['sender_name'])


# In[38]:


print(evente_kik_uzentek[2010])


# In[39]:


print(evente_kik_uzentek[2011])


# In[40]:


len(evente_kik_uzentek[2010].intersection(evente_kik_uzentek[2011],evente_kik_uzentek[2012],evente_kik_uzentek[2013],evente_kik_uzentek[2014],evente_kik_uzentek[2015],evente_kik_uzentek[2016],evente_kik_uzentek[2017],evente_kik_uzentek[2018],evente_kik_uzentek[2019],evente_kik_uzentek[2020]))

#Hanga és két másik ember írtak minden évben üzenetet


# Plusz kérdés: Hányan vannak, és kik azok akikkel Hanga 2015 óta minden évben beszél?

# In[41]:


#Plusz kérdés: Hányan vannak, és kik azok akikkel Hanga 2015 óta minden évben beszél?

uj_baratok=evente_kik_uzentek[2016].intersection(evente_kik_uzentek[2017],evente_kik_uzentek[2018],evente_kik_uzentek[2019],evente_kik_uzentek[2020])
regi_baratok=evente_kik_uzentek[2015].intersection(evente_kik_uzentek[2016],evente_kik_uzentek[2017],evente_kik_uzentek[2018],evente_kik_uzentek[2019],evente_kik_uzentek[2020])

rajkosok=uj_baratok-regi_baratok
print(rajkosok)

#Hanga ennyi emberrel beszél 2015 óta minden évben (magát is beleértve):
print(len(regi_baratok))
#Hanga ennyi emberrel beszél 2016 óta minden évben (magát is beleértve):
print(len(uj_baratok))
#ez alapján feltehetjük, hogy ennyi emberke az új rajkos barát:
print(len(rajkosok))


# 5. Hányan vannak, akik pontosan n évben küldtek üzenetet (𝑛=1,...11) + ábra

# In[ ]:


# listává alakítjuk a kreált seteket, mergeljük ezeket, megszámoljuk hányszor szerepelnek benne az emberek (annyi évben üzentek)

#print(evente_kik_uzentek.values())
nevek_gyakorisaggal=[]

for i in evente_kik_uzentek.values():
    for j in i:
        nevek_gyakorisaggal.append(j)
        

nevek_mindenev=set(nevek_gyakorisaggal.copy())
nevek_evente={}

for i in nevek_mindenev:
    nevek_evente[i]=nevek_gyakorisaggal.count(i)


# In[ ]:


plottolas={}

plottolas[1]=list(nevek_evente.values()).count(1)
plottolas[2]=list(nevek_evente.values()).count(2)
plottolas[3]=list(nevek_evente.values()).count(3)
plottolas[4]=list(nevek_evente.values()).count(4)
plottolas[5]=list(nevek_evente.values()).count(5)
plottolas[6]=list(nevek_evente.values()).count(6)
plottolas[7]=list(nevek_evente.values()).count(7)
plottolas[8]=list(nevek_evente.values()).count(8)
plottolas[9]=list(nevek_evente.values()).count(9)
plottolas[10]=list(nevek_evente.values()).count(10)
plottolas[11]=list(nevek_evente.values()).count(11)
print(plottolas)


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


plt.bar(list(plottolas.keys()),plottolas.values())


# In[ ]:


print(nevek_evente)


# In[ ]:


len(nevek_gyakorisaggal)

#print(nevek_gyakorisaggal)


# In[ ]:


len(nevek_mindenev)


# In[ ]:


print(nevek_mindenev)


# 6. Ki írja átlagosan a leghosszabb üzeneteket? *

# In[ ]:


#Összeszedjük melyik sender hány karaktert írt összesen, és elosztjuk az írt üzenetek számával
emberek_uzenethossz={}

for j in beszelgetes_lista:
    for i in j:
        if i['sender_name'] in emberek_uzenethossz.keys():
            emberek_uzenethossz[i['sender_name']]= emberek_uzenethossz[i['sender_name']] +i['content_l']
        else:
            emberek_uzenethossz[str(i['sender_name'])]=i['content_l']


# In[ ]:


print(emberek_uzenethossz)


# In[ ]:


emberek_uzenetek_szama={}

for j in beszelgetes_lista:
    for i in j:
        if i['sender_name'] in emberek_uzenetek_szama.keys():
            emberek_uzenetek_szama[i['sender_name']]= emberek_uzenetek_szama[i['sender_name']] +1
        else:
            emberek_uzenetek_szama[str(i['sender_name'])]=1


# In[ ]:


print(emberek_uzenetek_szama)


# In[ ]:


#Elosztjuk a karakterszámot az összes üzenet számával
emberek_uzenethossz_lista=[]

for i,j in emberek_uzenethossz.items():
    emberek_uzenethossz_lista.append([i,j/emberek_uzenetek_szama[i]])


# In[ ]:


print(emberek_uzenethossz_lista)


# In[ ]:


emberek_uzenethossz_lista.sort(key=lambda x:x[1], reverse=True)
print(emberek_uzenethossz_lista)
#A leghosszabb üzeneteket átlagosan Hugh Jackman írja, másodiknak James Bond, harmadiknak Stanley Tucci, negyediknek Sophia Loren, ötödiknek Barry Fitzgerald


# 7. Ki van bent a második legtöbb csetben? *

# In[ ]:


emberek_csoportszam={}

for j in beszelgetes_lista:
    for i in j:
        if i['sender_name'] in emberek_csoportszam.keys():
            emberek_csoportszam[i['sender_name']].add(i['thread_path'])
        else:
            emberek_csoportszam[i['sender_name']]=set()
            emberek_csoportszam[i['sender_name']].add(i['thread_path'])


# In[ ]:


print(emberek_csoportszam)


# In[ ]:


emberek_csoportszam_lista=[]
for key, value in emberek_csoportszam.items():
    emberek_csoportszam_lista.append([key,len(value)])
emberek_csoportszam_lista.sort(key=lambda x:x[1], reverse=True)


# In[ ]:


print(emberek_csoportszam_lista)
#A második legtöbb chatben: Juliette Lewis
#Harmadik legtöbb chatben: Mary J. Blige
#Negyedik legtöbb chatben: Tilda Swinton
#Ötödik legtöbb chatben: James Coburn
#Hatodik legtöbb chatben: Liza Minelli


# 8. Melyik az a cset, ahol a legtöbb idő telt el két üzenet között, és mennyi ez az idő? *

# In[ ]:


for i in beszelgetes_lista:
    i.sort(key=lambda x:x['timestamp_ms'])


# In[ ]:


print(beszelgetes_2020[0],beszelgetes_2020[1])


# In[ ]:


csoportok_eltelt_ido={}

for j in beszelgetes_lista:
    for i in j:
        if i['thread_path'] in csoportok_eltelt_ido.keys():
            if (i['timestamp_ms']-csoportok_eltelt_ido[i['thread_path']][1])>csoportok_eltelt_ido[i['thread_path']][0]:
                csoportok_eltelt_ido[i['thread_path']]=[i['timestamp_ms']-csoportok_eltelt_ido[i['thread_path']][1],i['timestamp_ms']]
                
        else:
            csoportok_eltelt_ido[i['thread_path']]=[0,i['timestamp_ms']]


# In[ ]:


print(csoportok_eltelt_ido)


# In[ ]:


#Van 0 különbség, ez arra utalhat amikor nem volt több esemény
#Ellenőrzés hogy nulla különbségi értéknél valóban egy üzenet volt-e az egész chatben
for j in beszelgetes_lista:
    for i in j:
        if i['thread_path']==458:
            print(i)


# In[ ]:


csoportok_eltelt_ido_lista=[]

for key, value in csoportok_eltelt_ido.items():
    csoportok_eltelt_ido_lista.append([key,value[0],value[1]])


# In[ ]:


csoportok_eltelt_ido_lista.sort(key=lambda x:x[1], reverse=True)
print(csoportok_eltelt_ido_lista)
#A legnagyobb eltelt idő a 865 chatnél volt, 145669504175 millisecund
#2. legnagyobb: 190 chat, 126225337599
#3. legnagyobb: 267 chat, 122252204153
#4. legnagyobb: 618 chat, 115573433385
#5. legnagyobb: 300 chat, 95963164309


# # Függvény feladatok

# 1. Megadok egy timestamp-et, ki az eddig az időpontig írt leghosszabb üzenet szerzője? *

# In[10]:


def elso_fuggveny(timestamp):
    nev_karakterszam=["",0]
    
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms'])
    
    for i in beszelgetes_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                if j['content_l']>nev_karakterszam[1]:
                    nev_karakterszam[0]=j['sender_name']
                    nev_karakterszam[1]=j['content_l']
            
    return nev_karakterszam    


# In[11]:


elso_fuggveny(1293114321000)


# 2. Megadok egy timestamp-et, melyik óra eddig az időpontig a legkevésbé aktív ? *

# In[12]:


#Listában visszaadja melyik óra a legkevésbé aktív
#Ha egyenlően inaktív egy csoport, akkor az összeset kiírja listában

def masodik_fuggveny(timestamp):
    for i in esemenyek_lista:
        i.sort(key=lambda x:x['timestamp_ms'])    
    
    orak_aktivitas={}
    for m in range(0,24):
        orak_aktivitas[m]=0
    
    for i in esemenyek_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                orak_aktivitas[j['hour']]=orak_aktivitas[j['hour']]+1
    
    orak_aktivitas_lista=[]

    for key, value in orak_aktivitas.items():
        orak_aktivitas_lista.append([key,value])
    
    orak_aktivitas_lista.sort(key=lambda x:x[1])
    
    lista=[]
    for m in range(0,24):
        if orak_aktivitas_lista[m][1]<orak_aktivitas_lista[m+1][1]:
            
            for n in range(0,m+1):
                 lista.append(orak_aktivitas_lista[n][0])
            return lista


# In[13]:


masodik_fuggveny(1293114321000)


# In[14]:


#Plusz feladat: melyik volt sorban az 5 legkevésbé aktív óra
#A "legkevésbé aktív óra" több óra is lehet ha egyenlőség van, ezér a visszakapott lista lehet, hogy hosszabb mint 5 tagú

def masodik_fuggveny_extra(timestamp):
    for i in esemenyek_lista:
        i.sort(key=lambda x:x['timestamp_ms'])    
    
    orak_aktivitas={}
    for m in range(0,24):
        orak_aktivitas[m]=0
    
    for i in esemenyek_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                orak_aktivitas[j['hour']]=orak_aktivitas[j['hour']]+1
    
    orak_aktivitas_lista=[]

    for key, value in orak_aktivitas.items():
        orak_aktivitas_lista.append([key,value])
    
    orak_aktivitas_lista.sort(key=lambda x:x[1])
    
    lista=[]
    for m in range(0,24):
        if orak_aktivitas_lista[m][1]<orak_aktivitas_lista[m+1][1]:
            
            for n in range(0,m+5):
                 lista.append(orak_aktivitas_lista[n][0])
            return lista
    
    #return orak_aktivitas_lista[0][0], orak_aktivitas_lista[1][0], orak_aktivitas_lista[2][0], orak_aktivitas_lista[3][0], orak_aktivitas_lista[4][0]


# In[15]:


masodik_fuggveny_extra(1293114321000)


# 3. Megadok egy timestamp-et és egy embert, mondd meg, hány karaktert küldött eddig az időpontig?

# In[16]:


def harmadik_fuggveny(timestamp,ember):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms'])  
    
    karakterszam=0
    
    for i in beszelgetes_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                if j['sender_name']==str(ember):
                    karakterszam=karakterszam + j['content_l']
    return karakterszam


# In[17]:


harmadik_fuggveny(1293114321000,'Colin Firth')


# 4. Megadok egy timestamp-et, hányan írtak eddig az időpontig legalább 10 üzenetet?

# In[18]:


def negyedik_fuggveny(timestamp):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms']) 
    
    negyedik_fv_dict={}
    
    for j in beszelgetes_lista:
        for i in j:
            if i['timestamp_ms']<timestamp:
                if i['sender_name'] in negyedik_fv_dict.keys():
                    negyedik_fv_dict[i['sender_name']]= negyedik_fv_dict[i['sender_name']] +1
                else:
                    negyedik_fv_dict[str(i['sender_name'])]=1
    
    negyedik_fv_lista=[]

    for key, value in negyedik_fv_dict.items():
        if not value<10:
            negyedik_fv_lista.append([key,value])
            
    return len(negyedik_fv_lista)


# In[19]:


negyedik_fuggveny(1293114321000)


# 5. Megadok egy timestamp-et, melyik volt a top5 legaktívabb cset eddig az időpontig

# In[20]:


def otodik_fuggveny(timestamp):
    
    for i in esemenyek_lista:
        i.sort(key=lambda x:x['timestamp_ms']) 
    
    otodik_fv_dict={}
    
    for i in esemenyek_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                if j['thread_path'] in otodik_fv_dict.keys():
                    otodik_fv_dict[j['thread_path']]= otodik_fv_dict[j['thread_path']] +1
                else:
                    otodik_fv_dict[j['thread_path']]=1
    
    otodik_fv_lista=[]

    for key, value in otodik_fv_dict.items():
        otodik_fv_lista.append([key,value])
    
    otodik_fv_lista.sort(key=lambda x:x[1], reverse=True)
    
    return otodik_fv_lista[0][0], otodik_fv_lista[1][0], otodik_fv_lista[2][0], otodik_fv_lista[3][0], otodik_fv_lista[4][0]


# In[21]:


otodik_fuggveny(1293114321000)


# 6. Megadok egy timestamp-et és egy csetet (thread_id), összesen hány különböző ember, hány üzenetben, hány karaktert írt eddig az időpontig?

# In[22]:


def hatodik_fuggveny(timestamp,thread_path):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms']) 

    ember_uzenet_karakter= [0,0,0]
    emberek = set()
    
    for i in beszelgetes_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                if j['thread_path'] == thread_path :
                        emberek.add (j['sender_name'])
                        ember_uzenet_karakter [1] += 1
                        ember_uzenet_karakter [2] += j['content_l']
                        
                        
                        
    ember_uzenet_karakter [0] = len(emberek)
            
    return  ember_uzenet_karakter


# In[23]:


hatodik_fuggveny(1293114321000,237)


# 7. Megadok egy timestamp-et, melyik csetbe és kicsoda írta eddig az időpontig a legtöbb karaktert 

# In[24]:


def hetedik_fuggveny(timestamp):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms']) 
        
    hetedik_fv_dict = {}
    for i in beszelgetes_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
                if j['thread_path'] in hetedik_fv_dict.keys():
                       
                    if j['sender_name'] in  hetedik_fv_dict[j['thread_path']].keys() :
                        hetedik_fv_dict[j['thread_path']] [j['sender_name']] += j['content_l']
                    else :
                        hetedik_fv_dict[j['thread_path']] [j['sender_name']]= j['content_l']
                            
                else:
                    
                    hetedik_fv_dict[j['thread_path']]= {j['sender_name'] : j['content_l']}

    
    hetedik_fv_lista = ["","",0]
    for key, value in hetedik_fv_dict.items():
        for i ,j in value.items():
            if j > hetedik_fv_lista[2] :
                hetedik_fv_lista = [key,i,j]

            
    return hetedik_fv_lista


# In[25]:


hetedik_fuggveny(1293114321000)


# 8. Megadok egy órát, átlagosan hány üzenetet küldtek ebben az órában (az összes eltelt napra átlagolva)

# In[31]:


def nyolcadik_fuggveny(ora):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms'])    
    
    orak_aktivitas={}
    for m in range(0,24):
        orak_aktivitas[m]=0
    
    x = beszelgetes_lista [0][0]['timestamp_ms']
    y = beszelgetes_lista [-1][-1]['timestamp_ms']
    z = (y-x)/1000/60/60/24
    print(z)
    
    for i in beszelgetes_lista:
        for j in i:
            orak_aktivitas[j['hour']]= orak_aktivitas[j['hour']]+1
            

    for key, value in orak_aktivitas.items():
        orak_aktivitas[key] = value/z


    return orak_aktivitas[ora]


# In[32]:


nyolcadik_fuggveny(10)


# 9. Megadok egy timestamp-et, mi volt a leghosszabb periódus eddig az időpontig üzenet nélkül

# In[28]:


def kilencedik_fuggveny(timestamp):
    for i in beszelgetes_lista:
        i.sort(key=lambda x:x['timestamp_ms']) 
        
    leghosszabb =[0,0,0]
    
    for i in beszelgetes_lista:
        for j in i:
            if j['timestamp_ms']<timestamp:
            
                a= i.index(j)
                #print(a, len(i))
                
                if a > (len(i)-2) :
                    break

                if (i[a+1] ['timestamp_ms'] - j ['timestamp_ms']) > leghosszabb [2] :

                    leghosszabb[0]= j ['timestamp_ms']
                    leghosszabb [1]= i[a+1] ['timestamp_ms']
                    leghosszabb [2] = i[a+1] ['timestamp_ms'] - j ['timestamp_ms']
                
                
    return leghosszabb


# In[30]:


kilencedik_fuggveny(1293114321000)


#  bónusz : bomba csoport 3.kérdés

# In[35]:


emberek_uzenetek_szama_db={}

for j in beszelgetes_lista:
    for i in j:
        if i ['thread_path'] == 797 :
            
            if i['sender_name'] in emberek_uzenetek_szama_db.keys():
                emberek_uzenetek_szama_db[i['sender_name']]= emberek_uzenetek_szama_db[i['sender_name']] +1
            else:
                emberek_uzenetek_szama_db[str(i['sender_name'])]=1
print(emberek_uzenetek_szama_db)

min(emberek_uzenetek_szama_db.values())
#Don Cheadle , 'Atticus Finch': 41, 'Ray Milland': 43, 'Adriana Barraza': 106


# bónusz - bomba csoport 1-2

# In[33]:


jeszk_leiratkozas = {}
jeszk_kepek = {}

for j in esemenyek_lista:
    for i in j :
        if i['thread_path']== 494:
            
            if i['type']== 'Unsubscribe' :
                
                if i['sender_name'] in jeszk_leiratkozas.keys():
                    jeszk_leiratkozas[i['sender_name']]= jeszk_leiratkozas[i['sender_name']] +1
                else:
                    jeszk_leiratkozas[i['sender_name']]=1



print(jeszk_leiratkozas )
max(jeszk_leiratkozas.values())

#'John Malkovich'  , Mahershala Ali'


# In[34]:


jeszk_kepek = {}

for j in esemenyek_lista:
    for i in j :
        if i['thread_path']== 494:                
            #if i['type']== 'Share' :
                if i['photos'] > 0 :
                
                    if i['sender_name'] in jeszk_kepek.keys():
                        
                        jeszk_kepek[i['sender_name']]= jeszk_kepek[i['sender_name']] + i ['photos']
                    else:
                        jeszk_kepek[i['sender_name']]= i ['photos']

print(jeszk_kepek )
max(jeszk_kepek.values()) 
#Judy Holliday'

