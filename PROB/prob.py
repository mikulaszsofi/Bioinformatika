import math

def prob(s):
    f = open(s,"r").read().replace("\n", " ").split(" ")
    dna = f[0]
    f.remove(f[0])
    for i in f:
        pr = 1
        for j in dna:
            if j == "C" or j == "G":
                pr = pr*float(i)/2
            else:
                pr = pr*(1-float(i))/2
        print(math.log(pr,10))

'''prob("prob.rosalind")'''