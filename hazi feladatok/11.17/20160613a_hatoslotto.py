#!/usr/bin/env python3


MAX = 45


def ehetiSzamok(osszeg, szorzat):
    for i in range(1, MAX + 1):
        for j in range(i + 1, MAX + 1):
            for k in range(j + 1, MAX + 1):
                for l in range(k + 1, MAX + 1):
                    for m in range(l + 1, MAX + 1):
                        for n in range(m + 1, MAX + 1):
                            if ((i + j + k + l + m + n) == osszeg and (i * j * k * l * m * n) == szorzat):
                                return (i, j, k, l, m, n)


def main():
    szamok = ehetiSzamok(90, 996300)
    print("Nyerő számok:", szamok)

##############################################################################


if __name__ == "__main__":
    main()
