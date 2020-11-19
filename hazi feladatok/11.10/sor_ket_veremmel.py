#!/usr/bin/env python3


import verem


class Sor:
    def __init__(self):
        """Inicializáció"""
        self.verem1 = verem.Verem()
        self.verem2 = verem.Verem()

    def ures(self):
        """True vagy False értékkel tér vissza attól függően, hogy üres-e a Sor"""
        return self.verem1.ures() and self.verem2.ures()

    def betesz(self, value):
        """Sor bővítése"""
        self.verem1.betesz(value)

    def kivesz(self):
        """Sor hamarabbi elemének a visszaadása, ha nem üres,
        egyébként None a visszatérési érték"""

        # ha a két verem üres, akkor a sor is üres
        if self.verem1.ures() and self.verem2.ures():
            return None

        # ha 2. verem üres és az első nem üres
        elif self.verem2.ures() and not self.verem1.ures():
            while not self.verem1.ures():
                self.verem2.betesz(self.verem1.kivesz())
            return self.verem2.kivesz()

        # egyébként
        else:
            return self.verem2.kivesz()

    def meret(self):
        """Sor méretének a visszaadása"""
        return self.verem1.meret() + self.verem2.meret()


def main():
    sor = Sor()               # üres sor létrehozása
    print(sor.ures())         # True
    sor.betesz(1)
    sor.betesz(4)
    sor.betesz(5)
    print(sor.meret())        # 3
    print(sor.ures())         # False
    x = sor.kivesz()
    print(x)                  # 1
    sor.kivesz()
    sor.kivesz()       # most már üres
    x = sor.kivesz()
    # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
    print(x)

##############################################################################


if __name__ == "__main__":
    main()
