class Solution:
    def climbStairs(self, n: int) -> int:
        ans=[1,2]
        if n>2:
            for i in range(2,n):
                m = ans[i-1] + ans[i-2]
                ans.append(m)
            return ans[-1]
        else:
            return ans[n-1]