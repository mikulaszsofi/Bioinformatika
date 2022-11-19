def subs(s,t):
    k =[]
    for i in range(len(s)-len(t)+1):
        if s[i:(i+len(t))] == t:
            k.append(i+1)
    return k

'''s = open("s.rosalind","r").read()
t = open("t.rosalind", "r").read()

print("\n".join(str(x) for x in subs(s,t)))'''




