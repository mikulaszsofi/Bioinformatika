import sys, os

dn = os.path.dirname(__file__)
pdn = os.path.join(dn,".")
sys.path.append(pdn)

from PCOV.pcov import pcov
from REVC.revc import compl

import networkx as nx

def gasm(m):
    l = open(m,'r').read().split('\n')
    k = len(l[0])
    for j in range(k-1, 1, -1):
        G = nx.DiGraph()
        reads = []
        for item in l:
            for i in range(k - j + 1):
                reads.append(item[i:i+j])
                reads.append(compl(item[i:i+j]))
        reads = set(reads)

        for node in reads:
            G.add_node(node)
        for item1 in reads:
            for item2 in reads:
                if item2[:(j-1)] == item1[1:]:
                    G.add_edge(item1, item2)
        cycles = sorted(nx.simple_cycles(G))
        if len(cycles) == 2:
            break
    h = []
    for cycle in cycles:
        s = cycle[0]
        for i in range(1, len(cycle)):
            s = s + cycle[i][len(cycle[i]) - 1]
        h.append(s[:len(s) - j + 1])

    return h[0]

print(gasm('rosalind_gasm.txt'))