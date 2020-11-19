#!/usr/bin/env python3


def main():
    cnt = 0
    with open("day02.txt", "r") as file:
        for sor in file:
            tmp = [int(i) for i in sor.split()]
            cnt += max(tmp) - min(tmp)
        #
    #
    print("Ellenőrző összeg:", cnt)

##############################################################################


if __name__ == "__main__":
    main()
