import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from DNA.dna import coun
from beolvas import beolv, csakdna

import numpy as np

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
    maxim = ""
    for k in range(len(p)):
        maxim+= max(set(p[k]), key = p[k].count)
    print(maxim)
    for r in range(4):
        print(b[r],":", profile[r])


cons("cons.rosalind")