#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 3:
        print("Hiba!")
        return -1

    print("{} + {} = {}".format(sys.argv[1],
                                sys.argv[2], int(sys.argv[1]) + int(sys.argv[2])))
    return 0

##############################################################################


if __name__ == "__main__":
    main()
