def seto(n,A,B):
    C = set(range(1,n+1))
    u = A.union(B)
    i = A.intersection(B)
    ad = A.difference(B)
    bd = B.difference(A)
    ca = C.difference(A)
    cb = C.difference(B)

    print(u)
    print(i)
    print(ad)
    print(bd)
    print(ca)
    print(cb)


