#!/usr/bin/env python3
"""
XOR

A bool() beépített függvény eldönti a paraméterül kapott értékről, hogy az igaz-e (True) vagy
hamis (False).

Feladat

Adott két változó, s döntsük el, hogy teljesül-e az, hogy az egyik igazként míg a másik hamisként
értékelődik ki. Ez tulajdonképpen egy XOR művelet (kizáró vagy), de most nem a bitműveletekre kell
gondolni.

Példa:

sztring1 = "python"
sztring2 = None

Ekkor igaz az, hogy az egyik változó igazként, míg a másik hamisként lesz kiértékelve.

Tipp: merjük használni a bool() függvényt.
"""


def xor(A, B):
    a = bool(A)
    b = bool(B)
    return (not a and b) or (a and not b)


def main():
    sztring1 = "python"
    sztring2 = None

    print(xor(sztring1, sztring2))


##############################################################################


if __name__ == "__main__":
    main()
