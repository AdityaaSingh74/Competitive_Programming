

def Collataz_COnjecture(k,x):
    for i in range(k):
        x*=2
    return x

n=int(input())
res=[]
for i in range(n):
    s = input().split()
    k = int(s[0])
    x = int(s[1])
    res.append(Collataz_COnjecture(k,x))

for i in res:
    print(i)
