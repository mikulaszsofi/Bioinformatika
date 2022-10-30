def iprb(k,m,n):
    # adott típusú választásának valószínűsége
    s = k+m+n
    kk = k/s*(k-1)/(s-1) # 1 vszéggel lesz dom. allélja
    km = k/s*m/(s-1)*2 # 1
    kn = k/s*n/(s-1)*2 # 1
    mm = m/s*(m-1)/(s-1) # 1-(1/2*1/2)=3/4
    mn = m/s*n/(s-1)*2 # 1/2
    nn = n/s*(n-1)/(s-1) # 0

    return (kk+km+kn+(3/4)*mm+(1/2)*mn)

'''print(iprb(int(open("iprb.rosalind", "r").read().split(" ")[0]), int(open("iprb.rosalind", "r").read().split(" ")[1]), int(open("iprb.rosalind", "r").read().split(" ")[2])))'''
