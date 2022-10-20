def beolv(k):
    f = open(k, "r")
    s = f.read().replace("\n", "")
    n = s.split(">")
    n = n[1:]  # az előző lépés után a lista első eleme " ", erre nincs szükség
    return n

def csakdna(l, n): #lista és a nem dna rész hossza
    dn = []
    for i in l:
        dn.append(i[n:])
    return dn
