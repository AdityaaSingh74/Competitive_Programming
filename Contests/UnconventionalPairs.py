def unconventionalPairs(s):
    s.sort()
    max = 0
    for i in range(0,len(s),2):
        if max < abs(s[i] - s[i+1]):
            max = abs(s[i] - s[i+1])
    return max
            


n = int(input())
for i in range(n):
    m = int(input())
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])
    print(unconventionalPairs(s))
