import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from REVC.revc import compl #reverse complements

def dbru(t):
    s = set(t)
    sr = set()
    for i in s:
        sr.add(compl(i))

    ks = set()
    for i in s:
        ks.add(i[1:])
        ks.add(i[:-1])
    ksr = set()
    for i in sr:
        ksr.add(i[1:])
        ksr.add(i[:-1])
    srs = list(s.union(sr))
    srs.sort()
    edges = []
    for i in srs:
        if [i[:-1],i[1:]] not in edges:
            if (i[:-1] in ks and i[1:] in ksr) or (i[:-1] in ks and i[1:] in ks) or (i[:-1] in ksr and i[1:] in ksr) or (i[1:] in ks and i[:-1] in ksr):
                edges.append([i[:-1],i[1:]])

    return edges

'''f  = open('rosalind_dbru.txt','r').read().split('\n')
k = ('\n'.join(str(x) for x in dbru(f)))
l = k.replace('\'','').replace('[','(').replace(']',')')
print(l)'''


