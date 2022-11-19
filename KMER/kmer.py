import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from beolvas import beolv, csakdna
from LEXF.lexf import lexf
from SUBS.subs import subs

def kmer(l,n):
    s = csakdna(beolv(l),n)
    l = ['A','C','G','T']
    m = lexf(l, 4)
    p = []
    for i in m:
        p.append(len(subs(str(s),str(i))))
    return p

'''print(' '.join(str(i) for i in kmer('kmer.rosalind',13)))'''
