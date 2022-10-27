def new(a,k):
    return a*k

def fib(n,k):
    nb = 1 #newborn pairs
    na = 0 #adult pairs
    p = 0 #parents pairs
    for i in range(n-1):
        p += na
        na = nb
        nb = new(p,k)
    return nb+na+p

print(fib(int(open("fib.rosalind", "r").read().split(" ")[0]), int(open("fib.rosalind", "r").read().split(" ")[1])))