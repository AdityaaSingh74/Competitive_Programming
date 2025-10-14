
res=[]
n=int(input())
for i in range(n):
    N = int(input())
    p = list(map(int, input().split()))
    q = list(range(2, N + 1)) + [1]
    
    res.extend(q)
    res.append(-1)

for i in res:
    if i == -1:
        print()
        continue
    print(i,end=" ")
