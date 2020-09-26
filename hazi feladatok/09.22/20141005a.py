#!/usr/bin/env python3
# encoding: utf-8
"""
valami_1 or valami_2 or … valami_N

Tekintsük az alábbi egyszerű kis programot:
"""

import sys


def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp.lower() == 'y' or inp == 'yes':    # <- egyszerűbben?
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')

##############################################################################


if __name__ == "__main__":
    main()
