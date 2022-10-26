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

def orf(so,m):
    # szövegben megkeresi a megfelelő részszövegeket (M-től az első Stopig)
    lista = []
    dna=''
    for e in so:
        # szótár alapján átírás, Stop helyett " ", hogy az is egy karakter legyen
        x = m.index(e)
        if m[x+1] !='Stop':
            dna+=m[x+1]
        else:
            dna+=" "
    list = dna.split(" ")
    if dna[len(dna)-1] != " ":
        # ha nem Stopra végződött, az utolsó szövegrészletben nincsen keresett részszöveg
        list.remove(list[len(list)-1])
    for i in list:
        for a in range(len(i)):
            if i[a] == "M":
                # M-ek szerint vágás
                lista.append(i[a:])
    return(lista)

def compl(dna):
    # reverse complement
    s = dna.replace("T", "t").replace("A","a").replace("G","g").replace("C","c")
    sc = s.replace("t","A").replace("a","T").replace("g","C").replace("c","G")
    comp = sc[::-1]
    return(comp)

def h(b):
    # T-k kicserélése U-kra + 3-asával felvágás
    f = b.replace("T","U").replace("\n","")
    s = [f[i:i+3] for i in range(0, len(f), 3)] # hármasával szétvágás
    if len(s[len(s)-1]) != 3:
        s.remove(s[len(s)-1])
    return(s)

g = open("orf.rosalind", "r").read()

# 3 féle csúsztatással kell megnézni
a = orf(h(g[15:]),dict("codontable"))
b = orf(h(g[16:]),dict("codontable"))
c = orf(h(g[17:]),dict("codontable"))

# reverse complement-re ugyanez
p = compl(g[15:])

d = orf(h(p),dict("codontable"))
e = orf(h(p[1:]),dict("codontable"))
r = orf(h(p[2:]),dict("codontable"))

# listák összeadása, hogy minden elem egyszer szerepeljen
v = []
for i in a+b+c+d+e+r:
    if i not in v:
        v.append(i)

#kiírás
for j in v:
    print (j)
