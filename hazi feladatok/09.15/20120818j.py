#!/usr/bin/env python3

"""
20120818j

Számjegyek száma

Hány számjegyből áll 2256?

Tipp: hatványozásra a ** operátort használjuk, pl. 2**3 = 8. A túlcsordulástól nem kell félni :)
"""

def main():
    print('2^256 számjegyeinek darabszáma: ', len(list(str(2**256))))

##############################################################################


if __name__ == "__main__":
    main()
