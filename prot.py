def prot():
    f = open("../Bioinformatika/prot", "r").read()
    s = [f[i:i+3] for i in range(0, len(f), 3)] # hármasával szétvágás
    print(s)

def dict():
    f = open("codontable", "r").read()
    f = f.replace("\n"," ")
    f = list(f.split(" "))
    f.remove('') #ez csak az elsőt távolítja el

    print(f)

#prot()

dict()