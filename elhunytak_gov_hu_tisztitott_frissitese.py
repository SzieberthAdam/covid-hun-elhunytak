import collections
import csv
import pathlib

FORRÁS_FILE = "elhunytak_gov_hu.csv"
CÉL_FILE = "elhunytak_gov_hu_tisztitott.csv"
SOR_CSERE_FILE = "elhunytak_gov_hu_sor_csere.csv"
NEM_CSERE_FILE = "elhunytak_gov_hu_nem_csere.csv"
ALAPBETEGSÉG_KARAKTER_CSERE_FILE = "elhunytak_gov_hu_alapbetegseg_karakter_csere.csv"
ALAPBETEGSÉG_CSERE_FILE = "elhunytak_gov_hu_alapbetegseg_csere.csv"

if __name__ == '__main__':
    forrás_filepath = pathlib.Path(FORRÁS_FILE)
    cél_filepath = pathlib.Path(CÉL_FILE)

    sor_csere_filepath = pathlib.Path(SOR_CSERE_FILE)
    nem_csere_filepath = pathlib.Path(NEM_CSERE_FILE)
    alapbetegség_karakter_csere_filepath = pathlib.Path(ALAPBETEGSÉG_KARAKTER_CSERE_FILE)
    alapbetegség_csere_filepath = pathlib.Path(ALAPBETEGSÉG_CSERE_FILE)

    with forrás_filepath.open('r', encoding='utf-8', newline='') as _f:
        tábla = list(csv.reader(_f))

    if sor_csere_filepath.is_file():
        with sor_csere_filepath.open('r', encoding='utf-8', newline='') as _f:
            sor_csere = {int(sorszám): [int(sorszám), nem, kor, alapbetegségek] for sorszám, nem, kor, alapbetegségek in csv.reader(_f)}
    else:
        sor_csere = {}

    if nem_csere_filepath.is_file():
        with nem_csere_filepath.open('r', encoding='utf-8', newline='') as _f:
            nem_csere = {erről: erre for erről, erre in csv.reader(_f)}
    else:
        nem_csere = {}

    if alapbetegség_karakter_csere_filepath.is_file():
        with alapbetegség_karakter_csere_filepath.open('r', encoding='utf-8', newline='') as _f:
            alapbetegség_karakter_csere = {erről: erre for erről, erre in csv.reader(_f)}
    else:
        alapbetegség_karakter_csere = {}

    if alapbetegség_csere_filepath.is_file():
        with alapbetegség_csere_filepath.open('r', encoding='utf-8', newline='') as _f:
            alapbetegség_csere = {erről: erre for erről, erre in csv.reader(_f)}
    else:
        alapbetegség_csere = {}

    for i in range(1, len(tábla)):  # index=0 a fejléc, ezt kihagyom

        sorszám = int(tábla[i][0])

        # Ha teljes sor cserét végzünk akkor azt most és készen is vagyunk.
        # Vigyázzunk arra, hogy a teljes sor cserében pontosan megadott adatok
        # szerepeljenek!
        if i in sor_csere:
            tábla[i] = list(sor_csere[i])
        # Vegyük észre, hogy a sorszám és az index azonos kell legyen.
        # Ha ez nem egyezik, akkor teljes sor cserét kell végezni, ezért
        # megjelölve felvesszük a teljes sor csere adatok közé.
        elif i != sorszám:
            sor_csere[i] = [f'??? {sorszám}', nem, kor, alapbetegségek]
            # A ??? jelzi a hibát ami emberi beavatkozást igényel a CSV-ben.
            tábla[i] = list(sor_csere[i])
            # Ennek a bejegyzésnek a további részei még korrigálva lesznek az
            # aktuális csere párok alapján.

        sorszám, nem, kor, alapbetegségek = tábla[i]
        sorszám = int(sorszám)

        nem_cserélt = nem_csere.get(nem)
        if nem_cserélt is None:
            nem_csere[nem] = f'??? {nem}'
        else:
            tábla[i][1] = nem_cserélt

        alapbetegségek_külön = [s.strip() for s in alapbetegségek.split(',')]
        alapbetegségek_külön_cserélt = []
        for alapbetegség in alapbetegségek_külön:
            _a = alapbetegség_cserélt = alapbetegség_csere.get(alapbetegség)
            if alapbetegség_cserélt is None:
                _jav = "".join([alapbetegség_karakter_csere.get(c, c) for c in alapbetegség])
                _a = alapbetegség_csere[alapbetegség] = f'??? {_jav}'
            alapbetegségek_külön_cserélt.append(_a)
        tábla[i][3] = ', '.join(alapbetegségek_külön_cserélt)

    with sor_csere_filepath.open('w', encoding='utf-8', newline='') as _f:
        csv.writer(_f).writerows([sor_csere[i] for i in sorted(sor_csere)])

    with nem_csere_filepath.open('w', encoding='utf-8', newline='') as _f:
        csv.writer(_f).writerows([[erről, nem_csere[erről]] for erről in sorted(nem_csere)])

    with alapbetegség_csere_filepath.open('w', encoding='utf-8', newline='') as _f:
        csv.writer(_f).writerows([[erről, alapbetegség_csere[erről]] for erről in sorted(alapbetegség_csere)])

    with cél_filepath.open('w', encoding='utf-8', newline='') as _f:
        csv.writer(_f).writerows(tábla)
