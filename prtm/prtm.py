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

def prtm(d, s):
    sum = 0
    for w in open(s,'r').read():
        sum+=float(d[d.index(w)+1])
    print (sum)

prtm(dict("masstable"), "prtm.rosalind")



#print(dict("masstable"))

