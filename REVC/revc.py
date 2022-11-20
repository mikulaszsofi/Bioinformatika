def compl(dna):
    s = dna.replace("T", "t").replace("A","a").replace("G","g").replace("C","c")
    sc = s.replace("t","A").replace("a","T").replace("g","C").replace("c","G")
    comp = sc[::-1]
    return comp

'''f = open("revc", "r")
print(compl(f.read()))'''
