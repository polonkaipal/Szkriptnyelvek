#!/usr/bin/env python3


def ciklus(n, debug=False):
    if debug:
        print("# ciklus kezdete")
    print(str([i for i in range(1, n + 1)]).replace("[", "").replace("]", ""))
    if debug:
        print("# ciklus vége")


def main():
    ciklus(10)
    print()
    ciklus(10, debug=True)

#############################################################################


if __name__ == "__main__":
    main()
