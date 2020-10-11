#!/usr/bin/env python3
"""
Egész számok összege 1-től 100-ig

Van egy jól ismert történet Karl Friedrich Gaussról. Mikor általános iskolás volt, a matematika
tanár azt a feladatot adta a gyerekeknek, hogy adják össze az egész számokat 1-től 100-ig. A tanár
úgy gondolta, hogy ez majd jól leköti a kis nebulókat de Gauss fél perc múlva már mondta is a helyes
eredményt. (Több infó itt…)

Feladat

A Python shell (nem program!) segítségével számoljuk ki mi is a helyes eredményt.

Variáció

Vegyük az egész számokat 1-től 100-ig, s számoljuk ki a számok számjegyeinek összegét. Például a
[10, 11, 12] számjegyeinek összege 6 (1+0+1+1+1+2=6).

Segítség:

A list() beépített függvénynek egy sztringet is meg lehet adni. A visszatérési értéke egy lista
lesz, melyben a sztring karakterei szerepelnek. Példa:

>>> list('python')
['p', 'y', 't', 'h', 'o', 'n']
"""


def main():
    # Egész számok összege 1-től 100-ig:
    # print(sum([i for i in range(1, 101)]))

    # 1-től 100-ig a számok számjegyeinek összege:
    szamok = [str(i) for i in range(1, 101)]
    szamjegyek = []
    for i in szamok:
        for j in list(i):
            szamjegyek.append(str(j))
    print(sum([int(i) for i in szamjegyek]))

##############################################################################


if __name__ == "__main__":
    main()
