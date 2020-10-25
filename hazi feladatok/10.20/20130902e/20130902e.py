#!/usr/bin/env python3


def test(s):
    VEREM = []
    for c in s:
        if c == '(':
            VEREM.append(c)
        elif c == ')':
            if VEREM.pop() != '(':
                return False
        elif c == '{':
            VEREM.append(c)
        elif c == '}':
            if VEREM.pop() != '{':
                return False
        elif c == '[':
            VEREM.append(c)
        elif c == ']':
            if VEREM.pop() != '[':
                return False
        else:
            continue
    return VEREM == []


def main():
    print(test("((5+3)*2+1)"))
    print(test("{[(3+1)+2]+}"))
    print(test("(3+{1-1)}"))
    print(test("[1+1]+(2*2)-{3/3}"))
    print(test("(({[(((1)-2)+3)-3]/3}-3)"))


##############################################################################


if __name__ == "__main__":
    main()
