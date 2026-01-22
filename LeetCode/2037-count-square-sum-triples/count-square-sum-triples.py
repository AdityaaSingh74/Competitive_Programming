class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        L = list(range(1,n+1))
        for i in range(1,n):
            for j in range(1,n):
                ele = ((i*i)+(j*j))
                if sqrt(ele) > n:
                    break
                if sqrt(ele) in L:
                    cnt+=1
        return cnt