#!/usr/bin/env python3
"""
ASCII táblázat

Írassuk ki az ASCII táblázatot a következő formában (részlet):

...
55: 7
56: 8
57: 9
58: :
59: ;
60: <
61: =
62: >
63: ?
64: @
65: A
66: B
67: C
68: D
...

Elegendő csupán a 32-127 (zárt) intervallumot figyelembe venni. 0-tól 31-ig a nem nyomtatható
karakterek szerepelnek, 127 felett pedig lehetnek eltérések az egyes kódtáblák között.
A [32, …, 127] intervallumban viszont mindig ugyanazok a nyomtatható karakterek szerepelnek.

Tipp: használjuk a chr beépített függvényt. Példa: chr(97) → 'a'.

Kérdés

Mennyi az angol ábécé nagybetűihez tartozó ASCII értékek összege?
"""


def main():
    for i in range(32, 128):
        print("{}: {}".format(i, chr(i)))

    print("Az angol ábécé nagybetűihez tartozó ASCII értékek összege: ",
          sum([i for i in range(65, 91)]))

##############################################################################


if __name__ == "__main__":
    main()
