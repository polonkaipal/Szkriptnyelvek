#!/usr/bin/env python3
"""
Hangrend

Döntsük el egy magyar szóról, hogy milyen hangrendű (mély, magas, vagy vegyes hangrendű).

Ha egy szóban vmennyi magánhangzó mély hangrendű, akkor a szó mély hangrendű. Ha egy szóban vmennyi magánhangzó magas hangrendű, akkor a szó magas hangrendű. Ha egy szóban mély és magas hangrendű magánhangzók is előfordulnak, akkor a szó vegyes hangrendű.

Mély hangrendű magánhangzók: a, á, o, ó, u, ú.

Magas hangrendű magánhangzók: e, é, i, í, ö, ő, ü, ű.

Példák

    "ablak" → mély
    "erkély" → magas
    "kisvasút" → vegyes
    "magas" → mély :)
    "mély" → magas :)

Segítség

Ha ékezetes karaktereket is használunk, akkor érdemes egy speciális sort beszúrni a forráskód elejére (lásd 1. gyakorlat). A magas és mély magánhangzókat egy-egy sztringben is letárolhatjuk:

MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'
...
words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
"""


MELY = 'aáoóuú'
MAGAS = 'eéiíöőüű'


def hangrend(s):
    mely = False
    magas = False
    for c in s:
        if not mely:
            mely = c in MELY
        if not magas:
            magas = c in MAGAS
    if mely and magas:
        return "vegyes"
    if mely:
        return "mély"
    if magas:
        return "magas"
    return None


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    for s in words:
        print("'{}' -> {}".format(s, hangrend(s)))

##############################################################################


if __name__ == "__main__":
    main()
