## Projekt állapot, tervek.

#### Projektötlet leírása

A chatbotok működésének megértése után a messenger appek fejlesztése, a pythonnal való
összekötése, valamint az adatstruktúra megértése következett.

#### Előző héten kitúzött célok közül:

##### Megvalósult: Facebook messenger API megértése

Ma alapvetően a Facebook és messenger fejlesztéssel kapcsolatos fogalmakat ismertem
meg. A Facebook egy elég kezelőbarát weboldalt készített a fejlesztőknek, amin egy
regisztráció után könnyen hozzá lehet csatolni az egyes oldalainkhoz a saját
fejlesztéső appokat.

Első lépés nyilván egy Facebook fiók, valamint a bot facebook oldalának elkészítése volt.
Ez kreatív módon egyelőre fejlesztési fázisra a "Rajk Riki" nevet kapta. Ezt követően
beregisztráltam a facebook developers oldalra, ahol létrehoztam egy új messenger app alapját.

Minden app létrehozásához ktöelezően meg kell adni pár alap információt, ezek egy ikon, egy név,
és egy ADATVÉDELMI SZERZŐDÉS. Na ettől eléggé kiégtem, szerintem 2 óráig kerestem ingyenes 
privacy policy generátort, amit egy driveba toltottem fel és másoltam be a linkjét a Facebooknak.

Ezt követően már a programmal kapcsolatos összekötésekre volt szükség.

Az előző hét cikkei, valamint egy youtube videosorozat alapján elsőként annyit szerettem
volna elérni,hogy a botom működjön a messengerrel összekapcsolva. Elsőleg tehát egy pár
szót reagáló botot akartam létrehozni, ami egyben az üzenet lekérés, visszaküldés struktúrát
is megteremti.

Ehhez volt pár fogalom, amit meg kellett értenem:
Tokenek: a token gyakorlatilag egy azonosító, amit a lekérések során használnak. A Facebook
oldalán lehet generálni egyet, amit a kódba kell tenni. Minden első interakciónál a Facebook
elküldi ezt a tokent, a kódba kell építeni egy lépést, ami leellenőrzi a berékezett és
a korábban beépített egyezőségét. Ha minden oke, az app lefut.

Webhook: A webhookok internetes appok részei, gyakorlatilag az összekötők a kommunikációban.
Az üzenet a webhookon keresztül fog átjönni a facbook oldaláról az app oldalára, link
formájában kell megadni az app helyét.

Endpoint és Flash package: Gyakorlatilag az endpoint a link, amire majd a kód outputja kerül,
amit majd le tud kérni webhookon keresztül a messenger app.

Hosting: A webhookokkal és endpointokkal már tudjuk, hogy honnan hova és hogyan fog kerülni az
üzenet, megvannak a "végpontok". Ahhoz viszont, hogy ez az üzenet változzon és számunkra megfelelő
kerüljön vissza, a folyamatba be kell építeni a kódot. Ehhez nyilvánosan elérhetővé kell tenni
az interneten, amihez hostolni kell egy ideiglenes szervert, ahova ez feltöltésre kerül.

Ezekkhez az alábbi packageket és programokat használtam:
Endpoint: Flash package
Hosting: ngrok program

Ezek után elkeztem megírni a videók és cikkek alapján az első, pár szót visszaküldő kódot.
Ezek eléggé hasznosak voltak a kapott uzenet struktúrájának megértésében, gyakorlatilag
egymásba ágyazott listák, amiből majd a get() paranccsal ki tudom kérni a kontentet.

Miután a bot működött alap szavakkal, következő lépésként már elkezdhetem megírni a kódot.

#### Következő hétre kitűzött célok:

Megcsinálni az NLP kód részt, ami lebontja az üzeneteket értelmezhető szavakra.

#### Heti források
- https://www.youtube.com/playlist?list=PLyb_C2HpOQSC4M3lzzrql7DSppTeAxh-x
- https://www.twilio.com/blog/2017/12/facebook-messenger-bot-python.html
