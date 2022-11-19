
def sset(n):
    x = 1
    for i in range(n):
        x=(x*2)%1000000
    return x

print(sset(937))