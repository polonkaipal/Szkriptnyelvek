#!/usr/bin/env python3

def get_movie_info():
    # t.f.h. kapcsolódunk egy AB-hoz
    # s visszaadjuk egy táblázat egy sorát
    return ("Total Recall", 1990, 7.5)

def main():
    (cim, ev, ertekeles) = get_movie_info()    
    print(cim, ev, ertekeles)
##############################################################################

if __name__ == "__main__":
    main()
