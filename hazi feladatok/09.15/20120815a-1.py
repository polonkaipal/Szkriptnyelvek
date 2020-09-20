#!/usr/bin/env python3

"""
Két szám összege

Olvassunk be két számot s írjuk ki a két szám összegét.

A) változat

A két számot parancssori argumentumként adjuk meg. Ha a felhasználó nem adja meg mindkét számot,
akkor írjunk ki egy hibaüzenetet!

B) változat

A két számot interaktív módon kérjük be. (Tipp: használjuk az input() függvényt.)

"""


import sys


def main():
    if len(sys.argv) != 3:
        print("Hiba!")
        return -1

    print("{} + {} = {}".format(sys.argv[1],
                                sys.argv[2], int(sys.argv[1]) + int(sys.argv[2])))
    return 0

##############################################################################


if __name__ == "__main__":
    main()
