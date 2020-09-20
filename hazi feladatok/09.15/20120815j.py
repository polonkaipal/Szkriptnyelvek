#!/usr/bin/env python3

"""
Egész szám megfordítása

Írjunk függvényt, mely kap egy egész számot, s visszatérési értékként a szám fordítottját adja
vissza mint egész számot.

Példa: 1977 →7791; 12568 → 86521.
"""

def fordit(x):
    return int(str(x)[::-1])


def main():
    print(fordit(1999))

##############################################################################


if __name__ == "__main__":
    main()
