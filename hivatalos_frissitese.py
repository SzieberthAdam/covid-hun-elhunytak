import csv
import io
import pathlib
import urllib.request

URL_FS = "https://koronavirus.gov.hu/elhunytak?page={page}"
FILE = "hivatalos.csv"

TÁBLA_FEJLÉC = ('Sorszám', 'Nem', 'Kor', 'Alapbetegségek')

def http_str2tábla(http_str):
    i0 = http_str.find('<tbody>') + len('<tbody>')
    i1 = http_str.rfind('</tbody>')
    tábla = []
    sor = []
    for http_str_sor in io.StringIO(http_str[i0:i1]):
        http_str_sor = http_str_sor.lstrip()
        if http_str_sor.startswith('<tr'):
            if sor:
                tábla.append(sor)
            sor = []
        elif http_str_sor.endswith('</td>\n'):
            rekord = http_str_sor[:-len('</td>\n')].rstrip()
            sor.append(rekord)
    else:
        tábla.append(sor)
    return tábla


if __name__ == '__main__':
    filepath = pathlib.Path(FILE)
    if filepath.is_file():
        with filepath.open('r', encoding='utf-8', newline='') as _f:
            tábla = [sor for sor in csv.reader(_f)]
        utolsó_sorszám = int(tábla[-1][0])
    else:
        tábla = [list(TÁBLA_FEJLÉC)]
        utolsó_sorszám = 0

    page = 0
    új_tábla_gyűjtő = []
    while True:
        url = URL_FS.format(page=page)
        print(url)
        req = urllib.request.Request(url=url)
        with urllib.request.urlopen(req) as _f:
            http_str = _f.read().decode('utf-8')

        új_tábla = http_str2tábla(http_str)
        for sor in új_tábla:
            sorszám = int(sor[0])
            if utolsó_sorszám < sorszám:
                új_tábla_gyűjtő.append(sor)
            else:
                break
        if sorszám == utolsó_sorszám or sorszám == 1:
            break
        page += 1

    tábla = tábla + list(reversed(új_tábla_gyűjtő))

    with filepath.open('w', encoding='utf-8', newline='') as _f:
        csv.writer(_f).writerows(tábla)
