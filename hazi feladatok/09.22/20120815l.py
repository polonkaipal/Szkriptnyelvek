#!/usr/bin/env python3
"""
Rejtélyes üzenet

A fater régi jegyzetei között túrkálva megakad a szemünk egy könyvön, melynek a borítóján a
következő cím díszeleg: "A programozás alapjai". Hmm, nem is tudtuk, hogy ilyet is tanult az öreg…
Belelapozva egy megsárgult papír hullik a lábunk elé, rajta egy rejtélyes üzenettel:

Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb

A papír túloldalán csupán ennyi áll: "K → M, O → Q, E → G".

Ez vajon mi lehet? Meg tudjuk fejteni az elkódolt szöveget?

Megjegyzés

A dekódolt szöveg formája egyezzen meg a fenti üzenet alakjával: ugyanannyi sorból álljon,
figyeljünk a kis- és nagybetűkre, stb.
"""

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""


def fordit(s, mennyivel):
    rendes = []
    for c in TEXT:
        c = ord(c)
        if c >= 65 and c <= 90:
            c += mennyivel
            c = c % 91 + 65 if c > 90 else c
            rendes.append(chr(c))
        elif c >= 97 and c <= 122:
            c += mennyivel
            c = c % 123 + 97 if c > 122 else c
            rendes.append(chr(c))
        else:
            rendes.append(chr(c))
    return "".join(rendes)


def main():
    print(fordit(TEXT, 2))

##############################################################################


if __name__ == "__main__":
    main()
