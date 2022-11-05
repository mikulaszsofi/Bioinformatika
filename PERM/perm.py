from itertools import permutations
def fact(n):
    f = 1
    for i in range(n):
        f*=(i+1)
    return f

def perm(n):
    perm = permutations(range(1,n+1))
    for i in list(perm):
        print(" ".join(str(x) for x in i))

'''print(fact(6))
perm(6)'''

