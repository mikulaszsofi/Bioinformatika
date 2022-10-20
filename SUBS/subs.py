def subs(s,t):
    for i in range(len(s)-len(t)+1):
        if s[i:(i+len(t))] == t:
            print(i+1)


s = open("s.rosalind","r").read()
t = open("t.rosalind", "r").read()

subs(s,t)




