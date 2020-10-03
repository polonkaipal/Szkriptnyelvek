#!/usr/bin/env python3


def main():
    # 1. feladat
    # ['auto', 'villamos', 'metro'] → ['AUTO!', 'VILLAMOS!', 'METRO!']
    print("1:", [s.upper() + '!' for s in ['auto', 'villamos', 'metro']])

    # 2. feladat
    # ['aladar', 'bela', 'cecil'] → ['Aladar', 'Bela', 'Cecil']
    print("2:", [s.capitalize() for s in ['aladar', 'bela', 'cecil']])

    # 3. feladat
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], azaz inicializáljunk egy 10-elemű listát csupa 0-val.
    print("3:", [0 for i in range(10)])

    # 4. feladat
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    # print([j * 2 for j in [i for i in range(1, 11)]])
    print("4:", [i for i in range(2, 22, 2)])

    # 5. feladat
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak)
    print("5:", [int(s) for s in [str(i) for i in range(1, 11)]])

    # 6. feladat
    # "1234567" → [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként)
    print("6:", [int(c) for c in "1234567"])

    # 7. feladat
    # 'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát
    print("7:", [len(s)
                 for s in "The quick brown fox jumps over the lazy dog".split()])

    # 8. feladat
    # "python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában
    print("8:", [s[0] for s in "python is an awesome language".split()])

    # 9. feladat
    # 'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).
    print("9:", [(s, len(s))
                 for s in "The quick brown fox jumps over the lazy dog".split()])

    # 10. feladat
    # [0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat
    # print([i for i in range(10) if i % 2 == 0])
    print("10:", [i for i in range(0, 10, 2)])

    # 11. feladat
    # Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
    print("11:", [i * i for i in range(20) if i * i % 2 == 0])

    # 12. feladat
    # Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).
    print("12:", [i * i for i in range(20) if i * i % 10 == 4])

    # 13. feladat
    # Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    print("13:", "".join([chr(i) for i in range(ord('A'), ord('Z') + 1)]))

    # 14. feladat
    # [' apple ', ' banana ', ' kiwi'] → ['apple', 'banana', 'kiwi'], vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket
    print("14:", [s.strip() for s in [' apple ', ' banana ', ' kiwi']])

    # 15. feladat
    # [1, 0, 1, 1, 0, 1, 0, 0] → "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé
    print("15:", "".join([str(i) for i in [1, 0, 1, 1, 0, 1, 0, 0]]))

##############################################################################


if __name__ == "__main__":
    main()
