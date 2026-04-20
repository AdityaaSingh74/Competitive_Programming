class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        cnt=0
        n=len(colors)

        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                cnt = max(cnt,abs(i))

        for i in range(n):
            if colors[i]!=colors[-1]:
                cnt = max(cnt,abs(n-i-1))
        
        return cnt
        
