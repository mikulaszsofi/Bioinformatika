def gc(s):
    f = open(s, "r")
    s = f.read().replace("\n","")
    n = s.split(">")
    n = n[1:] #az előző lépés után a lista első eleme " ", erre nincs szükség
    l =[]
    for i in n:
        d = i[13:] #csak a dna
        p = ((d.count("C")+d.count("G"))/len(d))*100
        l.append(p)
        if p == max(l):
            maxcode=i[:13]
            maxi=p
    print(maxcode)
    print(maxi)

'''gc("in")'''


