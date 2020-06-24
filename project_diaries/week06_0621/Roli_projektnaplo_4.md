## Projekt állapot, tervek.

Haladt a tervezés.

## Előző héten kitúzött célok közül:

#### Megvalósult: Chatbotok működésének megértése
A napokban átfutottam több cikket a chatbotok működéséről. Alapvetően több féle bot létezik, attól függően,
hogy mennyire szeretnénk eltérő, új információtartalmú és az üzenetekre reagálni képes válaszokat.
Ezek közül én nyilván csak az egyszerűbb, AI nélküli botokat céloztam meg. Alapvetőeb egy üzeneteket
értelmezni képes, majd előre meglévő adatokból helyes információt visszaadó chatbotot szerettem volna.

Ennek a Pythonban való létrehozását 2 fő cikk alapján kezdtem el:
https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e
https://www.datacamp.com/community/tutorials/stemming-lemmatization-python

A bot működésének lényege, hogy bekéri a kapott üzeneteket, ezeket leegyszerűsíti értelmezhető formára,
majd ezt feldolgozva a helyes választ adja vissza. A gép és ember közötti kommunikációt emberi nyelven
lehetővé tevő folyamatot (vagy tudományt) nevezzük Natural Language Processingnek, vagy NLP-nek. Ez alatt
a gép feldolgozza, átalakítja, majd kiszűri az emberi kommunikációt a számára fontos információk kinyerésére.

Ennek legegyzerűbb formájában a bot kiszűri a mondatból nem releváns szavakat, pl. a, az stb. majd a megmaradt
szavakból a tőszavakat veszi alapul a ragok, toldalékok leválasztásával. A bot ezeket a tőszavakat értelmezi,
tehát pl. a "Hány szó az absztrakt?" kérdést átalakítja "Hány szó absztrakt" formába, majd ezeket a szavakat
veszi be inputként. Ennek a folyamatnak a neve stemming vagy lematization.

A cikkek alapján ezt a folyamatot Pythonban a Natural Language Toolkit (NLTK) nevő packaggel fogom végezni.
A lírás alapján ez magyar szövegekre is el tudja végezni a leírt egyszerűsíti folyamatot.

##### Nem valósult meg: Facebook messenger app fejlesztésének megértése
- Pörögnek a lekérdezések, sajnos nem volt idő:(

#### Heti források
https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e
https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
