#!/usr/bin/env python3

"""
Lista elemeinek szorzata

Írjunk függvényt, mely kap egy egészeket tartalmazó listát s visszaadja a listában lévő elemek
szorzatát.

Megjegyzés

Definíció szerint egy üres lista elemeinek a szorzata 1. Hasonlóképpen, egy üres lista elemeinek az
összege 0.
"""


def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p


def main():
    a = []
    b = [1, 2, 3]
    c = [4, 5, 6]
    print(product(a))
    print(product(b))
    print(product(c))

##############################################################################


if __name__ == "__main__":
    main()
