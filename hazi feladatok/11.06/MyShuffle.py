#!/usr/bin/env python3


import random


def my_shuffle(li):
    """Helyben összekeveri a listát majd azt adja vissza"""
    random.shuffle(li)
    return li


def shuffled(li):
    """Az eredeti lista másolatát keveri össze, és azt adja vissza"""
    tmp_li = li[:]
    random.shuffle(tmp_li)
    return tmp_li


def main():
    list1 = [1, 2, 3, 4]
    print(my_shuffle(list1)[-1])
    print(list1)

    list2 = [1, 2, 3, 4]
    print(shuffled(list2)[-1])
    print(list2)                  # az eredeti lista változatlan

##############################################################################


if __name__ == "__main__":
    main()
