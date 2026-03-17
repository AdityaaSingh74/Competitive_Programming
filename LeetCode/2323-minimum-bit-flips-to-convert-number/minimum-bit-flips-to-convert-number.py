class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        s = bin(start)[2:]
        e = bin(goal)[2:]
        lens = len(s)
        lene = len(e)
        if lens <lene:
            s = (("0"*(lene-lens)) + s)
        else:
            e = (("0"*(lens-lene)) + e)

        for i in range(len(s)):
            if s[i] != e[i]:
                ans += 1
                
        return ans
