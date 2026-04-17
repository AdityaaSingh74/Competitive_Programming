from typing import List

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        
        def cost(a, b):
            diff = abs(ord(a) - ord(b))
            return min(diff, 26 - diff)
        
        dp = [[[0]*(k+1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for x in range(k+1):
                dp[i][i][x] = 1
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                
                for x in range(k+1):
                    dp[i][j][x] = max(
                        dp[i+1][j][x],
                        dp[i][j-1][x]
                    )
                    
                    c = cost(s[i], s[j])
                    
                    if c <= x:
                        if i+1 <= j-1:
                            dp[i][j][x] = max(
                                dp[i][j][x],
                                2 + dp[i+1][j-1][x-c]
                            )
                        else:
                            dp[i][j][x] = max(dp[i][j][x], 2)
        
        return dp[0][n-1][k]