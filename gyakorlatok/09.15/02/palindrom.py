#!/usr/bin/env python3

def is_palindrome(s):
    return s == s[::-1]

def main():
    print(is_palindrome("122"))
    print(is_palindrome("121"))

##############################################################################

if __name__ == "__main__":
    main()
