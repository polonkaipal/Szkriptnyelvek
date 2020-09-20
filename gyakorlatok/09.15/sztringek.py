#!/usr/bin/env python3

PI = 3.141592654

def hello(name, color, what):
    # géza, kék az ég!

    # v1
    #print("{0}, {1} a(z) {2}! Ki? {0}".format(name, color, what))

    # v2
    #print("{}, {} a(z) {}!".format(name, color, what))

    # v3
    print("{nev}, {szin} a(z) {obj}!".format(nev=name.capitalize(),
                                           szin=color,
                                           obj=what))

    # v4
    #print(f"1 + 1 = { 1 + 1 }")
    #print(f"{name}, {color} a(z) {what}!")

def main():
    hello("géza", "kék", "ég")
    print("-" * 30)
    hello("julcsi", "piros", "autó")

##############################################################################

if __name__ == "__main__":
    main()
