#!/usr/bin/env python3


def main():
    # ['auto', 'villamos', 'metro'] → ['AUTO!', 'VILLAMOS!', 'METRO!']
    li1 = ['auto', 'villamos', 'metro']
    LI1 = [s.upper() + '!' for s in li1]
    print(LI1)

    # ['aladar', 'bela', 'cecil'] → ['Aladar', 'Bela', 'Cecil'] 
    li2 = ['aladar', 'bela', 'cecil']
    Li2 = [s.capitalize() for s in li2]
    print(Li2)

    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], azaz inicializáljunk egy 10-elemű listát csupa 0-val. 
    li3 = [0 for i in range(10)]
    print(li3)

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 
    li4 = [i for i in range(1, 11)]
    LI4 = [i * 2 for i in li4]
    print(LI4)

    # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak) 
    li5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    LI5 = [int(s) for s in li5]
    print(LI5)

    # "1234567" → [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként) 
    s = "1234567"
    S = [int(c) for c in s]
    print(S)

    # 'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát 
    li6 = 'The quick brown fox jumps over the lazy dog'
    LI6 = [len(s) for s in li6.split(' ')]
    print(LI6)

    # "python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában 
    li7 = "python is an awesome language"
    LI7 = [s[0] for s in li7.split(' ')]
    print(LI7)

    # 'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz). 
    li8 = 'The quick brown fox jumps over the lazy dog'
    LI8 = [(s, len(s)) for s in li8.split(' ')]
    print(LI8)

    # [0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat 
    li9 = [i for i in range(2, 10, 2)]
    print(li9)

    

##############################################################################

if __name__ == "__main__":
    main()
