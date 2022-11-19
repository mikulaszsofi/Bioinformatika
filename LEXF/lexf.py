from itertools import product

def lexf(l, n):
    comb = list(product(l,repeat=n))
    comb.sort() #lexicographic order
    d = []
    for i in list(comb):
        d.append("".join(str(x) for x in i))
    return d

'''a = "A B C D E F G H I J"
l = a.split(" ")
f = lexf(l,2)
print('\n'.join(str(j) for j in f))'''

