def hamm(s,t):
    h = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            h+=1
    return h

'''a = open("hamm.rosalind", "r").read().split("\n")
b = a[0]
c = a[1]
print(hamm(b,c))'''