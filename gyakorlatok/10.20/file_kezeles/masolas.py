#!/usr/bin/env python3

INPUT = "szoveg.txt"
OUTPUT = "out.txt"

def main():
    f1 = open(INPUT, "r")
    to = open(OUTPUT, "w")
    for line in f1:
        to.write(line)

    to.close()
    f1.close()

#############################################################################


if __name__ == "__main__":
    main()
