from itertools import product

def lexf(l, n):
    comb = list(product(l,repeat=n))
    comb.sort() #lexicographic order
    for i in list(comb):
        print("".join(str(x) for x in i))

'''a = "A B C D E F G H I J"
l = a.split(" ")
lexf(l,2)'''

