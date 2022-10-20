def lista():
    f = open("prot.rosalind", "r").read()
    s = [f[i:i+3] for i in range(0, len(f), 3)] # hármasával szétvágás
    return s

def dict():
    f = open("codontable", "r").read()
    f = f.replace("\n"," ")

    f = list(f.split(" "))
    c = f.count('')
    while c>0:
        f.remove('')
        c=c-1
    #f.remove('') #ez csak az elsőt távolítja el

    return f

def prot(l,m):
    dna=''
    for e in l:
        x = m.index(e)
        if m[x+1] !='Stop':
            dna=dna+m[x+1]
    print(dna)

prot(lista(),dict())