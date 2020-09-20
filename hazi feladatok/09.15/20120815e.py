#!/usr/bin/env python3

"""
Palindróm

Írjunk függvényt, mely egy sztringről eldönti, hogy palindróm-e. Egy karaktersorozatot akkor
nevezünk palindrómnak, ha visszafelé olvasva megegyezik az eredeti karaktersorozattal, pl.: görög.

A feladatot többféleképpen is oldjuk meg:

(1) Triviális módszer (Pythonban egy szekvencia nagyon egyszerűen megfordítható).

(2) Iteratív módszer. A sztringről nem készíthetünk másolatot.

Tipp: használhatunk egy while ciklust is. Hasonlóan működik a C nyelvben megismertekkel:
i = 0
while i < 5:
    print(i)
    i += 1

(3) Rekurzív módszer. Csak hogy szokjuk a rekurziót is.
"""

TEXT = "görög"
TEXT2 = "török"


# 1. módszer
def palindrom1(s):
    return s == s[::-1]


# 2. módszer
def palindrom2(s):
    hossz = len(s) - 1
    for i in range(0, hossz + 1):
        if s[i] != s[hossz - i]:
            return False
    return True


# 3. módszer
def palindrom3(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return palindrom3(s[1:-1])
    else:
        return False


def main():
    print("'{}' {}palindróm".format(TEXT, "" if palindrom1(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom1(TEXT2) else "nem "))

    print("")
    print("'{}' {}palindróm".format(TEXT, "" if palindrom2(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom2(TEXT2) else "nem "))

    print("")
    print("'{}' {}palindróm".format(TEXT, "" if palindrom3(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom3(TEXT2) else "nem "))

##############################################################################


if __name__ == "__main__":
    main()
