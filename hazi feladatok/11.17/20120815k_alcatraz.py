#!/usr/bin/env python3


MAX = 600


def main():
    # Az első lépésben úgy is kinyitjuk mindegyiket
    cellak = [True for i in range(MAX + 1)]

    for i in range(2, MAX + 1):
        for j in range(i, MAX + 1, i):
            cellak[j] = not cellak[j]
        #
    #

    nyitottAjtokSzama = [str(index) for index, ertek in enumerate(cellak[1:], start=1) if ertek]
    # A négyzetszámú cellalakók szabadulnak
    print("".join(nyitottAjtokSzama))


##############################################################################


if __name__ == "__main__":
    main()
