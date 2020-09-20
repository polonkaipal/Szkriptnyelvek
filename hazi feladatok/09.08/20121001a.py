#!/usr/bin/env python3

"""
Legyen egy konkrét sztring metódusos feladat is. A program a következőképpen működjön:

$ ./name.py
Name:         Laci           <E>
Hello Laci!

Vagyis a program interaktív módon kérje be a nevünket. A nevünk előtt és után hagyjunk szóközöket.
A példában az "<E>" az Enter billentyű lenyomását jelöli. A program üdvözöljön minket a példában
feltüntetett módon.
"""

def main():
    s = input("Name: ").strip()
    print("Hello " + s + "!")

##############################################################################

if __name__ == "__main__":
    main()
