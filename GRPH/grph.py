import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn," ")
sys.path.append(pdn)

from beolvas import beolv

def grph(s):

    for i in s:
        for j in s:
            if i != j:

                if j[13:16] == i[(len(i)-3):(len(i))]:
                    print(i[:13], j[:13])


'''grph(beolv("grph.rosalind"))'''

