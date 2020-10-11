#!/usr/bin/env python3


def munchausen(n):
    li = [int(i) for i in list(str(n))]
    osszeg = 0
    for i in li:
        if i == 0:
            continue
        osszeg += (i ** i)
        if osszeg > n:
            return False
    return osszeg == n


def main():
    #n = 10000
    n = 440000000
    for i in range(n):
        if munchausen(i):
            print(i)

##############################################################################


if __name__ == "__main__":
    main()
