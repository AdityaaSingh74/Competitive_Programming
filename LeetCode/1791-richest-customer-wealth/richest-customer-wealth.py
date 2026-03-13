class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = -10000000
        for i in accounts:
            a = sum(i)
            if maxx < a:
                maxx = a
        return maxx