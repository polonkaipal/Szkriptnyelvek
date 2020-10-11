#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    return "".join([c for c in list(text) if c in chars])


def main():
    print("\"{}\"".format(valid("Barking!")))                              # -> "B"
    print("\"{}\"".format(valid("KL754", "0123456789")))                   # -> "754"
    print("\"{}\"".format(valid("BEAN", "abcdefghijklmnopqrstuvwxyz")))    # -> ""


##############################################################################


if __name__ == "__main__":
    main()
