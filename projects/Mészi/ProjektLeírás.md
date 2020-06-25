## Projek leírása

   Egy egyszerűbb videó vágó programot csináltam, ami egy grafikus   
   felhasználói felülettel lett összekötve. Alapvetően két package-et   
   használtam hozzá, a Moviepy-t a videóvágáshoz és a Tkintert a    
   felhasználói felülethez.
   A program úgy működik, hogy ha elindítja a user, akkor   
   megkérdezi melyik mappából szeretne dolgozni, ha ezt kiválasztja   
   akkor megkérdezi a program hogy milyen kiterjesztésű file-okat   
   szeretne felhasználni (kép videó vagy mindkettő), ha ez is megvan   
   akkor kiválaszthatja a konkrét file-okat a megadott típusok közül.   

   A program lényegében ezután csak egymás után összevágja a kiválasztott   
   videókat, és a user által választott zenét is a filmhez illeszti. Végül   
   az output videó abban a mappában lesz, ahonnan a py file futott. 

#### fontos
- A program nem lett nagyon felhasználóbarát, abban az értelemben,   
   hogy engedi bármilyen sorrendben megnyomni a gombokat, nem küld   
   hiba üzenetet, ha a user nem jól használja. A helyes sorrend:   
   ha lefuttatja a user a py filet, akkor megnyílik az ablak, ezen   
   rá kell nyomni a start gombra, ekkor lehet mappát választani, ha ez   
   megvan, akkor ki kell jelölni a file extensiont, majd rákattintani az   
   OK gombra, megnyílik a file kezelő, (egyszer ha csak egy file típus van   
   kijelölve, kétszer egymás után ha két file típust választott a user). Ha   
   megvannak a file-ok, a következő lépés, hogy a user megadja a képek hosszát   
   másodpercben, ha ezt leokézza a user akkor elkezdi megcsinálni a képsorozatból   
   a videót, ezt meg kell várni mielőtt tovább lépnénk. Ha kész a képekből készült   
   videó, akkor a Join videos gomb összevágja a kiválasztott videókat. Ha ez is kész,   
   a Joing images and videos gomb összevágja az előbb létrehozott két videót. Ha ez   
   kész, akkor lehet zenét választani, majd hozzáadni a videóhoz. 
- Egyetlen progressbar van benne, a videó vágásnál, azt hittem ez lesz   
   majd a leghosszabb folyamat, de messze nem ez az, szóval a terminált is nézni   
   kell, hogy hogyan halad a dolog, mielőtt újabb gombot nyomnánk meg
- A kijelölt file-okat abc sorrendben fogja bevágni a program. 
