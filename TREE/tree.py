
def tree(file):
    f = open(file,'r').read().replace('\n', ' ').split(' ')
    n = int(f.pop(0))
    edges = []
    for i in range(int(len(f)/2)):
        edges.append([f[2*i],f[2*i+1]])

    return (n-len(edges)-1)

print(tree('tree.rosalind'))