def lista(p):
    f = open(p, "r").read()
    s = [f[i:i+3] for i in range(0, len(f), 3)] # hármasával szétvágás
    return s

def dict(text):
    f = open(text, "r").read()
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
    return dna

'''print(prot(lista("prot.rosalind"),dict("codontable")))'''