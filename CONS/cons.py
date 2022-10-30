import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from DNA.dna import coun
from beolvas import beolv, csakdna

def cons(s):
    so = csakdna(beolv(s),13)
    p = []
    for n in range(len(so[0])):
        p.append([])
        for m in so:
            p[n].append(m[n])
    profile = []
    for j in range(4):
        profile.append([])
        for i in p:
            profile[j].append(coun(i)[j])
    b = ["A", "C", "G", "T"]
    maxim = "".join(max(set(p[k]), key = p[k].count) for k in range(len(p)))
    print(maxim)
    for r in range(4):
        print (b[r]+": "+" ".join(str(x) for x in profile[r]))

'''cons("cons.rosalind")'''