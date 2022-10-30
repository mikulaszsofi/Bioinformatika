def coun(s):
    a = s.count("A")
    c = s.count("C")
    g = s.count("G")
    t = s.count("T")
    return(a,c,g,t)

'''f = open("dna.rosalind", "r")
print(coun(f.read()))'''