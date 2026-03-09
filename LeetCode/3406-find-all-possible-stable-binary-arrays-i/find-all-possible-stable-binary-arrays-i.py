class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] = stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] = stable arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: runs of all 0s or all 1s (valid only if <= limit)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Ending in 0: last run of 0s has length 1..limit
                # preceded by a 1 (or nothing for pure-zero prefix)
                for k in range(1, min(i, limit) + 1):
                    if i - k == 0:
                        # entire prefix is zeros, valid base case handled
                        # but we need j == 0 for that; here j >= 1 so skip
                        pass
                    else:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-k][j][1]) % MOD
                
                # Ending in 1: last run of 1s has length 1..limit
                for k in range(1, min(j, limit) + 1):
                    if j - k == 0:
                        pass
                    else:
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j-k][0]) % MOD
        
        # Optimize with prefix sums for O(zero*one) total
        # Recompute using prefix sum optimization
        dp2 = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        for i in range(min(zero, limit) + 1):
            if i > 0: dp2[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            if j > 0: dp2[0][j][1] = 1
        
        # prefix_end0[i][j] = sum of dp2[i'][j][0] for i'=0..i
        # prefix_end1[i][j] = sum of dp2[i][j'][1] for j'=0..j
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # sum dp2[i-k][j][1] for k=1..min(i,limit)
                # = prefix1[i-1][j] - prefix1[i-1-limit][j]
                s0 = 0
                for k in range(1, min(i, limit) + 1):
                    s0 = (s0 + dp2[i-k][j][1]) % MOD
                dp2[i][j][0] = s0
                
                s1 = 0
                for k in range(1, min(j, limit) + 1):
                    s1 = (s1 + dp2[i][j-k][0]) % MOD
                dp2[i][j][1] = s1
        
        return (dp2[zero][one][0] + dp2[zero][one][1]) % MOD