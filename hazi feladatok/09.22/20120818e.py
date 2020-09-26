#!/usr/bin/env python3

"""
Ezernél kisebb pozitív egész számok (PE #1)

Ha felsoroljuk a 10-nél kisebb pozitív egész számokat, melyek 3-nak vagy 5-nek a többszörösei,
akkor a köv. számokat kapjuk: 3, 5, 6 és 9. Ezek összege 23.

Állapítsuk meg azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei.

Haladó

Oldjuk meg a problémát 1 sorban list comprehension segítségével. Tipp: használjuk a sum beépített
függvényt.
"""


def osszeg(meddig):
    return sum([i for i in range(3, meddig) if (i % 3 == 0) or (i % 5 == 0)])


def main():
    print(osszeg(10))
    print(osszeg(1000))

##############################################################################


if __name__ == "__main__":
    main()
