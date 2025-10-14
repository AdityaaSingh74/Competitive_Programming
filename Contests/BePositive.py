def no_of_negetive(s):
    count = 0
    for i in s:
        if int(i) < 0:
            count += 1
    return count

def be_positive(s):
    neg_cnt = no_of_negetive(s)
    cnt = 0
    for i in s:
        if (i<0 and neg_cnt%2!=0):
            cnt+=2
            neg_cnt-=1
        if i==0:
            cnt+=1
    return cnt

n = int(input())
for i in range(n):
    m = int(input())
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    print(be_positive(s))
