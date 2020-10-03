#!/usr/bin/env python3
TEXT = "görög"
TEXT2 = "török"


# 1. módszer
def palindrom1(s):
    return s == s[::-1]


# 2. módszer
def palindrom2(s):
    hossz = len(s) - 1
    for i in range(0, hossz + 1):
        if s[i] != s[hossz - i]:
            return False
    return True


# 3. módszer
def palindrom3(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return palindrom3(s[1:-1])
    else:
        return False


def main():
    print("'{}' {}palindróm".format(TEXT, "" if palindrom1(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom1(TEXT2) else "nem "))

    print("")
    print("'{}' {}palindróm".format(TEXT, "" if palindrom2(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom2(TEXT2) else "nem "))

    print("")
    print("'{}' {}palindróm".format(TEXT, "" if palindrom3(TEXT) else "nem "))
    print("'{}' {}palindróm".format(TEXT2, "" if palindrom3(TEXT2) else "nem "))

##############################################################################


if __name__ == "__main__":
    main()
