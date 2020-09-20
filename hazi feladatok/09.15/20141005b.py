#!/usr/bin/env python3

"""
haladó sztringformázás

Nézze át az alábbi két blogbejegyzést a haladó sztringformázásról, majd írjon egy egyszerű kis
szkriptet, amely valamelyik haladó módszer alkalmazását mutatja be.

String formatting in Python - http://knowledgestockpile.blogspot.hu/2011/01/string-formatting-in-python_09.html
Python String Format Cookbook - http://mkaz.com/2012/10/10/python-string-format/
"""


def main():
    adatok = ["Learn Programming in Python with Cody Jackson",
              "Cody Jackson", 34.9901]
    print("'{title}' - {author} : ${dollar:.2f}".format(
        title=adatok[0], author=adatok[1], dollar=adatok[2]))


##############################################################################

if __name__ == "__main__":
    main()
