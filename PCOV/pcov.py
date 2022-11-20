import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from DBRU.dbru import dbru
from REVC.revc import compl

def pcov(s):
    graph = dbru(s)
    hamilton = [graph[0][0]]
    bnodes = [x[0] for x in graph]
    enodes = [x[1] for x in graph]
    i = bnodes.index(enodes[0])
    while i != 0: #search Hamilton cycle
        hamilton.append(enodes[i])
        i = bnodes.index(enodes[i])
    cycle = ''.join(str(x[0]) for x in hamilton)
    return compl(cycle)


'''f = open('rosalind_pcov.txt','r').read().split('\n')
print(pcov(f))'''


