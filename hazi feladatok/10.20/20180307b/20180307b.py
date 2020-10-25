#!/usr/bin/env python3

#INPUT = "day04.txt"
INPUT = "sajat.txt"


def main():
    with open(INPUT, 'r') as f:
        db = 0
        for sor in f:
            li = []
            reszek = ["".join(sorted(list(s))) for s in sor.split()]
            for s in reszek:
                if s not in li:
                    li.append(s)
                else:
                    continue
            if li == reszek:
                db += 1
        print(db)

##############################################################################


if __name__ == "__main__":
    main()
