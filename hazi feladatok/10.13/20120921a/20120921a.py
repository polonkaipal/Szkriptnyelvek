#!/usr/bin/env python3

TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

EKEZETEK = {
    'á' : 'a',
    'é' : 'e',
    'í' : 'i',
    'ó' : 'o',
    'ö' : 'o',
    'ő' : 'o',
    'ú' : 'u',
    'ü' : 'u',
    'ű' : 'u',
    'Á' : 'A',
    'É' : 'E',
    'Í' : 'I',
    'Ó' : 'O',
    'Ö' : 'O',
    'Ő' : 'O',
    'Ú' : 'U',
    'Ü' : 'U',
    'Ű' : 'U'}

for k,v in EKEZETEK.items():
    TEXT = TEXT.replace(k, v)

def main():
    print(TEXT)

##############################################################################


if __name__ == "__main__":
    main()
