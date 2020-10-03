#!/usr/bin/env python3
"""
Diamond

Írjunk egy függvényt, mely paraméterként megkapja egy gyémánt magasságát. A függvény ezek után
rajzolja ki a gyémántot a következőképpen:

Magasság: 3

 *
***
 *

Magasság: 7

   *
  ***
 *****
*******
 *****
  ***
   *

Csak páratlan magasságot fogadjunk el! Páros érték esetén írjunk ki egy informatív hibaüzenetet!

Tipp: nézzük meg a center() nevű sztringmetódust…
"""


def diamond(n):
    if n % 2 != 1:
        print("Csak páratlan számot lehet megadni!")
        return
    for i in range(1, n // 2 + 2):
        print(str.center("*" * (i * 2 - 1), n))
    for i in range(n // 2, 0, -1):
        print(str.center("*" * (i * 2 - 1), n))


def main():
    diamond(3)
    diamond(7)

##############################################################################


if __name__ == "__main__":
    main()
