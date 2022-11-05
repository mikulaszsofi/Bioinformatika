import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from beolvas import beolv, csakdna
from PROT.prot import prot, dict
from SUBS.subs import subs
from RNA.rna import replace

def splc(l):
    all = list(csakdna(beolv(l),13))
    dna = all[0]
    introns = all[1:]
    for i in introns:
        h = subs(dna,i)[0]-1
        dna = dna[:h]+dna[(h+len(i)):]
    return prot([replace(dna)[i:i + 3] for i in range(0, len(dna), 3)], dict("codontable"))


'''print(splc("splc.rosalind"))'''