def coun(s):
    a = s.count("A")
    c = s.count("C")
    g = s.count("G")
    t = s.count("T")
    print(a,c,g,t)

f = open("dna.rosalind", "r")
coun(f.read())