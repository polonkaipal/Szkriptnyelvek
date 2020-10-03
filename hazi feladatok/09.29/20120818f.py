#!/usr/bin/env python3
"""
Négyzetek összege, összeg négyzete (PE #6)

Az első tíz természetes szám négyzetösszege:

12 + 22 + … + 102 = 385

Az első tíz természetes szám összegének a négyzete:

(1 + 2 + … + 10)2 = 552 = 3025

Vagyis az első tíz természetes szám összegének a négyzete és az első tíz természetes szám
négyzetösszege közti különbség: 3025 − 385 = 2640.

Számítsuk ki az első száz természetes szám összegének a négyzete és az első száz természetes szám
négyzetösszege közti különbséget!
"""


def negyzetekOsszegeOsszegekNegyzete(n):
    negyzetosszeg = 0
    osszeg = 0
    for i in range(1, n + 1):
        negyzetosszeg += i * i
        osszeg += i
    return osszeg * osszeg - negyzetosszeg


def main():
    print("10 -->", negyzetekOsszegeOsszegekNegyzete(10))
    print("100 -->", negyzetekOsszegeOsszegekNegyzete(100))

##############################################################################


if __name__ == "__main__":
    main()
