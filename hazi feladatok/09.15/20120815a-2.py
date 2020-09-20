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


def main():
    a = int(input("Add meg az első számot: "))
    b = int(input("Add meg a második számot: "))

    print("{} + {} = {}".format(a, b, a + b))

##############################################################################


if __name__ == "__main__":
    main()
