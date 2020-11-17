#!/usr/bin/env python3


class Sor():
    """Sor osztály implementációja"""

    def __init__(self):
        """Inicializáció"""
        self.data = []

    def ures(self):
        """True vagy False értékkel tér vissza attól függően, hogy üres-e a Sor"""
        return not bool(len(self.data))

    def betesz(self, value):
        """Sor bővítése"""
        self.data.append(value)

    def meret(self):
        """Sor méretének a visszaadása"""
        return len(self.data)

    def kivesz(self):
        """Sor hamarabbi elemének a visszaadása, ha nem üres,
        egyébként None a visszatérési érték"""
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

    def __str__(self):
        """Sor objektum szöveges megjelenítése"""
        return "<" + str(self.data).replace(",", "") + "<"


def main():
    sor = Sor()        # üres sor létrehozása
    print(sor)         # <[]<
    print(sor.ures())  # True
    sor.betesz(1)
    sor.betesz(4)
    sor.betesz(5)
    print(sor)         # <[1 4 5]<
    print(sor.meret())  # 3
    print(sor.ures())  # False
    x = sor.kivesz()
    print(x)           # 1
    print(sor)         # <[4 5]<
    sor.kivesz()
    sor.kivesz()       # most már üres
    x = sor.kivesz()
    # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    print(x)

##############################################################################


if __name__ == "__main__":
    main()
