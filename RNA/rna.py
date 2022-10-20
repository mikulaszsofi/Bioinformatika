def replace(dna):
    rna = dna.replace("T","U")
    print(rna)

f = open("rna.rosalind","r")
replace(f.read())