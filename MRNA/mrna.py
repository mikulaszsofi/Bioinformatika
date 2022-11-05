'''lista a szótár elemeiből'''
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

def mrna(rna):
    total = 3 #STOP-ok száma
    for i in rna:
        n = dict("codontable").count(i)
        total = (total*n)%1000000
    return total

'''a = open("mrna.rosalind","r").read()
print(mrna(a))'''