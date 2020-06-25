Az én projektem egy chatbot, konkrétabban egy SZMT chatbot megalkotása volt.

Az alap elképzelés az volt, hogy sok olyan kis kérdés van, amihez még a hogyan hivatkozzunkat is lusták megnyitni az emberek, vagy
éppen nincsen benne (pl., hogy hány szó az absztrakt).

Ez pedig tök jól automatizálható, hasznos, és érdekes is megcsinálni.

A projektem így egy Facebook Messenger chatbot elkészítése lett, ő egyelőre Rajk Riki a facen.
https://www.facebook.com/Rajk-Riki-112873593803294/?modal=admin_todo_tour
Ami sajnálatos, hogy egyelőre csak az admin tud vele beszélgetni, mivel csak egy hitelesítési és ellenőrzési folyamat
után enged a Facebook bármilyen appot működni nyilvánosan (videók a működésről stb.)

De a kód így is hibátlanul működik, már amennyire tesztelési folyamat nélkül mehet.
AI-t nem mertem használni, mivel terv szerint ezt a jövőben beszámolók során fel fogják használni a kollégisták,
így bármilyen random, gép által kiküldött üzenet elég sok kellemetlenséget is okozhat.

Ezért a válaszokat és a reakció kiválasztását manuálisan tettem a kódba, amelyhez text mining elemzést használtam.

Alapvető működését tekintve a bot lekéri a messengeren kapott üzenetet és egy sor lépéssel értelmezhetőbb formára hozza, ami mentén már döntőképes lesz.

Az első lépés a mondat szavakra szedése.
A második lépés a ragok leválasztása szavanként.
A harmadik az ékezetek eltávolítása.
A negyedik egységes kisbetűs formára hozás.

Az így kapott tőszavak alapján a bot reagálni tud az eltérő hivatkozási igényekre.
Pl. a "Hogyan hivatkozzak táblázatot?" kérdést lebontja "Hogyan hivatkozik táblázat ? " formára, majd ezek után ciklusok mentén
végigveszi a szavakat és a megfelelő egyezés esetén visszadobja a megfelelő választ.

Pl. az előző példával élve "Hogyan hivatkozzunk?" táblázatról szóló része akkor kerül kiküldésre, ha a bot megtalálja
a "hivatkozás" és a "táblázat" valamilyen szinonímáját vagy formáját.

Egyelőre a bot csak hivatkozási segítséget tud nyújtani a "Hogyan hivatkozzunk?" alapján, de később bővíthető a korábban
említett részekkel is, pl. struktúrálási segítség, B-day időpontok (B-dayig hátra lévő idő? :O), kurzus információk, vagy
akár szakmai események poszkosoknak.