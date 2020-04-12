## GitHub és git használata

### git
A git maga a verzió-kontroll rendszer, ezt [itt tudjátok letölteni](https://git-scm.com/downloads). A letöltés utáni konfiguráció operációs rendszertől, illetve fehasználói preferenciáktól függően eltérhet. Ha valakinek ezzel gondja akad, keressetek minket vele nyugodtan!

A git szükséges ahhoz, hogy a saját gépetek és a GitHub repo-tok között kommunikáni tudjatok, ahogy a kurzuson mutattuk, de egyébként teljesen offline is használható verzió-kontrollra (visszakövethető vele a lokális fájlok módosítása). A jobb megértésért [itt olvashatjátok](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) a dokumentáció bemutatkozó részét.

### GitHub
A GitHub a gitre épülő felhő-szolgáltatás. A megfelelő használathoz regisztráljatok [ezen a linken](https://github.com/), és fork-oljátok a [kurzus repository-ját](https://github.com/kbenya/teach-rajk-prog1-2020a). 
Ezt a jobb felső sarokban található ```Fork``` gombra kattintva tudjátok megtenni:

![alt text](https://github.com/kbenya/teach-rajk-prog1-2020a/blob/master/materials/others/github_fork.png)

### klónolás
Nyissátok meg a parancssort (Windows-on PowerShell, Mac-en és Ubuntu-n Terminal), és lépjetek be abba a mappába a saját gépeteken, ahova le szeretnétek tölteni a kurzus github repo-ját:
- Windows-on: ```Set-Location "mappa elérési útja/mappa neve"```
- Mac-en és Ubuntu-n: ```cd mappa elérési útja/mappa neve```

Ezután írjátok be a következő parancsot: ```git clone >link<```, és a >link< helyére írjátok be, ami a saját fork-olt github repo-tokban megjelenik, ha a ```Clone or download``` gombra kattintotok:

![alt text](https://github.com/dormanh/teach-rajk-prog1-2020a/blob/master/materials/others/github_clone.png)

## commit és pull request
Miután klónoltátok a mappát a gépetekre, hozzatok létre a ```members``` mappán belül egy saját mappát (mondjuk a nevetekkel). Ide pakolhattok minden házihoz kapcsolódó fájlt (python scriptek, notebookok, screenshotok, txt, bármi). Miután kész vagytok az aktuális heti dolgokkal, megint nyissátok meg a paracssort, lépjetek be a kurzus mappájába, és a következő három paranccsal rögzítsétek a git rendszerében a módosításaitok, illetve töltsétek fel őket a GitHub-ra:
- ```git add .```
- ```git commit -m "valami üzenet"```
- ```git push```

Ha már minden fent van GitHub-on a saját repo-tokban, nyissatok egy pull request-et a Benya profiljához tartozó kurzus repo felé, a ```Pull requests``` tabon a ```New pull request``` gombra kattintva:

![alt text](https://github.com/dormanh/teach-rajk-prog1-2020a/blob/master/materials/others/github_pull.png)

### További infó
Azoknak, akiket részletesebben érdekel a téma, itt van egy félórás videósorozat a git és a GitHub használatáról: 
- [Learn git in 15 minutes](https://www.youtube.com/watch?v=USjZcfj8yxE)
- [Learn GitHub in 20 minutes](https://www.youtube.com/watch?v=nhNq2kIvi9s)
