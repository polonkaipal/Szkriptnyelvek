#!/usr/bin/env python3


def is_palindrome(n):
    """Kettes és tizes számrendszeri számról eldönti, hogy palindróm-e"""
    s = str(n).replace("0b", "")
    return s == s[::-1]


def main():
    N = 1_000_000
    cnt = 0
    for i in range(1, N):
        if is_palindrome(i) and is_palindrome(bin(i)):
            cnt += i
        #
    #
    print(cnt)

##############################################################################


if __name__ == "__main__":
    main()
