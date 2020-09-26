#!/usr/bin/env python3
"""
Sztring tisztítása

Hacker Hugó egy olyan szkripten dolgozik, mely proxy szerverek listáját tárolja egy lokális
SQLite adatbázisban. A szkript a proxy-k címét több publikus oldalról gyűjti össze
(pl. http://www.ip-adress.com/proxy_list/). A szkript a legtöbb URL-t helyesen szedi ki, viszont
egyes címekben whitespace karakterek is szerepelnek, pl.: "192.20.246.138:\n 6666",
"206.130.99.82:\n8080", stb. Segítsünk Hugónak egy olyan függvény megírásában, mely paraméterként
kap egy sztringet, visszatérési értéke pedig a whitespace-ektől megtisztított sztring legyen.
"""


def tisztit(s):
    return s.replace(' ', '').replace('\n', '')


def main():
    print(tisztit("192.20.246.138:\n 6666"))
    print(tisztit("206.130.99.82:\n8080"))

##############################################################################


if __name__ == "__main__":
    main()
