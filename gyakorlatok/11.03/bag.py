#!/usr/bin/env python3

class Bag:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def add_twice(self, value):
        self.add(value)
        self.add(value)

    def __str__(self):
        return "Bag(" + str(self.data) + ")"


def main():
    b = Bag()
    b.add(3)
    b.add(5)
    b.add_twice(9)
    print(b)

#############################################################################


if __name__ == "__main__":
    main()
