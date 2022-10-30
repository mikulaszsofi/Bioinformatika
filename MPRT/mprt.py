import requests

def mprt(file):
    id = open(file, "r").read().split("\n") #beolvassa az ID-kat
    for i in id:
        j = requests.get("http://rest.uniprot.org/uniprotkb/"+i[:6]+".fasta").text.split("\n")[1:][:-1]
        p = ""
        for s in j:
            p+=s
        list = ""
        for l in range(len(p)-3):
            if (p[l] == "N") and (p[l+1] != "P") and (p[l+2] == "S" or p[l+2] == "T") and (p[l+3] != "P"):
                list+=str(l+1)
                list+=" "
        if list != "":
            print(i)
            print(list)

'''mprt("mprt.rosalind")'''

