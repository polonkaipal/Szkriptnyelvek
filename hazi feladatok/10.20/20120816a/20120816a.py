#!/usr/bin/env python3


def rajzol(li):
    print("+-----------------+")
    for i in range(7, 0 - 1, -1):
        print('|', 'Q' if i == li[0] else '.', 'Q' if i == li[1] else '.',
                   'Q' if i == li[2] else '.', 'Q' if i == li[3] else '.',
                   'Q' if i == li[4] else '.', 'Q' if i == li[5] else '.',
                   'Q' if i == li[6] else '.', 'Q' if i == li[7] else '.', '|')
    print("+-----------------+")


def main():
    rajzol([7, 3, 0, 2, 5, 1, 6, 4])
    rajzol([0, 4, 7, 5, 2, 6, 1, 3])

##############################################################################


if __name__ == "__main__":
    main()
