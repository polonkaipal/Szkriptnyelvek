#!/usr/bin/env python3


class Verem():
    """Verem osztály implementációja"""

    def __init__(self):
        """Inicializáció"""
        self.data = []

    def ures(self):
        """True vagy False értékkel tér vissza attól függően, hogy üres-e a Verem"""
        return not bool(len(self.data))

    def betesz(self, value):
        """Verem bővítése"""
        self.data.append(value)

    def meret(self):
        """Verem méretének a visszaadása"""
        return len(self.data)

    def kivesz(self):
        """Verem utoljára betett elemének a visszaadása, ha nem üres,
        egyébként None a visszatérési érték"""
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def __str__(self):
        """Verem objektum szöveges megjelenítése"""
        return str(self.data).replace("]", "").replace(",", "")


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

##############################################################################


if __name__ == "__main__":
    main()
