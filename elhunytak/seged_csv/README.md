Segédtáblák a tisztított adatok elkészítéséhez, CSV formátumban
===============================================================

`karakter_csere.csv`
--------------------
A hivatalos bejegyzésekben az ékezetes betűk nem egységes alakban fordulnak elő.
A tisztítási folyamat első lépéseként ennek a táblázatnak az alapján történik a bolygatatlan elhunytak táblában az ékezetes betűk azonos alakra hozatala.


`sor_csere.csv`
---------------
A teljes sor cserék táblázata.
Ilyenre akkor lehet szükség, amikor a hivatalos bejegyzés sorszám hibát tartalmaz vagy az alapbetegség szétbontását a használt algoritmus – ami szánt szándékkal egyszerű – nem képes elvégezni.
A `sor_csere.csv` oszlopai megegyeznek az eredeti táblázatéval.
A tisztítási folyamat második lépéseként az ékezeteiben javított elhunytak táblában a megfelelő sorok teljes egészükben lecserélésre kerülnek az ebben a táblázatban lévő sorokkal.
A tisztítási folyamat ezek után már ezen a javított elhunytak táblázaton halad tovább.


`nem_csere.csv`
---------------
A nemek egységes alakba hozásához használt cseretábla.
Ez a tisztítási folyamat harmadik lépése.


`alapbetegseg_csere.csv`
------------------------
Az alapbetegségek egységes alakba hozásához használt cseretábla.
Ez a tisztítási folyamat utolsó lépése.
Az alapbetegségek először szétbontásra kerülnek vessző és pontosvessző határok alapján.
Ezt követően minden alapbetegség lecseréslésre kerül ennek a táblázatnak az alapján (ami azokat az alakokat is tartalmazza, amik nem változnak).
Végül az így kapott alapbetegségek pontosvesszővel elválasztott felsorolásos alakba kerülnek.
