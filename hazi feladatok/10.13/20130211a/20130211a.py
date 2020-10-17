#!/usr/bin/env python3


def normalize(s):
    return s.lower().replace(' ', '')

def isAnagramma(s1, s2):
    return sorted(list(normalize(s1))) == sorted(list(normalize(s2)))

def main():
    print("\"{}\" == \"{}\" : \"{}\"".format("A gentleman", "Elegant man", isAnagramma("A gentleman", "Elegant man")))
    print("\"{}\" == \"{}\" : \"{}\"".format("Debit card", " Bad credit", isAnagramma("Debit card", " Bad credit")))
    print("\"{}\" == \"{}\" : \"{}\"".format("azta", "pasta", isAnagramma("azta", "pasta")))

##############################################################################


if __name__ == "__main__":
    main()
