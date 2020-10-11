#!/usr/bin/env python3


def greet(name, greetings="Hello"):
    print(f"{greetings} {name}!")


def hello(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(name + postfix)


def main():
    # greet("Pali")
    # greet("Pali", greetings="Hola")
    # greet("Pali", greetings="Bonjour")

    hello("Pali")
    print('-'*25)
    hello("Pali", repeat=2)
    print('-'*25)
    # számít a sorrend, de a legjobb ha kiírjuk a nevüket, akkor viszont már nem számít sorrend
    hello("Pali", 2, '!')

#############################################################################


if __name__ == "__main__":
    main()
