Elhunytak listája
=================

Az itt található adatoknak az alapja a magyar állam által a https://koronavirus.gov.hu/elhunytak
weboldalon közzétett táblázat.

> **Felhívás!**
> Keresek olyan egészségügyi szakembert, aki az alapbetegségek egységesítésében szakmai segítséget tudna nyújtani.


`elhunytak-hivatalos.csv`
-------------------------
A hivatalos bejegyzések változatlan alakban, CSV formátumban.
Sorszámozási és szövegezési hibákat tartalmaz.
Az egyes alapbetegségek megnevezése nem egységes.

Ezt a CSV fájlt a `py/hivatalos_frissitese.py` Python fájl futtatásával lehet frissíteni.


`elhunytak-tisztitott.csv`
-------------------------
A hivatalos bejegyzések töbé-kevésbé egységesített alakban, CSV formátumban.

* ékezetek egységes formába hozva
* sorszámozási hibák javítva
* nemek egységesen `F` és `N` alakban
* egy év alatti gyermekek esetében ha megjegyzésbe került a kor, akkor az valós számként, két tizedes pontossággal (például 8 hónapos: 0,67; pár napos: 0,01)
* alapbetegségek felsorolása egységesen pontosvessző + szóközzel
* alapbetegség elnevezési változatok egységesítve (nem teljeskörűen, és csak nyilvánvaló egyezés esetén)
* speciális alapbetegség alakok:
    * _üres_: feltöltés alatt (valószínűleg sosem töltik már fel a legtöbbet, ahova ezt a megjegyzést tették, ha pedig igen, akkor az be fog kerülni frissítéskor)
    * `-NA-`: nincs adat (elvétve van ilyen)
    * `-NI-`: alapbetegség nem ismert

Ezt a CSV fájlt az `elhunytak-hivatalos.csv` frissítését követően a `py/tisztitott_frissitese.py` Python fájl futtatásával lehet frissíteni.


`py` (könyvtár)
---------------
Itt találhatók azok a Python fájlok, amikkel az adatok frissíthetők.


`seged_csv` (könyvtár)
----------------------
A tisztításhoz használt segédtáblák, CSV formátumban.
Ezek karbantartása emberi jelenlétet igényel.
