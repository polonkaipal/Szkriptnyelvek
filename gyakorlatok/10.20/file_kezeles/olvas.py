#!/usr/bin/env python3


def main():
    # olvasás
    f = open("szoveg.txt", "r")
    
    sorok = f.read().splitlines()
    print(sorok)

    f.close()

    # írás
    f = open("out.txt", "w")
    print("hello", file=f)
    print("word", file=f)
    f.write("ab\n")
    f.write("ba\n")

    f.close()

#############################################################################


if __name__ == "__main__":
    main()
