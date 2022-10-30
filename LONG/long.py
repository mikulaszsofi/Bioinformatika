import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn," ")
sys.path.append(pdn)

from beolvas import beolv, csakdna

def long(l, e, h):
    # a lista első elemének végének lehető leghosszabb részével passzolót ragasztom hozzá
    k = l
    x = int((h+1)/2)
    dna = k[0]
    k.remove(k[0])
    for i in range(h, x-1, -1):
        elhasznalt = []
        for j in k:
            if j[:i] == dna[(len(dna)-i):(len(dna))]:
            # ha a dna végének i hosszú része egyezik a j első i betűjével, hozzáragasztom az i+1.-től
            # hogy ne lépjen ki a forciklusból, eltárolom, melyikeket ragasztottam már hozzá, és később egyben kiveszem k-ból
                if j not in elhasznalt:
                    dna = dna + j[i:]
                    elhasznalt.append(j)
        for elh in elhasznalt:
            k.remove(elh)
    e = e+1
    # e: felváltva a dna végéhez próbálok újakat ragasztani, és egy új kezdődna-t találni
    if k != []:
        if e%2 == 1:
            ujlist=[]
            ujlist.append(dna)
            for p in k:
               ujlist.append(p)
            long(ujlist,e,h)
        else:
            k.append(dna)
            long(k,e,h)
    else:
        print(dna)

'''ha = csakdna(beolv("long.rosalind"),13)
hos = len(ha[0])
long(csakdna(beolv("long.rosalind"),13),1, hos)'''

