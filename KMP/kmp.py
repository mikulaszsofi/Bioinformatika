def kmp(s):
    f = open(s, "r").read().replace("\n","")[14:]
    fail = []
    for i in range(len(f)):
        fail.append(0)
        for j in range(1,i):
            if f[i-j:i] == f[:j]:
                fail[i-1] = j
            else:
                break
    return(fail)

'''print(""+" ".join(str(x) for x in kmp("kmp.rosalind")))'''